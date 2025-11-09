# Implementation Tasks: Module Description System

## 1. Setup Phase ✅ ABGESCHLOSSEN

### 1.1 Erstelle global.yml mit gemeinsamen Daten ✅
- [x] Datei `yml/global.yml` erstellen
- [x] Gemeinsame Felder aus nachrichten.yml extrahieren:
  - `opencode_repository`
  - `deployed_in_municipalities` (42 Kommunen)
- [x] Dokumentation für global.yml hinzufügen

### 1.2 Erstelle Verzeichnisstruktur ✅
- [x] Verzeichnis `yml/modules/` erstellen
- [x] Verzeichnis `scripts/` erstellen (falls nicht vorhanden)

### 1.3 Implementiere YAML-Generator ✅
- [x] Script `scripts/generate_module_yaml.py` erstellen (317 Zeilen)
- [x] Funktion: global.yml einlesen
- [x] Funktion: modules/[name].yml einlesen
- [x] Funktion: Beide Quellen mergen (3-Level-Priorität)
- [x] Funktion: Validierung gegen app-module.schema.json
- [x] Funktion: YAML-Datei in yml/[name].yml schreiben
- [x] Header-Kommentar hinzufügen: `# AUTO-GENERATED FROM yml/modules/[name].yml + yml/global.yml`
- [x] **Funktion: city_app.yml automatisch aktualisieren**
  - Prüfen, ob Modul-URL bereits in `modules:` Array existiert
  - Falls nicht: GitHub-Raw-URL hinzufügen
  - Format: `https://raw.githubusercontent.com/smart-village-solutions/smart-village-app-admin-doku/main/yml/[name].yml`
  - YAML-Struktur von city_app.yml beibehalten (inkl. Kommentare)
- [x] CLI-Optionen: `--module`, `--all`, `--no-register`
- [x] Colored terminal output
- [x] Getestet mit Abfallkalender-Modul (erfolgreich)

### 1.4 Implementiere interaktives CLI-Tool ✅
- [x] Script `scripts/create_module.py` erstellen (489 Zeilen)
- [x] **Git-Branch automatisch erstellen**
  - Branch-Name: `feature/module-[modulname]`
  - Von aktuellem `main` abzweigen
  - Automatisch auschecken
- [x] Interaktive Prompts für alle Pflichtfelder:
  - `name` (Modulname)
  - `topic` (aus Schema-Enum, 30+ Optionen)
  - `short_description`
  - `usage_scenario`
  - `description`
- [x] Optionale Felder abfragen:
  - `interfaces`
  - `dependencies`
  - `external_services`
  - `customization_options`
  - `involved_actors`
- [x] Colored output für bessere UX
- [x] Speichern in `yml/modules/[name].yml`
- [x] Automatischer Aufruf von generate_module_yaml.py
- [x] Automatische Validierung
- [x] **Git-Commits erstellen**
  - Commit 1: `feat(module): add [name] partial`
  - Commit 2: `feat(module): generate [name] complete YAML`
  - Commit 3: `feat(module): register [name] in city_app.yml`
- [x] **Pull Request erstellen**
  - GitHub CLI (`gh pr create`) nutzen
  - Titel: `feat(module): Add [Modulname] module description`
  - Body: Automatisch generiert mit Moduldetails
  - Fallback wenn gh CLI nicht verfügbar

