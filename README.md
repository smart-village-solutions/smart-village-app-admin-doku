# smart-village-app-admin-doku
Dokumentation für App-Admins

## Modul-Beschreibungen erstellen

Diese Repository enthält strukturierte Beschreibungen aller Smart Village App Module.

### Schnellstart

**Neues Modul interaktiv erstellen:**

```bash
python3 scripts/create_module.py
```

Das Script führt durch alle notwendigen Schritte:
- Sammelt Modul-Informationen
- Erstellt Git-Branch
- Generiert YAML-Dateien
- Registriert in `city_app.yml`
- Erstellt Pull Request (falls GitHub CLI verfügbar)

**YAML manuell generieren:**

```bash
# Einzelnes Modul
python3 scripts/generate_module_yaml.py --module [name]

# Alle Module
python3 scripts/generate_module_yaml.py --all

# Ohne city_app.yml Registrierung
python3 scripts/generate_module_yaml.py --module [name] --no-register
```

**Validierung:**

```bash
# Standard-Module validieren
python3 validate_schemas.py

# Alle Module validieren
python3 validate_schemas.py --all
```

### Voraussetzungen

**Python 3.x mit Paketen:**
```bash
pip3 install pyyaml jsonschema
```

**GitHub CLI (für automatische PRs):**

✅ Bereits installiert: `gh version 2.83.0`

```bash
# Authentifizierung erforderlich
gh auth login

# Status prüfen
gh auth status
```

Falls noch nicht installiert:
```bash
# macOS
brew install gh

# Linux
sudo apt install gh
# oder
sudo dnf install gh
```

### Verzeichnisstruktur

```
yml/
├── global.yml                    # Gemeinsame Daten für alle Module
├── modules/                      # Modul-spezifische Partials
│   ├── abfallkalender.yml
│   ├── nachrichten.yml
│   └── ...
├── abfallkalender.yml            # Generierte vollständige YAMLs
├── nachrichten.yml
└── ...

scripts/
├── create_module.py              # Interaktives Erstellungs-Tool
└── generate_module_yaml.py       # YAML-Generator

schema/
├── app-module.schema.json        # JSON Schema für Module
└── city-app-schema.json          # JSON Schema für city_app.yml
```

### Workflow

1. **Module erstellen:**
   ```bash
   python3 scripts/create_module.py
   ```

2. **Review und Test:**
   - Branch wird automatisch erstellt: `feature/module-[name]`
   - 3 Commits werden erzeugt (partial, generated YAML, registration)
   - Prüfe generierte Dateien

3. **Pull Request:**
   - Automatisch per GitHub CLI (falls installiert)
   - Oder manuell über GitHub UI

4. **Merge:**
   - Nach Review PR mergen
   - CI validiert automatisch alle Schemas

### Template-System

Module bestehen aus zwei Teilen:

**1. Global (`yml/global.yml`):**
- Gemeinsame Daten (DRY-Prinzip)
- Deployment-Liste (42 Kommunen)
- Standard-Werte

**2. Modul-spezifisch (`yml/modules/[name].yml`):**
- Nur individuelle Felder
- Überschreibt global bei Bedarf

**Merge-Priorität:**
```
Modul-spezifisch > Global > Schema-Defaults
```

Siehe `openspec/changes/add-module-descriptions-system/OVERRIDE_CONCEPT.md` für Details.

### Dokumentation

Vollständige Dokumentation:
- **OpenSpec Proposal:** `openspec/changes/add-module-descriptions-system/`
- **Design Decisions:** `openspec/changes/add-module-descriptions-system/design.md`
- **Implementation Tasks:** `openspec/changes/add-module-descriptions-system/tasks.md`
- **Override Konzept:** `openspec/changes/add-module-descriptions-system/OVERRIDE_CONCEPT.md`
