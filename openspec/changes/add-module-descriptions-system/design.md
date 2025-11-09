# Design: Template-System für Modulbeschreibungen

## Context

Die Smart Village App umfasst über 60 verschiedene Module. Jedes Modul muss gemäß dem `app-module.schema.json` beschrieben werden. Die bestehenden Beispiele (nachrichten.yml, veranstaltungen.yml) zeigen, dass:

- Viele Felder identisch sind (z.B. `opencode_repository`, `deployed_in_municipalities`)
- Einige Felder modulspezifisch sind (z.B. `name`, `topic`, `description`)
- Die YAML-Dateien umfangreich sind (150-200 Zeilen)

**Stakeholder:**
- Projektdokumentation-Team (Erstellung der Beschreibungen)
- Entwickler (technische Dokumentation)
- Kommunen (Übersicht über verfügbare Module)

## Goals / Non-Goals

### Goals
- Vereinfachte Erstellung neuer Modulbeschreibungen durch Template-System
- Zentrale Verwaltung gemeinsamer Daten (DRY-Prinzip)
- Interaktives CLI-Tool für geführte Modulerstellung
- Automatische Validierung gegen Schema
- Konsistente Struktur über alle Module

### Non-Goals
- Automatische Generierung von Beschreibungstexten (KI-generiert)
- Migration bestehender Module (bleiben manuell erstellte YAML-Dateien)
- Änderung des bestehenden Schemas
- Web-UI für die Modulerstellung

## Decisions

### 1. Zwei-Schichten-Architektur: Global + Modul-spezifisch

**Entscheidung:** Aufteilung in `global.yml` (gemeinsame Daten) und individuelle Modul-Dateien.

**Begründung:**
- Felder wie `opencode_repository` und `deployed_in_municipalities` sind bei allen Modulen identisch
- Bei Änderungen (z.B. neue Kommune) muss nur eine Datei aktualisiert werden
- Reduziert Redundanz von ~150 Zeilen pro Modul auf ~80 Zeilen

**Alternativen:**
- Vollständige manuelle YAML-Dateien: Fehleranfällig, hohe Redundanz
- Datenbank-System: Zu komplex für statische Dokumentation
- JSON statt YAML: Weniger menschenlesbar

**Struktur:**

```yaml
# global.yml - Standardwerte für alle Module
common:
  opencode_repository: "https://gitlab.opencode.de/bad-belzig/smart-village-app-app"
  development_status: "Production"
  deployed_in_municipalities:
    - "Angermünde"
    - "Augsburg"
    # ... weitere 42 Kommunen

# yml/modules/abfallkalender.yml - Nutzt globale Werte
name: "Abfallkalender"
topic: "abfallkalender"
short_description: "Übersicht über Müllabfuhr-Termine"
# ... nur modulspezifische Felder
# deployed_in_municipalities wird von global.yml übernommen

# yml/modules/chatbot.yml - Überschreibt globale Werte
name: "Chatbot"
topic: "chatbot"
short_description: "KI-gestützter Assistent"
development_status: "Beta"  # ← Überschreibt "Production" aus global.yml
deployed_in_municipalities:  # ← Überschreibt globale Liste
  - "Bad Belzig"  # Nur in einer Kommune im Einsatz
  - "Kiel"
```

**Merge-Logik (Priorität):**
1. Modul-spezifische Werte (höchste Priorität)
2. Globale Werte (wenn nicht im Modul definiert)
3. Schema-Defaults (wenn weder Modul noch global definiert)

### 2. Python-basiertes CLI-Tool

**Entscheidung:** Interaktives Python-Skript `create_module.py` mit Prompts.

**Begründung:**
- Python bereits für validate_schemas.py genutzt
- Einfache Integration mit bestehenden YAML/JSON-Tools
- Colored output für bessere UX
- Läuft direkt im Terminal ohne zusätzliche Dependencies

**Alternativen:**
- Bash-Skript: Weniger robust für YAML-Verarbeitung
- Node.js: Zusätzliche Runtime erforderlich
- Web-Interface: Überdimensioniert für interne Nutzung

**Features:**
```python
# Interaktiver Modus
python scripts/create_module.py --interactive

# Oder mit Parametern
python scripts/create_module.py --name "Abfallkalender" --topic "abfallkalender"
```

### 3. Schema-basierte Validierung nach Generierung

**Entscheidung:** Generierte YAML-Dateien werden automatisch validiert.

**Begründung:**
- Stellt sicher, dass generierte Dateien dem Schema entsprechen
- Nutzt bestehendes `validate_schemas.py`
- Verhindert fehlerhafte Commits

**Workflow:**
1. Modul-Informationen eingeben → `yml/modules/[name].yml`
2. YAML generieren → `yml/[name].yml`
3. Automatische Validierung gegen `app-module.schema.json`
4. Bei Fehler: Korrektur und erneute Generierung

### 4. Dateistruktur

**Entscheidung:**
```
yml/
├── global.yml                    # Gemeinsame Daten
├── modules/                      # Modul-spezifische Teilinformationen
│   ├── abfallkalender.yml
│   ├── app-intro.yml
│   └── ...
├── nachrichten.yml               # Vollständige YAML (bestehend)
├── veranstaltungen.yml           # Vollständige YAML (bestehend)
├── abfallkalender.yml            # Generiert aus global.yml + modules/abfallkalender.yml
└── ...                           # Weitere generierte Module

scripts/
├── create_module.py              # Interaktives Erstellungstool
└── generate_module_yaml.py       # YAML-Generator
```