### 1.5 Erweitere validate_schemas.py ✅
- [x] Option `--all` für Validierung aller yml/*.yml Dateien
- [x] Ignoriere yml/global.yml (Template, kein vollständiges Modul)
- [x] Colored summary für alle Module
- [x] **Validierung von city_app.yml gegen city-app-schema.json**
- [x] Exit codes für CI/CD Integration
- [x] Getestet: 4/4 Validierungen erfolgreich

### 1.6 GitHub CLI Setup ✅
- [x] Prüfe, ob `gh` CLI installiert ist ✅ Installiert: v2.83.0
- [x] Fallback: Manuelle PR-Erstellung mit URL
- [x] Dokumentiere GitHub CLI Installation
- [x] Hinweis auf Authentifizierung: `gh auth login`

### 1.7 PR-Template erstellen ✅
- [x] Datei `.github/PULL_REQUEST_TEMPLATE.md` erstellt
- [x] Template für Modul-PRs mit Checkliste:
  - [x] Modul validiert gegen Schema
  - [x] In city_app.yml registriert
  - [x] Screenshots vorhanden (falls zutreffend)
  - [x] Dokumentation vollständig
  - [x] Technical documentation URL funktioniert
- [x] Testing-Anweisungen integriert
- [x] Labels konfiguriert

### 1.8 Dokumentation ✅
- [x] README-Abschnitt für Modulerstellung hinzugefügt
- [x] Beispiel-Workflow dokumentiert
- [x] Voraussetzungen dokumentiert (Python, gh CLI)
- [x] Verzeichnisstruktur erklärt
- [x] Template-System dokumentiert (Override-Konzept)
- [x] Links zu OpenSpec-Dokumentation

### 1.9 Completion Report ✅
- [x] `PHASE1_COMPLETION.md` erstellt
- [x] Alle Features dokumentiert
- [x] Test-Ergebnisse dokumentiert
- [x] Metriken erfasst (1200+ Zeilen Code)
- [x] Nächste Schritte definiert

## 2. Proof of Concept Phase ✅ ABGESCHLOSSEN

### 2.1 Pilotmodul: Abfallkalender (einfach) ✅
- [x] Modulinformationen sammeln
- [x] Modul mit generate_module_yaml.py erstellen (in Phase 1 als Test)
- [x] Generierte YAML-Datei reviewen
- [x] Validierung prüfen (erfolgreich)
- [x] Tool funktioniert einwandfrei

### 2.2 Pilotmodul: Mängelmelder (komplex) ✅
- [x] Modulinformationen sammeln (3 Varianten dokumentiert)
- [x] Modul manuell erstellen (yml/modules/maengelmelder.yml)
- [x] Komplexe Felder getestet:
  - 3 external_services
  - 5 involved_actors
  - 3 Varianten im description
  - development_status: Beta (Override)
  - cost field (Override)
- [x] Generierte YAML-Datei reviewen (180 Zeilen)
- [x] Validierung erfolgreich

### 2.3 Pilotmodul: Karten (mit Dependencies) ✅
- [x] Modulinformationen sammeln
- [x] Modul manuell erstellen (yml/modules/karten.yml)
- [x] Dependencies und Interfaces getestet:
  - 3 dependencies
  - 5 interfaces
  - 4 external_services
  - 4 involved_actors
- [x] Topic-Issue identifiziert ("karten" nicht im Schema → "tourismusinformationen")
- [x] Generierte YAML-Datei reviewen (200 Zeilen)
- [x] Validierung erfolgreich

### 2.4 Feedback-Runde ✅
- [x] Tool-Usability bewertet (5/5 Sterne für Generator & Validator)
- [x] Erkenntnisse dokumentiert (PHASE2_FEEDBACK.md)
- [x] Verbesserungspotential identifiziert:
  - Schema: Topic-Enum erweitern (HOCH)
  - create_module.py noch nicht getestet (MITTEL)
  - Varianten-Strukturierung (NIEDRIG)
  - Screenshots fehlen (NIEDRIG)
- [x] Metriken erfasst: ~23 Min/Modul, 30-35h für 60 Module
- [x] Empfehlungen für Phase 3 formuliert

## 2.5 Workflow-Verbesserung ✅ ABGESCHLOSSEN

### 2.5.1 Neue Scripts für Human-in-the-Loop ✅
- [x] `scripts/draft_module.py` implementiert (378 Zeilen)
  - AI-basierter Entwurf als DRAFT-[name].yml
  - Öffnet Editor und wartet
  - Interaktive CLI mit Schema-basierten Prompts
- [x] `scripts/review_module.py` implementiert (287 Zeilen)
  - Zeigt Modul-Zusammenfassung
  - Validierung gegen Schema
  - Vollständigkeits-Check mit Warnungen
  - Iterative Bearbeitung möglich
  - Explizite Freigabe-Entscheidung
- [x] `scripts/finalize_module.py` implementiert (422 Zeilen)
  - Entfernt DRAFT-Prefix
  - Generiert finale YAML mit global.yml merge
  - Registriert in city_app.yml
  - Git-Workflow mit Flags (--no-git, --no-pr, --full)
  - 3 Commits: Partial, Complete YAML, Registration

### 2.5.2 Workflow-Dokumentation ✅
- [x] WORKFLOW_IMPROVEMENT.md erstellt
  - 3-Schritt-Prozess dokumentiert
  - Workflow-Diagramm
  - Beispiel-Session
  - Migration-Strategie für bestehende Module

### 2.5.3 Stub-Generator ✅
- [x] `scripts/create_empty_module_stubs.py` implementiert
  - Prüft automatisch existierende Module
  - Erstellt STUB-Dateien für fehlende Module
  - Intelligentes Topic-Mapping
  - 46 Stubs erfolgreich generiert

## 3. Bulk-Erstellung Phase (46 Module)

**Workflow pro Modul (5 Schritte):**

1. **Branch erstellen:** `git checkout -b feature/module-[name]` → tasks.md aktualisieren
2. **STUB befüllen:** AI-generiert oder manuell → tasks.md aktualisieren
3. **Review:** Validierung und Korrekturen → tasks.md aktualisieren
4. **PR erstellen:** Commit und PR öffnen → tasks.md aktualisieren
5. **Nach Merge:** PR mergen, `main` pullen, Schema-Validierung durchführen, tasks.md aktualisieren

### 3.1 Basis-Module (9 Module)

#### 3.1.1 App-Intro ✅

- [x] Branch erstellen: `feature/module-app-intro`
- [x] STUB befüllen (DRAFT-app-intro.yml → app-intro.yml)
- [x] Human Review & Korrekturen
- [x] Commit & PR nach Freigabe
- [x] PR gemergt & Schema-Validierung erfolgreich

#### 3.1.2 Einstellungen

- [ ] Branch erstellen: `feature/module-einstellungen`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.1.3 Suche

- [ ] Branch erstellen: `feature/module-suche`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.1.4 Navigation

- [ ] Branch erstellen: `feature/module-navigation`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.1.5 Merkliste/Favoriten

- [ ] Branch erstellen: `feature/module-merkliste-favoriten`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.1.6 Push-Nachrichten

- [ ] Branch erstellen: `feature/module-push-nachrichten`
- [ ] STUB befüllen (DRAFT bereits vorhanden)
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.1.7 Nachrichten/Informationen

- [ ] Branch erstellen: `feature/module-nachrichten-informationen`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.1.8 Veranstaltungen

- [ ] Branch erstellen: `feature/module-veranstaltungen`
- [ ] Bestehendes Modul prüfen und ggf. aktualisieren
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.1.9 Bilderslider

- [ ] Branch erstellen: `feature/module-bilderslider`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

### 3.2 Content-Module (4 Module)

#### 3.2.1 Statische Seiten
- [ ] Branch erstellen: `feature/module-statische-seiten`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.2.2 Statische Listen/Kacheln
- [ ] Branch erstellen: `feature/module-statische-listen-kacheln`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.2.3 Schwarzes Brett
- [ ] Branch erstellen: `feature/module-schwarzes-brett`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.2.4 Störer
- [ ] Branch erstellen: `feature/module-stoerer`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

### 3.3 Bürgerdienste-Module (8 Module)

#### 3.3.1 Bürgerbeteiligung/Consul
- [ ] Branch erstellen: `feature/module-buergerbeteiligung-consul`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.3.2 Feedback-Formular
- [ ] Branch erstellen: `feature/module-feedback-formular`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.3.3 Umfragen
- [ ] Branch erstellen: `feature/module-umfragen`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.3.4 Terminbuchung
- [ ] Branch erstellen: `feature/module-terminbuchung`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.3.5 Postfach
- [ ] Branch erstellen: `feature/module-postfach`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.3.6 Zuständigkeitsfinder
- [ ] Branch erstellen: `feature/module-zustaendigkeitsfinder`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.3.7 Rathaus-Informationssystem
- [ ] Branch erstellen: `feature/module-rathaus-informationssystem`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.3.8 Content-Sharing
- [ ] Branch erstellen: `feature/module-content-sharing`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

### 3.4 Meldewesen-Module (5 Module)

#### 3.4.1 Mängelmelder (einfach)
- [ ] Branch erstellen: `feature/module-maengelmelder-einfach`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.4.2 Mängelmelder (mit Schnittstelle)
- [ ] Branch erstellen: `feature/module-maengelmelder-mit-schnittstelle`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.4.3 Hinweisgebersystem
- [ ] Branch erstellen: `feature/module-hinweisgebersystem`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.4.4 Fristenmelder
- [ ] Branch erstellen: `feature/module-fristenmelder`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.4.5 Warnmeldungen
- [ ] Branch erstellen: `feature/module-warnmeldungen`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

### 3.5 Informations-Module (7 Module)

#### 3.5.1 Baustellen/Verkehrsstörungen
- [ ] Branch erstellen: `feature/module-baustellen-verkehrsstoerungen`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.5.2 Wetter
- [ ] Branch erstellen: `feature/module-wetter`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.5.3 Wassertemperatur
- [ ] Branch erstellen: `feature/module-wassertemperatur`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.5.4 ÖPNV-Daten (Abfahrtspläne)
- [ ] Branch erstellen: `feature/module-oepnv-daten-abfahrtsplaene`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.5.5 Datenvisualisierungen
- [ ] Branch erstellen: `feature/module-datenvisualisierungen`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.5.6 Dashboard
- [ ] Branch erstellen: `feature/module-dashboard`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.5.7 Abfallkalender
- [ ] Branch erstellen: `feature/module-abfallkalender`
- [ ] Bestehendes Modul prüfen und ggf. aktualisieren
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

### 3.6 Wirtschafts-Module (6 Module)

#### 3.6.1 Branchenbuch/Wegweiser
- [ ] Branch erstellen: `feature/module-branchenbuch-wegweiser`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.6.2 Stellenanzeigen
- [ ] Branch erstellen: `feature/module-stellenanzeigen`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.6.3 Produkte und Dienstleistungen
- [ ] Branch erstellen: `feature/module-produkte-und-dienstleistungen`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.6.4 Gastro-Angebote
- [ ] Branch erstellen: `feature/module-gastro-angebote`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.6.5 Gutscheine
- [ ] Branch erstellen: `feature/module-gutscheine`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.6.6 Treueclub/Vorteilssystem
- [ ] Branch erstellen: `feature/module-treueclub-vorteilssystem`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

### 3.7 Mobilitäts-Module (3 Module)

#### 3.7.1 Karten (Standortnutzung)
- [ ] Branch erstellen: `feature/module-karten-standortnutzung`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.7.2 Car-/Bikesharing-Angebote
- [ ] Branch erstellen: `feature/module-car-bikesharing-angebote`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.7.3 Smartes Trampen
- [ ] Branch erstellen: `feature/module-smartes-trampen`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

### 3.8 Community-Module (2 Module)

#### 3.8.1 Gruppen/Soziales Netzwerk
- [ ] Branch erstellen: `feature/module-gruppen-soziales-netzwerk`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.8.2 Persönliches Profil (Bund.ID)
- [ ] Branch erstellen: `feature/module-persoenliches-profil-bund-id`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

### 3.9 Spezial-Module (5 Module)

#### 3.9.1 Augmented-Reality
- [ ] Branch erstellen: `feature/module-augmented-reality`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.9.2 Chatbot
- [ ] Branch erstellen: `feature/module-chatbot`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.9.3 Nutzertracking
- [ ] Branch erstellen: `feature/module-nutzertracking`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.9.4 Webview
- [ ] Branch erstellen: `feature/module-webview`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

#### 3.9.5 Widgets
- [ ] Branch erstellen: `feature/module-widgets`
- [ ] STUB befüllen
- [ ] Human Review & Korrekturen
- [ ] Commit & PR nach Freigabe
- [ ] PR mergen & Schema-Validierung

## 4. Qualitätssicherung

### 4.1 Validierung aller Module
- [ ] Script ausführen: `python validate_schemas.py --all`
- [ ] Alle Fehler beheben
- [ ] Sicherstellen: 60+ Module validieren erfolgreich

### 4.2 Konsistenz-Prüfung
- [ ] Alle Module haben korrekte `topic`-Werte (aus Schema-Enum)
- [ ] Alle Module haben `technical_documentation` URLs
- [ ] Screenshots-URLs sind konsistent
- [ ] `last_update` Datumsformat korrekt (YYYY-MM-DD)

### 4.3 Dokumentation vervollständigen
- [ ] README aktualisieren mit vollständiger Modulliste
- [ ] FAQ für häufige Fragen hinzufügen
- [ ] Beispiele für verschiedene Modultypen dokumentieren

## 5. CI/CD Integration

### 5.1 Pre-commit Hooks
- [ ] Hook für automatische YAML-Validierung
- [ ] Warnung bei direkter Bearbeitung generierter Dateien
- [ ] Hook für YAML-Linting

### 5.2 GitHub Actions / CI Pipeline
- [ ] Workflow für automatische Validierung bei PRs
- [ ] Badge für Schema-Validierung im README
- [ ] Automatische Generierung bei Änderungen in yml/modules/

## 6. Nacharbeiten

### 6.1 Optionale Verbesserungen
- [ ] Screenshots von Mock-URLs auf echte URLs umstellen
- [ ] Deprecated-Module kennzeichnen
- [ ] Mehrsprachigkeit vorbereiten (EN-Versionen)

### 6.2 Monitoring
- [ ] Nutzung der Tools überwachen
- [ ] Feedback von Redakteuren einholen
- [ ] Kontinuierliche Verbesserungen

## Progress Tracking

**Phase 1 (Setup):** 9/9 abgeschlossen ✅ 100%
**Phase 2 (PoC + Workflow):** 7/7 abgeschlossen ✅ 100%
**Phase 3 (Bulk-Erstellung):** 5/230 Tasks (1/46 Module) ✅ 2.2%
**Phase 4 (QA):** 0/3 abgeschlossen
**Phase 5 (CI/CD):** 0/2 abgeschlossen
**Phase 6 (Nacharbeiten):** 0/2 abgeschlossen

**Gesamt:** 21/269 Tasks abgeschlossen (7.8%)

**Status:** 🚀 Phase 1 & 2 erfolgreich! App-Intro als erstes Modul in Phase 3 abgeschlossen!
**Aktuelle Module:** 7 vollständig validiert (city_app, abfallkalender, app-intro, karten, maengelmelder, nachrichten, veranstaltungen)
**STUBs erstellt:** 45 Module warten auf Befüllung (1 von 46 abgeschlossen)
**Nächster Schritt:** 3.1.2 Einstellungen (Branch erstellen)
