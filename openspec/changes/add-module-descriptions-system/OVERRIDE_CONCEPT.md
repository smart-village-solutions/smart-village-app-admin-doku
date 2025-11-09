# Override-Konzept: Globale vs. Modul-spezifische Werte

## Grundprinzip

Das Template-System verwendet eine **3-stufige Priorität** beim Zusammenführen von Daten:

1. **Modul-spezifische Werte** (höchste Priorität)
2. **Globale Werte** aus `global.yml`
3. **Schema-Defaults** (niedrigste Priorität)

## Wie funktioniert es?

### Merge-Logik

```python
# Pseudocode
generated_yaml = {}

# Schritt 1: Globale Werte laden (Basis)
generated_yaml.update(global_yml['common'])

# Schritt 2: Modul-spezifische Werte überschreiben
generated_yaml.update(module_yml)

# Ergebnis: Modul-Werte haben Vorrang
```

## Praktische Beispiele

### Beispiel 1: Standard-Module (nutzen globale Werte)

**Situation:** Die meisten Module sind in allen 42 Kommunen verfügbar.

```yaml
# global.yml
common:
  opencode_repository: "https://gitlab.opencode.de/bad-belzig/smart-village-app-app"
  development_status: "Production"
  deployed_in_municipalities:
    - "Angermünde"
    - "Augsburg"
    - "Bad Belzig"
    # ... 39 weitere Kommunen
```

```yaml
# yml/modules/abfallkalender.yml
name: "Abfallkalender"
topic: "abfallkalender"
short_description: "Übersicht über Müllabfuhr-Termine"
# KEIN deployed_in_municipalities definiert
# KEIN development_status definiert
```

**Ergebnis in `yml/abfallkalender.yml`:**
```yaml
name: "Abfallkalender"
topic: "abfallkalender"
short_description: "Übersicht über Müllabfuhr-Termine"
opencode_repository: "https://gitlab.opencode.de/bad-belzig/smart-village-app-app"  # ← von global.yml
development_status: "Production"  # ← von global.yml
deployed_in_municipalities:  # ← von global.yml
  - "Angermünde"
  - "Augsburg"
  - "Bad Belzig"
  # ... alle 42 Kommunen
```

### Beispiel 2: Beta-Module (überschreiben development_status)

**Situation:** Chatbot ist noch in Beta-Phase.

```yaml
# yml/modules/chatbot.yml
name: "Chatbot"
topic: "chatbot"
short_description: "KI-gestützter Assistent"
development_status: "Beta"  # ← Überschreibt "Production"
```

**Ergebnis in `yml/chatbot.yml`:**
```yaml
name: "Chatbot"
topic: "chatbot"
short_description: "KI-gestützter Assistent"
development_status: "Beta"  # ← Modul-Wert hat Vorrang!
deployed_in_municipalities:  # ← von global.yml
  - "Angermünde"
  - "Augsburg"
  # ... alle 42 Kommunen
```

### Beispiel 3: Pilot-Module (überschreiben Kommune-Liste)

**Situation:** Augmented Reality wird nur in 2 Kommunen getestet.

```yaml
# yml/modules/augmented-reality.yml
name: "Augmented Reality"
topic: "augmented-reality"
short_description: "AR-Stadtführung"
development_status: "Beta"
deployed_in_municipalities:  # ← Überschreibt globale Liste
  - "Bad Belzig"
  - "Kiel"
```

**Ergebnis in `yml/augmented-reality.yml`:**
```yaml
name: "Augmented Reality"
topic: "augmented-reality"
short_description: "AR-Stadtführung"
development_status: "Beta"  # ← Modul-Wert
deployed_in_municipalities:  # ← Modul-Wert hat Vorrang!
  - "Bad Belzig"
  - "Kiel"
# Nur 2 statt 42 Kommunen!
```

### Beispiel 4: Externe Module (überschreiben Repository)

**Situation:** HumHub hat ein separates Repository.

```yaml
# yml/modules/humhub.yml
name: "HumHub"
topic: "sozialdienste"
short_description: "Soziales Netzwerk"
opencode_repository: "https://github.com/humhub/humhub"  # ← Überschreibt Standard-Repo
```