**Begründung:**
- Klare Trennung zwischen Quellen (modules/) und Ausgabe (yml/)
- Bestehende Module bleiben unverändert
- Einfache Git-History (nur geänderte Modul-Files committen)

### 5. Automatische Registrierung in city_app.yml

**Entscheidung:** `generate_module_yaml.py` fügt generierte Module automatisch zur `city_app.yml` hinzu.

**Begründung:**
- Module müssen in `city_app.yml` unter `modules:` registriert werden, um von außen erreichbar zu sein
- Manuelle Registrierung ist fehleranfällig und wird oft vergessen
- Automatische Integration stellt sicher, dass generierte Module sofort verfügbar sind

**Workflow:**
1. Modul wird generiert → `yml/[name].yml`
2. Generator prüft, ob URL bereits in `city_app.yml` existiert
3. Falls nicht: Füge URL zum `modules:`-Array hinzu
4. Format: `https://raw.githubusercontent.com/smart-village-solutions/smart-village-app-admin-doku/main/yml/[name].yml`

**Alternativen:**
- Manuelle Registrierung: Fehleranfällig, wird vergessen
- Separate Sync-Script: Zusätzliche Komplexität
- CLI-Prompt nach Generierung: Unterbricht den Flow

### 6. Git-Workflow mit Branch und Pull Request

**Entscheidung:** Jedes neue Modul wird in einem eigenen Feature-Branch entwickelt und per PR integriert.

**Begründung:**
- Ermöglicht Code-Review vor Integration
- Verhindert direkte Commits auf `main`
- Erlaubt CI/CD-Validierung vor Merge
- Dokumentiert Änderungen klar in Git-History

**Workflow:**
```bash
# Nach Modulerstellung
1. create_module.py erstellt Branch: feature/module-[modulname]
2. Generierung und Commits im Feature-Branch
3. Automatisches Erstellen eines PR nach GitHub
4. Review und Approval
5. Merge in main
```

**Implementierung:**
- `create_module.py` erstellt automatisch Branch
- Nutzt GitHub CLI (`gh`) für PR-Erstellung
- PR-Template mit Checkliste (Validierung, Dokumentation, etc.)
- Optional: Auto-Merge bei erfolgreicher CI-Validierung

**Alternativen:**
- Direct commits auf main: Keine Review-Möglichkeit
- Manueller Branch-Workflow: Konsistent, aber aufwändiger
- Trunk-based development: Weniger Kontrolle bei Bulk-Erstellung

## Risks / Trade-offs

### Risiko: Synchronisation zwischen Quellen und generierten Dateien

**Problem:** Nutzer könnten generierte YAML-Dateien direkt bearbeiten statt die Quellen zu ändern.

**Mitigation:**
- Kommentar in generierten Dateien: `# AUTO-GENERATED - Edit yml/modules/[name].yml instead`
- Pre-commit Hook zur Warnung bei direkten Änderungen
- Dokumentation des Workflows

### Trade-off: Zwei Wahrheiten (Quellen vs. generierte Dateien)

**Trade-off:** Komplexität durch zusätzliche Abstraktionsschicht.

**Akzeptiert weil:**
- Gemeinsame Daten reduzieren Fehler erheblich
- Pflegeaufwand für 60+ Module rechtfertigt die Komplexität
- Alternativ: Manuelle Pflege wäre noch fehleranfälliger

### Risiko: Schema-Änderungen

**Problem:** Änderungen am `app-module.schema.json` erfordern Anpassung des Generators.

**Mitigation:**
- Schema-Version in global.yml referenzieren
- Generator validiert gegen aktuelles Schema
- Tests für Generator mit allen Schema-Feldern

## Migration Plan

### Phase 1: Setup (Tag 1)
1. `global.yml` erstellen mit gemeinsamen Daten aus nachrichten.yml
2. `create_module.py` und `generate_module_yaml.py` implementieren
3. Template für `modules/[name].yml` definieren
4. Validierung in CI/CD integrieren

### Phase 2: Proof of Concept (Tag 1-2)
1. 3 Module als Piloten erstellen:
   - Abfallkalender (einfaches Modul)
   - Mängelmelder (komplexes Modul)
   - Karten (mit vielen Dependencies)
2. Feedback einholen und Tool verbessern

### Phase 3: Bulk-Erstellung (Tag 2-5)
1. Modulinformationen sammeln (aus vorhandenen Docs, PDFs, etc.)
2. Module in Gruppen erstellen:
   - Basis-Module (Einstellungen, Suche, etc.)
   - Content-Module (Nachrichten, Veranstaltungen, etc.)
   - Spezial-Module (AR, Chatbot, etc.)
3. Kontinuierliche Validierung

### Phase 4: Dokumentation & Rollback-Plan
1. README für Module-Erstellung aktualisieren
2. Rollback: Bei Problemen bleiben Original-YAMLs funktionsfähig
3. Git-History ermöglicht Rückkehr zu manuellen Dateien

## Open Questions

1. **Wie werden Screenshots bereitgestellt?**
   - Aktuell: Mock-URLs in YAML
   - Langfristig: Reale Screenshots hosten?

2. **Sollen deprecated Module gekennzeichnet werden?**
   - `development_status: "Deprecated"` nutzen?
   - Separate Liste für nicht mehr unterstützte Module?

3. **Mehrsprachigkeit für Modulbeschreibungen?**
   - Aktuell nur Deutsch
   - Englische Versionen parallel pflegen?
   - Lösung: Zunächst nur Deutsch, später i18n-System

4. **Versionierung der Modulbeschreibungen?**
   - Aktuell: `last_update` Feld
   - Git-History ausreichend oder explizite Versionsnummern?
