# Kartendarstellung

## Übersicht

Das Kartenmodul der Smart Village App ermöglicht die Darstellung von Points of Interest (POIs), Veranstaltungen und anderen Inhalten auf einer interaktiven Karte.

## Technologie

Die App nutzt **MapLibre React Native** für moderne, vektorbasierte Kartendarstellung mit einem eigenen Tile-Server.

Die App wurde von `react-native-maps` auf `maplibre-react-native` migriert. Für technische Details zur Migration siehe die [MapLibre-Migrationsdokumentation](../dev/migration-maplibre.md).

## Tile-Server

Die Karten werden von einem eigenen Tile-Server bereitgestellt:
```
https://tileserver-gl.smart-village.app/styles/osm-liberty/style.json
```

Weitere Informationen zur Tile-Server-Infrastruktur finden sich unter [`docs/system/maptiles.md`](../system/maptiles.md).

## Features

- **Vektorbasierte Karten**: Scharfe Darstellung in allen Zoomstufen
- **Clustering**: Automatische Gruppierung vieler Marker
- **Custom Icons**: Kundenspezifische Marker-Symbole
- **Remote-Konfiguration**: Zentrale Steuerung von Karteneinstellungen
- **Offline-Caching**: Gecachte Tiles für bessere Performance

## Warum der Wechsel zu MapLibre?

Die Smart Village App hat im Jahr 2025 eine wichtige technologische Verbesserung im Kartenbereich vollzogen:

### Vorher: react-native-maps
- Rasterbasierte Kartendarstellung
- Unscharfe Darstellung bei hohem Zoom
- Externe Dienste oder komplexe Workarounds für eigene Karten
- Performance-Probleme bei vielen Markern

### Nachher: MapLibre
- **Vektorbasierte Karten**: Immer scharfe Darstellung, auch bei starkem Zoom
- **Eigener Tile-Server**: Vollständige Datensouveränität, keine externen API-Kosten
- **Bessere Performance**: Flüssiges Zoomen und Schwenken, natives Clustering
- **Mehr Flexibilität**: Eigene Kartendesigns und Layer möglich
- **Zukunftssicher**: Open-Source-Standard für moderne Kartenanwendungen

### Was bedeutet das für Sie?

**Für Nutzer/innen:**
- Schärfere, hochwertigere Kartendarstellung
- Schnellere und flüssigere Bedienung
- Zuverlässigere Funktion auch bei vielen gleichzeitigen Kartenmarkern

**Für Kund/innen:**
- Keine Kosten für externe Kartendienste
- Volle Kontrolle über Kartendarstellung und -daten
- Grundlage für zukünftige Features (z.B. 3D-Ansichten, Offline-Karten)
- Datensouveränität durch eigene Infrastruktur

## Konfiguration

Die Kartendarstellung kann zentral über das Backend konfiguriert werden:

- **Marker-Icons**: Eigene Symbole für verschiedene Inhaltstypen
- **Clustering**: Automatische Gruppierung ab einer bestimmten Anzahl von Markern
- **Farben**: Anpassbare Cluster-Farben je nach Inhaltstyp
- **Zoom-Level**: Standard-Zoom beim Öffnen der Karte
- **Kartenstil**: Anpassungen am Basis-Kartenstil möglich

Diese Einstellungen können zum Großteil ohne App-Update geändert werden.

## Für Entwickler/innen

Technische Dokumentation zur Kartenimplementierung:
- [MapLibre Migration Guide](../dev/migration-maplibre.md) - Umstieg von react-native-maps
- [API-Dokumentation](../dev/api.md) - GraphQL-Endpunkte für Kartendaten
- [System-Architektur](../system/maptiles.md) - Tile-Server-Setup
