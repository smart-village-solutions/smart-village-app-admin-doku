# Module Description Workflow - Specification Delta

## ADDED Requirements

### Requirement: Interaktive Modulerstellung

The system SHALL provide a CLI tool (`create_module.py`) that guides users through the module creation process.

#### Scenario: Neues Modul erstellen

- **WHEN** ein Redakteur `python scripts/create_module.py --interactive` ausführt
- **THEN** werden folgende Informationen abgefragt:
  - Modulname (Pflicht)
  - Topic aus Schema-Enum (Pflicht)
  - Kurzbeschreibung (Pflicht)
  - Nutzungsszenario (Pflicht)
  - Detaillierte Beschreibung (Pflicht)
  - Optionale Felder (Roadmap, Interfaces, Dependencies, etc.)
- **AND** die Eingaben werden in `yml/modules/[modulname].yml` gespeichert
- **AND** automatisch eine vollständige YAML-Datei in `yml/[modulname].yml` generiert
- **AND** die generierte Datei gegen `app-module.schema.json` validiert

#### Scenario: Modulerstellung mit Validierungsfehler

- **WHEN** die generierte YAML-Datei nicht dem Schema entspricht
- **THEN** wird eine detaillierte Fehlermeldung angezeigt
- **AND** der Nutzer kann die Eingaben korrigieren
- **AND** die Generierung wird wiederholt

### Requirement: Automatische YAML-Generierung

The system SHALL provide a generator script (`generate_module_yaml.py`) that creates complete YAML files from partial information.

#### Scenario: YAML-Generierung aus Teilinformationen

- **WHEN** `python scripts/generate_module_yaml.py --module abfallkalender` ausgeführt wird
- **THEN** werden Daten aus `yml/global.yml` geladen
- **AND** werden Daten aus `yml/modules/abfallkalender.yml` geladen
- **AND** beide Datenquellen werden zusammengeführt
- **AND** die Ausgabe wird in `yml/abfallkalender.yml` geschrieben
- **AND** ein Kommentar `# AUTO-GENERATED FROM yml/modules/abfallkalender.yml + yml/global.yml` wird hinzugefügt

#### Scenario: Batch-Generierung aller Module

- **WHEN** `python scripts/generate_module_yaml.py --all` ausgeführt wird
- **THEN** werden alle Dateien in `yml/modules/` verarbeitet
- **AND** für jede Datei wird eine vollständige YAML-Datei generiert
- **AND** ein Fortschrittsbericht wird angezeigt

### Requirement: Schema-Validierung

The system SHALL automatically validate generated YAML files against the schema.

#### Scenario: Erfolgreiche Validierung

- **WHEN** eine YAML-Datei generiert wird
- **THEN** wird sie gegen `app-module.schema.json` validiert
- **AND** bei Erfolg wird eine Erfolgsmeldung angezeigt (grün)
- **AND** die Datei wird gespeichert

#### Scenario: Fehlgeschlagene Validierung

- **WHEN** eine YAML-Datei nicht dem Schema entspricht
- **THEN** wird eine detaillierte Fehlermeldung mit Pfad und Wert angezeigt (rot)
- **AND** die Datei wird NICHT gespeichert
- **AND** Exit Code 1 wird zurückgegeben

### Requirement: Bulk-Validierung

The system SHALL provide a way to validate all modules at once.

#### Scenario: Validierung aller Module

- **WHEN** `python validate_schemas.py --all` ausgeführt wird
- **THEN** werden alle `*.yml` Dateien in `yml/` (außer `yml/modules/`) validiert
- **AND** für jedes Modul wird der Status angezeigt
- **AND** eine Zusammenfassung zeigt erfolgreiche und fehlgeschlagene Validierungen
- **AND** Exit Code 0 bei Erfolg, 1 bei Fehlern

### Requirement: Dokumentation

The system SHALL provide comprehensive documentation for the module creation process.

#### Scenario: README-Dokumentation

