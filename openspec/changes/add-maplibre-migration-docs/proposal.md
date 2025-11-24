# Change: MapLibre-Migrationsdokumentation hinzufügen

## Why

Die Smart Village App hat einen wichtigen technologischen Wechsel vollzogen: von `react-native-maps` zu `maplibre-react-native`. Diese Migration betrifft ein Kernmodul der App (Kartendarstellung) und bringt erhebliche technische und architektonische Änderungen mit sich.

Aktuell existiert diese kritische Information nur in informeller Form. Für zukünftige Entwickler*innen, Wartung und Kund*innen fehlt eine strukturierte Dokumentation über:
- Gründe für den Wechsel
- Technische Herausforderungen und Lösungen
- API-Änderungen und Breaking Changes
- Migrationsstrategie und Best Practices
- Neue Architektur (GeoJSON, Layer-System, eigener Tile-Server)

## What Changes

- **NEU**: Umfassende Migrationsdokumentation unter `docs/dev/migration-maplibre.md`
- **NEU**: OpenSpec-Capability für "Developer Documentation" etablieren
- **ERWEITERT**: Entwickler-Dokumentation um kritisches Migrationswissen

Die Dokumentation umfasst:
1. Problemanalyse und Entscheidungsgrundlagen
2. Technische Architektur (GeoJSON, Layer-System, Tile-Server)
3. API-Migrationsguide mit Code-Beispielen
4. Konfiguration und Remote-Settings
5. Testing und bekannte Einschränkungen
6. Parallelbetrieb-Strategie
7. Build-Anforderungen und Dependencies

## Impact

### Affected specs
- **NEU**: `developer-documentation` (neue Capability)

### Affected code
- **NEU**: `docs/dev/migration-maplibre.md` (neue Datei)
- Keine Code-Änderungen - reine Dokumentation

### Benefits
- Wissenstransfer für neue Entwickler/innen
- Nachvollziehbare Architekturentscheidungen
- Reduzierung von Support-Anfragen
- Beschleunigung zukünftiger Kartenerweiterungen
- Basis für weitere Migrationen ähnlicher Art

### Stakeholders
- Entwickler/innen (primär)
- Technische Projektleitung
- Kund/innen (sekundär, für Verständnis der Verbesserungen)
