---
name: Module Description
about: Add or update a module description
title: 'feat(module): Add [MODULE_NAME] module description'
labels: module, documentation
assignees: ''

---

## Modul

**Name:** [Modulname]
**Topic:** [z.B. veranstaltungskalender, maengelmelder]

## Beschreibung

[Kurze Beschreibung was dieses Modul macht]

## Änderungen

- [ ] Modul-Partial erstellt (`yml/modules/[name].yml`)
- [ ] Vollständige YAML generiert (`yml/[name].yml`)
- [ ] In `city_app.yml` registriert
- [ ] Schema-Validierung erfolgreich

## Testing

```bash
# Validierung durchführen
python3 validate_schemas.py --all

# Einzelnes Modul validieren
python3 -c "import yaml, json, jsonschema; \
  data = yaml.safe_load(open('yml/[name].yml')); \
  schema = json.load(open('schema/app-module.schema.json')); \
  jsonschema.validate(data, schema); \
  print('✓ Schema valid')"
```

## Checklist

- [ ] Alle erforderlichen Felder ausgefüllt
- [ ] Beschreibungen sind verständlich und vollständig
- [ ] Screenshots hinzugefügt (falls verfügbar)
- [ ] Links und URLs geprüft
- [ ] Rechtschreibung geprüft
- [ ] Barrierefreiheit beachtet (Alt-Texte für Bilder, etc.)

## Zusätzliche Informationen

[Weitere Hinweise, Kontext oder Links]

---

**Generiert mit:** `scripts/create_module.py`
**Schema:** `schema/app-module.schema.json`