- **GIVEN** ein Redakteur möchte ein neues Modul erstellen
- **WHEN** die README-Datei geöffnet wird
- **THEN** findet der Nutzer:
  - Schritt-für-Schritt-Anleitung für Modulerstellung
  - Erklärung des Template-Systems
  - Beispiele für verschiedene Modultypen
  - Troubleshooting-Hinweise
  - Links zu Schema-Dokumentation

#### Scenario: Inline-Hilfe im CLI-Tool

- **WHEN** `python scripts/create_module.py --help` ausgeführt wird
- **THEN** wird eine Übersicht aller Optionen angezeigt
- **AND** Beispiele für die Nutzung werden gezeigt

### Requirement: Automatische Registrierung in city_app.yml

The system SHALL automatically register generated modules in `city_app.yml`.

#### Scenario: Modul wird in city_app.yml registriert

- **WHEN** ein Modul mit `generate_module_yaml.py` generiert wird
- **THEN** prüft das System, ob die Modul-URL bereits im `modules:` Array von `city_app.yml` existiert
- **AND** falls nicht vorhanden, wird die GitHub-Raw-URL hinzugefügt
- **AND** Format: `https://raw.githubusercontent.com/smart-village-solutions/smart-village-app-admin-doku/main/yml/[modulname].yml`
- **AND** die YAML-Struktur und Kommentare in `city_app.yml` bleiben erhalten

#### Scenario: Duplikat-Registrierung wird verhindert

- **GIVEN** ein Modul ist bereits in `city_app.yml` registriert
- **WHEN** das Modul erneut generiert wird
- **THEN** wird keine doppelte URL hinzugefügt
- **AND** eine Meldung informiert über die bestehende Registrierung

### Requirement: Git-Workflow mit Branch und Pull Request

The system SHALL create a Git branch and pull request for each new module.

#### Scenario: Automatische Branch-Erstellung

- **WHEN** `python scripts/create_module.py --interactive` ausgeführt wird
- **THEN** wird automatisch ein neuer Branch erstellt
- **AND** Branch-Name: `feature/module-[modulname]` (kebab-case)
- **AND** der Branch zweigt vom aktuellen `main` ab
- **AND** der Branch wird automatisch ausgecheckt

#### Scenario: Automatische Commits

- **WHEN** ein Modul erfolgreich erstellt wurde
- **THEN** werden automatisch 3 Commits erstellt:
  1. `feat: add module definition for [name]` (yml/modules/[name].yml)
  2. `feat: generate YAML for [name] module` (yml/[name].yml)
  3. `feat: register [name] module in city_app.yml` (city_app.yml)
- **AND** alle Commits folgen Conventional Commits Standard

#### Scenario: Automatische PR-Erstellung

- **WHEN** alle Commits erstellt wurden
- **THEN** wird automatisch ein Pull Request über GitHub CLI erstellt
- **AND** PR-Titel: `feat: Add [Modulname] module`
- **AND** PR-Body enthält:
  - Modulname und Topic
  - Kurzbeschreibung
  - Link zur generierten YAML-Datei
  - Checkliste für Review
- **AND** Labels: `module`, `documentation`
- **AND** optionale Reviewer werden zugewiesen (konfigurierbar)

#### Scenario: Fallback bei fehlendem GitHub CLI

- **GIVEN** GitHub CLI (`gh`) ist nicht installiert
- **WHEN** PR-Erstellung versucht wird
- **THEN** wird eine Fehlermeldung angezeigt
- **AND** eine GitHub-URL zum manuellen PR-Erstellen wird bereitgestellt
- **AND** die Commits sind bereits vorhanden im Branch

#### Scenario: PR-Template wird genutzt

- **WHEN** ein Pull Request erstellt wird
- **THEN** wird das PR-Template aus `.github/PULL_REQUEST_TEMPLATE.md` genutzt
- **AND** automatisch generierte Informationen werden eingefügt
- **AND** Checkliste enthält:
  - Modul validiert gegen Schema
  - In city_app.yml registriert
  - Screenshots vorhanden (optional)
  - Dokumentation vollständig
  - Technical documentation URL funktioniert
