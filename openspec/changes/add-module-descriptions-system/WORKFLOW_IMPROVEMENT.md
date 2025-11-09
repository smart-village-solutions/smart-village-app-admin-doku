# Verbesserter Workflow: Module mit Human-in-the-Loop

## Problem

Der aktuelle Workflow automatisiert zu viel und lässt keinen Raum für menschliche Expertise:
- KI erstellt Modul-Beschreibung
- ❌ Direkt automatische Validierung, Git, PR
- ❌ Keine Möglichkeit für Korrekturen und Ergänzungen

## Lösung: 3-Schritt-Prozess pro Modul

### Schritt 1: KI-basierte Erstellung (Draft)

**Tool:** Neues Script `scripts/draft_module.py`

```bash
python3 scripts/draft_module.py --name "Modulname"
```

**Was passiert:**
1. KI sammelt verfügbare Informationen (Doku, Schema, ähnliche Module)
2. Erstellt **Draft** in `yml/modules/DRAFT-[name].yml`
3. Öffnet Datei im Editor
4. **STOPPT** und wartet auf menschlichen Input

**Ausgabe:**
```
✓ Draft erstellt: yml/modules/DRAFT-modulname.yml
📝 Bitte überprüfen und ergänzen:
   - Beschreibungen korrekt?
   - Fehlende Informationen?
   - Use Cases vollständig?

→ Wenn fertig: python3 scripts/review_module.py --name modulname
```

### Schritt 2: Human Review & Iteration (Loop)

**Du bearbeitest die Datei:**
- Korrigierst falsche Annahmen
- Ergänzt fehlendes Wissen
- Verfeinert Beschreibungen
- Kann mehrere Iterationen durchlaufen
- **Kein Zeitdruck!**

**Tool:** `scripts/review_module.py`

```bash
python3 scripts/review_module.py --name modulname
```

**Was passiert:**
1. Liest DRAFT-Datei
2. Zeigt Zusammenfassung
3. Fragt: "Bereit für Finalisierung? [y/n/edit]"
   - `n` → Zurück zum Editor
   - `edit` → Öffnet Editor nochmal
   - `y` → Weiter zu Schritt 3

**Optional: Interaktive Ergänzung**
```bash
python3 scripts/review_module.py --name modulname --interactive
```
- Stellt gezielte Fragen zu fehlenden Feldern
- "Welche external_services werden genutzt?"
- "Gibt es spezielle customization_options?"

### Schritt 3: Finalisierung & Automatisierung

**Tool:** `scripts/finalize_module.py`

```bash
python3 scripts/finalize_module.py --name modulname
```

**Was passiert:**
1. Entfernt `DRAFT-` Prefix
2. Generiert vollständige YAML mit global.yml
3. Validiert gegen Schema
4. **Optional:** Git-Branch + Commits
5. **Optional:** Registriert in city_app.yml
6. **Optional:** Erstellt PR

**Mit Flags steuerbar:**
```bash
# Nur validieren, kein Git
python3 scripts/finalize_module.py --name modulname --no-git

# Validieren + Git, aber kein PR
python3 scripts/finalize_module.py --name modulname --no-pr

# Alles
python3 scripts/finalize_module.py --name modulname --full
```

## Workflow-Diagramm

```
┌─────────────────────────────────────────────────────────────┐
│ Schritt 1: KI Draft                                         │
│ $ python3 scripts/draft_module.py --name "Modulname"       │
│                                                              │
│ → Erstellt: yml/modules/DRAFT-modulname.yml                │
│ → Öffnet Editor                                             │
│ → WARTET                                                     │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│ Schritt 2: Human Review (LOOP)                             │
│                                                              │
│ Du bearbeitest DRAFT-modulname.yml:                         │
│ • Korrigierst Fehler                                        │
│ • Ergänzt Details                                           │
│ • Verfeinert Texte                                          │
│                                                              │
│ $ python3 scripts/review_module.py --name modulname        │
│                                                              │
│ Bereit? [y/n/edit]                                          │
│  ├─ n/edit → Zurück zum Editor ─┐                          │
│  └─ y → Weiter                   │                          │
└──────────────────────┬────────────┘                          │
                       │             ▲                         │
                       │             └─────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────────────────┐
│ Schritt 3: Finalisierung                                    │
│ $ python3 scripts/finalize_module.py --name modulname      │
│                                                              │
│ → Entfernt DRAFT- Prefix                                    │
│ → Generiert vollständige YAML                               │
│ → Validiert Schema                                          │
│ → [Optional] Git Branch + Commits                           │
│ → [Optional] Registriert in city_app.yml                   │
│ → [Optional] Erstellt PR                                    │
│                                                              │
│ ✓ Modul fertig!                                             │
└─────────────────────────────────────────────────────────────┘
```

## Beispiel-Session

```bash
# Terminal 1: Draft erstellen
$ python3 scripts/draft_module.py --name "Chatbot"

Sammle Informationen für Modul 'Chatbot'...
  ✓ Ähnliche Module gefunden: Feedback, Umfragen
  ✓ Schema-Anforderungen geladen
  ✓ Topic vorgeschlagen: feedbackmodul

Draft erstellt: yml/modules/DRAFT-chatbot.yml
📝 Editor geöffnet - Bitte überprüfen!

[Editor öffnet sich automatisch]

# Du bearbeitest die Datei, speicherst

# Terminal: Review starten
$ python3 scripts/review_module.py --name chatbot

Modul-Zusammenfassung:
  Name: Chatbot
  Topic: feedbackmodul
  Description: 150 Zeilen
  Dependencies: 3
  External Services: 2

Bereit für Finalisierung? [y/n/edit]: n

# Zurück zum Editor, weitere Änderungen

$ python3 scripts/review_module.py --name chatbot
Bereit für Finalisierung? [y/n/edit]: y

# Terminal: Finalisierung
$ python3 scripts/finalize_module.py --name chatbot --full

  ✓ DRAFT-chatbot.yml → chatbot.yml
  ✓ Vollständige YAML generiert
  ✓ Schema-Validierung erfolgreich
  ✓ Git Branch erstellt: feature/module-chatbot
  ✓ 3 Commits erstellt
  ✓ In city_app.yml registriert
  ✓ PR erstellt: #42

Modul 'Chatbot' erfolgreich finalisiert!
PR: https://github.com/smart-village-solutions/.../pull/42
```

## Vorteile

1. **Klare Trennung:** Draft → Review → Finalisierung
2. **Flexibilität:** Mehrere Iterationen möglich
3. **Kontrolle:** Du entscheidest, wann es weitergeht
4. **Sicherheit:** Keine ungewollten Git-Operationen
5. **Lerneffekt:** KI lernt aus deinen Korrekturen

## Migration bestehender Module

Für bereits erstellte Module (Abfallkalender, Mängelmelder, Karten):
```bash
# Zurück zu Draft-Status für Review
python3 scripts/revert_to_draft.py --name maengelmelder

# Review und ggf. verbessern
python3 scripts/review_module.py --name maengelmelder

# Erneut finalisieren
python3 scripts/finalize_module.py --name maengelmelder --full
```

## Nächste Schritte

1. ✅ Workflow-Konzept definiert
2. ⏳ `draft_module.py` implementieren
3. ⏳ `review_module.py` implementieren
4. ⏳ `finalize_module.py` implementieren
5. ⏳ `create_module.py` entsprechend anpassen
6. ⏳ Bestehende Module testen
7. ⏳ Phase 3 mit neuem Workflow starten
