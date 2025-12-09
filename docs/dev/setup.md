# Lokale Entwicklung

## Voraussetzungen

- Node.js 18.19.1 (empfohlen: 20.19.4)
- Expo SDK 52.0.47 (empfohlen: 54.0.0)
- React Native 0.76.9 (empfohlen: 0.81.4)

## Installation

```bash
# Dependencies installieren
npm install

# oder
yarn install
```

## Development Builds

Da die App native Module verwendet (insbesondere MapLibre), funktioniert sie nicht in Expo Go. Development Builds sind erforderlich.

```bash
# Prebuild (native Ordner generieren)
npx expo prebuild --clean

# Development Builds erstellen
eas build --profile development --platform ios
eas build --profile development --platform android
```

## Kartenentwicklung

Die App nutzt MapLibre für Kartendarstellung. Weitere Details:
- [MapLibre Migration Guide](migration-maplibre.md) - Technische Details zur Kartenimplementierung
- [MapLibre React Native Repo](https://github.com/maplibre/maplibre-react-native)

## Dokumentation lokal bauen

```bash
# MkDocs installieren
pip install mkdocs

# Dokumentation lokal starten
mkdocs serve

# Dokumentation bauen
mkdocs build
```