**Ergebnis in `yml/humhub.yml`:**
```yaml
name: "HumHub"
topic: "sozialdienste"
short_description: "Soziales Netzwerk"
opencode_repository: "https://github.com/humhub/humhub"  # ← Modul-Wert!
deployed_in_municipalities:  # ← von global.yml
  - "Angermünde"
  - "Augsburg"
  # ... alle 42 Kommunen
```

## Best Practices

### Wann globale Werte nutzen?

✅ **Nutze globale Werte wenn:**
- Das Modul in allen oder den meisten Kommunen verfügbar ist
- Der Wert für alle Module identisch ist
- Du Änderungen zentral verwalten möchtest

### Wann modul-spezifische Werte definieren?

✅ **Überschreibe mit modul-spezifischen Werten wenn:**
- Das Modul nur in wenigen Kommunen verfügbar ist
- Der development_status vom Standard abweicht (z.B. Beta, Alpha)
- Das Modul ein eigenes Repository hat
- Das Modul andere `external_services` nutzt
- Screenshots oder Dokumentation modulspezifisch sind

## Häufige Anwendungsfälle

### Fall 1: Neues Modul in allen Kommunen

```yaml
# yml/modules/neue-funktion.yml
name: "Neue Funktion"
topic: "bürgerservices"
short_description: "..."
# Nichts weiter definieren → nutzt alle globalen Werte
```

### Fall 2: Experimentelles Modul in einer Kommune

```yaml
# yml/modules/experiment.yml
name: "Experiment"
topic: "innovation"
short_description: "..."
development_status: "Alpha"
deployed_in_municipalities:
  - "Bad Belzig"  # Nur Test-Kommune
```

### Fall 3: Modul mit eigenem Entwicklungszyklus

```yaml
# yml/modules/spezial-modul.yml
name: "Spezial-Modul"
topic: "..."
short_description: "..."
development_status: "Beta"
last_update: "2025-11-10"  # Eigenes Update-Datum
opencode_repository: "https://github.com/andere/repo"
```

## Technische Implementierung

Der Generator (`generate_module_yaml.py`) wird folgende Logik verwenden:

```python
def merge_yaml_data(global_data, module_data):
    """
    Merge global and module-specific YAML data.
    Module values override global values.
    """
    result = {}

    # 1. Start with global common values
    if 'common' in global_data:
        result.update(global_data['common'])

    # 2. Override with module-specific values
    result.update(module_data)

    # 3. Remove any processing metadata
    result.pop('common', None)

    return result
```

## Wartung und Updates

### Globale Änderungen (z.B. neue Kommune)

```bash
# 1. global.yml bearbeiten
vim yml/global.yml

# 2. Alle Module regenerieren
python scripts/generate_module_yaml.py --all

# 3. Nur Module OHNE eigene deployed_in_municipalities werden aktualisiert
```

### Modul-spezifische Änderungen

```bash
# 1. Modul-Datei bearbeiten
vim yml/modules/chatbot.yml

# 2. Einzelnes Modul regenerieren
python scripts/generate_module_yaml.py --module chatbot

# 3. Nur dieses Modul wird aktualisiert
```

## Zusammenfassung

| Feld | Global definieren? | Modul überschreiben? | Beispiel |
|------|-------------------|---------------------|----------|
| `opencode_repository` | ✅ Ja (Standard-Repo) | 🔄 Bei Bedarf | HumHub hat eigenes Repo |
| `deployed_in_municipalities` | ✅ Ja (alle Kommunen) | 🔄 Häufig | Pilot-Module nur in 1-2 Kommunen |
| `development_status` | ✅ Ja ("Production") | 🔄 Bei Beta/Alpha | Beta-Module überschreiben |
| `last_update` | 🔄 Optional | ✅ Ja, pro Modul | Jedes Modul hat eigenes Datum |
| `name` | ❌ Nein | ✅ Ja, immer | Jedes Modul einzigartig |
| `topic` | ❌ Nein | ✅ Ja, immer | Jedes Modul einzigartig |
| `description` | ❌ Nein | ✅ Ja, immer | Jedes Modul einzigartig |

**Faustregel:** Wenn ein Feld für >80% der Module gleich ist → global definieren. Einzelne Module können es dann bei Bedarf überschreiben.
