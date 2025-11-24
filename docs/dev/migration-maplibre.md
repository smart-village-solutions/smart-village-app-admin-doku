# Migration von `react-native-maps` zu `maplibre-react-native`

**Status:** In Umsetzung (Phase 1 abgeschlossen)
**Letzte Aktualisierung:** 09. Dezember 2025
**Branch:** `epic/map`
**Fortschritt:** ~92% (Kern-Implementierung fertig, schrittweiser Rollout läuft)

## Inhaltsverzeichnis

1. [Überblick](#überblick)
2. [Warum wir überhaupt wechseln mussten](#1-warum-wir-überhaupt-wechseln-mussten)
3. [Vorteile von MapLibre](#2-vorteile-von-maplibre-react-native)
4. [Herausforderungen der Migration](#3-herausforderungen-der-migration)
5. [Rückblick: Entscheidungsprozess](#4-rückblick-entscheidungsprozess)
6. [Technische Infrastruktur](#5-technische-infrastruktur)
7. [API-Migration Guide](#6-api-migration-guide-für-entwicklerinnen)
8. [Konfiguration und Anpassung](#7-konfiguration-und-anpassung)
9. [Migrationsstrategie](#8-migrationsstrategie-parallelbetrieb)
10. [Voraussetzungen und Dependencies](#9-voraussetzungen-und-dependencies)
11. [Testing und Qualitätssicherung](#10-testing-und-qualitätssicherung)
12. [Offene Aufgaben](#11-offene-aufgaben--nächste-schritte)
13. [Zielsetzung](#12-zielsetzung-des-umstiegs)
14. [Fazit](#13-fazit)
15. [Ressourcen und Links](#14-ressourcen-und-links)

## Überblick

Dieses Dokument beschreibt die Hintergründe, Herausforderungen und Vorteile des Wechsels von `react-native-maps` auf `maplibre-react-native` innerhalb der Smart Village App. Es richtet sich sowohl an zukünftige Entwickler/innen des Projekts als auch an Kund/innen, die ein Verständnis für die Gründe und Abläufe dieses Migrationsprozesses gewinnen möchten.

### Wichtigste Unterschiede auf einen Blick

| Aspekt | Vorher | Nachher |
|--------|--------|---------|
| **Bibliothek** | react-native-maps | maplibre-react-native |
| **Karten-Typ** | Raster-Kacheln | Vektor-Kacheln |
| **Tile-Server** | erst externe Dienste, dann eigener Server | eigener Server |
| **Marker-System** | React-Komponenten | GeoJSON + Layer |
| **Clustering** | separate Implementierung | native Unterstützung |
| **Performance** | mittel | hoch |

### Versions-Kompatibilität

| Komponente | Minimum | Empfohlen |
|------------|---------|-----------|
| **Expo SDK** | 52.0.47 | 54.0.27 |
| **React Native** | 0.76.9 | 0.81.5 |
| **@maplibre/maplibre-react-native** | 10.4.0 | 11.0.0-alpha.15 |
| **@turf/helpers** | 7.1.0 | 7.2.0 |
| **Node.js** | 18.19.1 | 20.19.4 |

---

## 1. Warum wir überhaupt wechseln mussten

### 1.1 Einschränkungen von `react-native-maps`

`react-native-maps` (https://github.com/react-native-maps/react-native-maps) ist ein weit verbreitetes Paket, aber wir sind damit an technische Grenzen gestoßen, wenn es um moderne Kartendarstellungen geht. Die wichtigsten Probleme waren:

* **Unscharfe Karten bei hohen Zoomstufen**: Rasterkacheln verlieren bei hohem Zoom-Level stark an Schärfe. Besonders bei hohen Zoomstufen waren die Karten unscharf und pixelig, was die Orientierung erschwerte.
* **Abgeschnittene Inhalte**: Marker und Kartenbereiche wurden teilweise nicht vollständig dargestellt. Dieses Problem trat wiederholt auf und beeinträchtigte die Nutzererfahrung erheblich.
* **Kachel-Sprünge bei verschiedenen Zoomstufen**: Durch die Verwendung von Rasterbildern kam es zu sichtbaren Übergängen zwischen Kacheln, insbesondere beim Rein- und Rauszoomen.
* **Performance-Probleme**: Schnelles Zoomen oder Schwenken führte zu Rucklern, verzögerten Reaktionen und einer insgesamt stockenden Bedienung, welche die Nutzererfahrung beeinträchtigten.
* **Plattform-spezifische Probleme (vor allem auf Android)**: Die oben genannten Probleme traten verstärkt auf Android-Geräten auf, was zu inkonsistenten Erfahrungen zwischen iOS und Android führte. Zusätzlich erfordert `react-native-maps` auf Android einen Google API-Key und kommuniziert unnötigerweise mit Google-Diensten – selbst wenn wir keine Google Maps verwenden. Dies widerspricht unserem Anspruch auf Datensouveränität und Open-Source-Unabhängigkeit.
* **Keine Unterstützung für Vektorkarten**: Wir möchten moderne Vektordaten für unsere Open-Source-Karten nutzen. `react-native-maps` unterstützt jedoch nur Raster-Kacheln. Dadurch konnten wir die Karten nicht in ihrer optimalen Form nutzen.

### 1.2 Anforderungen, die unerfüllt blieben

Unsere Anforderungen an das Kartenmaterial entwickelten sich weiter:

* Nutzung eigener Open-Source-Vektorkarten
* Moderne, flüssige Interaktion mit der Karte
* Einheitliche Darstellung ohne grafische Artefakte
* Zukunftssichere Technologie mit aktiver Community

Diese Punkte konnten wir mit dem alten Paket nicht ausreichend erfüllen.

---

## 2. Vorteile von `maplibre-react-native`

Mit dem Wechsel zu `maplibre-react-native` (https://github.com/maplibre/maplibre-react-native) ergeben sich folgende Verbesserungen:

* **Vektorbasiertes Rendering**: Darstellung bleibt in allen Zoomstufen scharf und sauber.
* **Bessere Performance**: Flüssiges Zoomen, Drehen und Bewegen der Karte.
* **Open-Source & aktiv entwickelt**: MapLibre ist vollständig Open Source und wird stark von der Community unterstützt.
* **Starke Flexibilität**: Eigene Kartendesigns, Layer-Logik und Darstellungsmöglichkeiten.
* **Bessere Zukunftssicherheit**: Da Vektorkarten Standard in modernen App-Karten sind, bauen wir auf eine stabile Grundlage.
* **Native Layer-System**: Professionelle Kartenarchitektur mit Source/Layer-Konzept für optimale Performance.
* **Mapbox Expression Syntax**: Mächtige Style-Engine für dynamische Kartenelemente.

---

## 3. Herausforderungen der Migration

Obwohl die Vorteile überwiegen, bringt `maplibre-react-native` auch eigene Herausforderungen mit sich:

### 3.1 Technische Integration

* **Komplexere API**: Die Funktionsvielfalt bedeutet mehr Einarbeitung.
* **Andere Denkweise in Layern und Quellen**: Vektorkarten setzen auf ein anderes Renderkonzept als Rasterkarten.
* **Paradigmenwechsel**: Statt React-Komponenten für Marker nutzen wir nun `ShapeSource` und `SymbolLayer` für bessere Performance.

### 3.2 Plattform- und Build-Themen

* **iOS- und Android-Builds** können herausfordernder sein, da MapLibre auf nativen Implementierungen basiert.
* **Expo Prebuild erforderlich**: Kein Support für Expo Go, da native Module eingebunden werden.
* **Config-Plugin-Integration**: Automatische Konfiguration über Expo Config Plugins (`app.json`).
* **Podfile-Anpassungen**: Auf iOS werden automatisch MapLibre-spezifische Post-Install-Hooks eingefügt.
* **React Native New Architecture**: v10 hat nur eingeschränkte Unterstützung über Interoperability Layer (Details siehe [Abschnitt 9.6](#96-react-native-new-architecture))

### 3.3 Anpassung bestehender Features

* **Marker-System**: Wechsel von `<Marker>` Komponenten zu GeoJSON-basierten `ShapeSource` mit `SymbolLayer`.
* **Camera-API**: Neue `Camera`-Komponente statt `animateToRegion` (https://maplibre.org/maplibre-react-native/docs/components/general/camera).
* **Interaktivität**: Event-Handling funktioniert anders (z.B. `onPress` auf `ShapeSource` statt auf einzelnen Markern).
* **Eigene Position**: Neue `UserLocation`-Komponente mit spezifischen Optionen (https://maplibre.org/maplibre-react-native/docs/components/general/user-location).

### 3.4 Clustering

Das Clustering von vielen Kartenpunkten (z. B. POIs, Veranstaltungsorten oder Einträgen aus verschiedenen Datenquellen) war bereits im alten System eine Herausforderung. Bei `react-native-maps` mussten eigene Workarounds entwickelt werden, um große Datenmengen performant zusammenzufassen. Diese Lösungen waren jedoch teilweise unzuverlässig, schwer erweiterbar und nicht optimal für unsere Bedürfnisse.

Mit dem Wechsel zu `maplibre-react-native` ergab sich eine komplett neue Herangehensweise: Das Clustering basiert nun auf den nativen Mechanismen der **MapLibre-Source- und Layer-Architektur**, insbesondere **GeoJSON-Quellen, Cluster-Eigenschaften und dynamischen Layern**.

Nach einer intensiven Einarbeitungsphase konnte das Clustering erfolgreich implementiert werden. Die neue Lösung ist:

* **stabiler**, da Clustering nativ unterstützt wird,
* **performanter**, weil MapLibre große Datenmengen effizient aggregiert,
* **optisch konsistenter**, da Cluster-Icons auf Vektorbasis sauber skalieren und nicht mehr verpixeln,
* **flexibler**, da Cluster-Styles und Farben leichter anpassbar sind,
* **multi-type-fähig**: Cluster können verschiedene Feature-Typen enthalten und werden dynamisch eingefärbt,
* **remote konfigurierbar**: Cluster-Parameter wie Radius, Max-Zoom und Farben können vom Server gesteuert werden.

Die Implementierung nutzt **Mapbox Expression Syntax** für komplexe Style-Logik:
- Dynamische Farbgebung basierend auf Feature-Typen im Cluster
- Aggregation von Feature-Eigenschaften über `clusterProperties`
- Mehrstufige Ring-Visualisierung für bessere Erkennbarkeit

---

## 4. Rückblick: Entscheidungsprozess

Da der Prozess bereits seit längerer Zeit läuft, dokumentieren wir hier retrospektiv die wichtigsten Meilensteine und Überlegungen:

1. **Problemanalyse in der bestehenden App**: Performance- und Qualitätsprobleme im Kartenbereich wurden wiederholt gemeldet.
2. **Bewertung alternativer Lösungen**:
   * Evaluierung anderer Bibliotheken
   * Abwägung Kosten/Risiken
3. **Technische Prototypen**: Erste Tests mit MapLibre bestätigten, dass es unsere Anforderungen erfüllt.
4. **Entscheidung im Team**: Beschlossen wurde ein schrittweiser Umstieg mit Parallelbetrieb.
5. **Erstellung eines Migrations-Branch**: Umsetzung im Branch `epic/map`.

---

## 5. Technische Infrastruktur

### 5.1 Eigener Tile-Server

Ein entscheidender Vorteil der neuen Lösung ist die Nutzung eines **eigenen Tile-Servers**:

```
https://tileserver-gl.smart-village.app/styles/osm-liberty/style.json
```

**Vorteile:**
* **Datensouveränität**: Vollständige Kontrolle über Kartendaten und -darstellung
* **Unabhängigkeit**: Keine externen Dienste wie Google Maps oder Mapbox erforderlich
* **OSM-Liberty Style**: Freier, anpassbarer Kartenstil basierend auf OpenStreetMap-Daten
* **Performance**: Optimiert für unsere spezifischen Anforderungen
* **Kostenkontrolle**: Keine API-Kosten für Kartenaufrufe

Weitere Informationen zum Tile-Server-Setup finden sich unter [`docs/system/maptiles.md`](../system/maptiles.md)

### 5.2 GeoJSON-basierte Architektur

Die neue Implementierung nutzt moderne **GeoJSON-Standards** mit `@turf/helpers`:

```javascript
import { featureCollection, point } from '@turf/helpers';

const features = locations.map(location =>
  point([location.position.longitude, location.position.latitude], {
    ...location
  })
);

const geoJsonData = featureCollection(features);
```

**Vorteile:**
* Standard-konform und weit verbreitet
* Bessere Kompatibilität mit Backend-Systemen
* Einfachere Integration mit GIS-Tools
* Ermöglicht komplexe geografische Operationen

### 5.3 Layer-System

MapLibre verwendet ein professionelles **Source/Layer-Konzept**:

```javascript
<ShapeSource id="pois" shape={geoJsonData} cluster={true}>
  <SymbolLayer id="single-icon" style={symbolStyle} />
  <CircleLayer id="cluster" style={clusterStyle} />
  <SymbolLayer id="cluster-count" style={textStyle} />
</ShapeSource>
```

**Komponenten:**
* **ShapeSource**: Enthält die Geodaten (GeoJSON) (https://maplibre.org/maplibre-react-native/docs/components/sources/shape-source)
* **SymbolLayer**: Zeigt Symbole/Icons an (https://maplibre.org/maplibre-react-native/docs/components/layers/symbol-layer)
* **CircleLayer**: Zeichnet Kreise (z.B. für Cluster) (https://maplibre.org/maplibre-react-native/docs/components/layers/circle-layer)
* **LineLayer**: Für Linien bei Touren (https://maplibre.org/maplibre-react-native/docs/components/layers/line-layer)
* **MarkerView**: Nur für Custom React-Komponenten (Performance-Overhead) (https://maplibre.org/maplibre-react-native/docs/components/general/marker-view)

---

## 6. API-Migration Guide für Entwickler/innen

### 6.1 Breaking Changes

| Alt (`react-native-maps`) | Neu (`maplibre-react-native`) |
|---------------------------|-------------------------------|
| `<MapView initialRegion={...}>` | `<MapView>` + `<Camera defaultSettings={{centerCoordinate, zoomLevel}}>` |
| `<Marker coordinate={...}>` | `<ShapeSource>` + `<SymbolLayer>` + `<MarkerView>` |
| `<UrlTile urlTemplate={...}>` | `<MapView mapStyle="https://...style.json">` |
| `animateToRegion()` | `cameraRef.current.fitBounds()` oder `.setCamera()` |
| `region={{latitude, longitude, latitudeDelta, longitudeDelta}}` | `centerCoordinate={[lng, lat]}` + `zoomLevel={...}` |

**Wichtig:** GeoJSON verwendet `[longitude, latitude]` statt `{latitude, longitude}`!

### 6.2 User-Location (Eigene Position)

Die Darstellung der eigenen Position funktioniert mit MapLibre über die `UserLocation`-Komponente statt über Props am MapView und bietet erweiterte Konfigurationsmöglichkeiten.

### 6.3 Callouts und Tooltips

MapLibre hat keine eingebauten Callouts wie react-native-maps. Stattdessen werden Custom Overlays mit `MarkerView` verwendet oder alternativ Bottom-Sheets/Modals für Marker-Details. **Bekannte Einschränkung:** Custom Callouts verhalten sich auf Android anders als auf iOS. MarkerView hat einen Performance-Overhead und sollte sparsam eingesetzt werden.

---

## 7. Konfiguration und Anpassung

### 7.1 Remote Map Settings

Die Karten-Konfiguration kann zentral vom Server gesteuert werden über den Hook `useMapSettings()`:

```javascript
const { data } = useMapSettings();
// data enthält:
// - clusterRadius
// - clusterMaxZoom
// - clusterMinPoints
// - clusterFallbackColor
// - clusterSuperiorColor
// - markerImages (Icon-Definitionen)
// - layerStyles
// - zoomLevel
```

**Vorteile:**
* Keine App-Updates für Style-Änderungen nötig
* Kundenspezifische Anpassungen zentral verwaltbar
* A/B-Testing von Kartendarstellungen möglich

Beispiele:

```javascript
clusterSuperiorColor: '#949390',
clusterSuperiorTextColor: '#001E52',
clusterFallbackColor: '#949390',
clusterFallbackTextColor: '#001E52',
clusterDistance: 80,
clusterMaxZoom: 15,
clusterMinPoints: 3,
mapCenterPosition: {
  latitude: 52.402311244,
  longitude: 13.509221244
},
zoomLevel: {
  minZoom: 5,
  multipleMarkers: 10,
  singleMarker: 16
},
layerStyles: {
  singleIcon: {
    iconSize: 0.75,
    iconAnchor: 'bottom'
  },
  clusteredCircle: {
    circleRadius: 20
  },
  clusteredCircleShadow: {
    circleColor: '#949390',
    circleBlur: 0.8,
    circleRadius: 25,
    circleTranslate: [
      0,
      4
    ]
  },
  clusterCount: {
    textSize: 12,
    textColor: '#001E52'
  }
}
```

### 7.2 Marker-Icon-Konfiguration

Icons werden als Objekt definiert und der Map übergeben:

```javascript
const markerImages = {
  defaultPin: {
    uri: 'https://example.com/poi-icon.png',
    color: '#949390'
  },
  ownLocationPin: {
    uri: 'https://example.com/event-icon.png',
    color: '#001E52'
  }
};

<Images images={markerImages} />
```

### 7.3 Cluster-Konfiguration

**Grundeinstellungen:**
```javascript
<ShapeSource
  cluster={true}
  clusterRadius={50}              // Radius für Clustering
  clusterMaxZoomLevel={14}        // Ab diesem Zoom kein Clustering mehr
  clusterMinPoints={2}            // Minimum Punkte für Cluster
  clusterProperties={...}         // Aggregation von Properties
/>
```

**Clustering-Ausnahmen:** Einzelne Marker können vom Clustering ausgeschlossen werden (z.B. ein vom User gewählter alternativer Standort). Dafür gibt es zwei Ansätze: (1) Separate ShapeSource ohne Clustering für spezielle Marker, oder (2) Filterung der GeoJSON-Daten nach Properties. Der erste Ansatz ist einfacher zu handhaben, der zweite flexibler bei vielen Ausnahmen.

**Dynamische Farbgebung:**
```javascript
const clusterCircleColor = [
  'case',
  ['>=', ['+', ...typeChecks], 2],  // Wenn 2+ Typen
  '#FF5733',                         // Superior Color
  ...typeCases,                      // Einzelne Typ-Farben
  '#CCCCCC'                          // Fallback
];

<CircleLayer
  id="cluster"
  style={{
    circleColor: clusterCircleColor,
    circleRadius: 30
  }}
/>
```

### 7.4 Filter und Layer-Verwaltung

Dynamische Filter und Overlays werden über Layer-Filter und mehrere ShapeSources realisiert. Filter-Expressions ermöglichen das Ein-/Ausblenden von Features basierend auf Properties. **Performance-Tipp:** Layer-Sichtbarkeit per Style zu kontrollieren ist performanter als GeoJSON neu zu generieren. Marker können dynamisch durch State-Updates hinzugefügt oder entfernt werden.

### 7.5 Style-Anpassungen

Layer-Styles können spezifisch angepasst werden:

```javascript
const layerStyles = {
  singleIcon: {
    iconSize: 1,
    iconAnchor: 'bottom',
    iconAllowOverlap: true
  },
  clusteredCircle: {
    circleRadius: 30,
    circleOpacity: 1
  },
  clusterCount: {
    textField: ['get', 'point_count'],
    textSize: 14,
    textColor: '#FFFFFF'
  }
};
```

---

## 8. Migrationsstrategie

Zur Risikominimierung läuft die Migration schrittweise:

### 8.1 Schrittweise Migration

**Phase 1** (✅ abgeschlossen):
- MapLibre-Implementierung ist in Entwicklung funktional
- Alte Map bleibt in Apps erhalten
- Tests beider Versionen möglich

**Phase 2** (✅ abgeschlossen):
- Vollständige Ablösung der alten Implementierung
- Entfernung von `react-native-maps` als Dependency
- Schrittweiser Austausch in allen Screens
- Integration in Test-Apps

**Phase 3** (🔄 aktuell):
- Tests mit bestimmtem Kundenstamm

**Phase 4** (⏳ geplant):
- Vollständiger Rollout in allen Apps

---

## 9. Voraussetzungen und Dependencies

### 9.1 Neue Dependencies

```json
{
  "@maplibre/maplibre-react-native": "^10.4.0",
}
```

### 9.2 Expo Config Plugin

In `app.json`:
```json
{
  "plugins": [
    ...,
    "@maplibre/maplibre-react-native",
    ...
  ]
}
```

### 9.3 Build-Anforderungen

* **Expo SDK**: 52.0+
* **React Native**: 0.76+
* **Expo Prebuild**: Erforderlich für native Module
* **Expo Go**: Nicht kompatibel (Development Builds erforderlich)

**Build-Kommandos:**
```bash
# Prebuild (native Ordner generieren)
npx expo prebuild --clean

# Development Builds
eas build --profile development --platform ios
eas build --profile development --platform android

# Production Builds
eas build --profile production --platform all
```

MapLibre benötigt native Module und funktioniert daher nicht in Expo Go. Development Builds sind erforderlich.

### 9.4 iOS-spezifische Konfiguration

Das Expo Config Plugin fügt automatisch Post-Install-Hooks zum Podfile hinzu:

```ruby
# ios/Podfile (automatisch generiert)
post_install do |installer|
  $MLRN.post_install(installer)
  # ...
end
```

**Wichtig:** Nach Änderungen an nativen Dependencies:
```bash
cd ios && pod install && cd ..
```

### 9.5 Android-spezifische Konfiguration

Keine manuellen Änderungen erforderlich, das Config Plugin kümmert sich um:
- Gradle-Abhängigkeiten
- Permissions
- Maven-Repositories

### 9.6 React Native New Architecture

Die Smart Village App nutzt die neue React Native Architektur (Fabric, TurboModules). MapLibre v10 unterstützt diese nur über einen Interoperability Layer, was zu Kompatibilitätsproblemen führen kann.

**Bekannte Einschränkungen:**
- Nicht alle Features sind vollständig kompatibel mit der neuen Architektur
- Gelegentliche Instabilitäten bei komplexen Interaktionen
- Performance-Einbußen durch den Interoperability Layer

**Zukunftsperspektive:**
- MapLibre v11 (Alpha) bietet native Unterstützung für die neue Architektur
- Migration auf v11 ist für Phase 3 der Kartenmigration geplant
- Aktuelle Tracking: [MapLibre React Native GitHub](https://github.com/maplibre/maplibre-react-native/tree/alpha)
- [Offizieller v10→v11 Migration Guide](https://github.com/maplibre/maplibre-react-native/blob/alpha/docs/content/setup/migrations/v11.md)

---

## 10. Testing und Qualitätssicherung

### 10.1 Manuelle Tests

Checkliste für Tests:
- [ ] Einzelner Marker wird korrekt angezeigt
- [ ] Mehrere Marker werden geclustert
- [ ] Cluster expandieren beim Zoomen
- [ ] Clustering-Ausnahme: Ausgewählter alternativer Standort wird nicht geclustert
- [ ] Custom Icons werden geladen
- [ ] Marker mit unterschiedlichen Icons können überlagert werden (iconAllowOverlap)
- [ ] Marker-Interaktion (onPress) funktioniert
- [ ] Tooltip/Callout wird bei Marker-Klick angezeigt
- [ ] User-Location (eigene Position) wird korrekt dargestellt
- [ ] Camera-Interaktion: Zentrierung durch Buttons/Aktionen funktioniert
- [ ] Camera-Animationen laufen flüssig (setCamera, fitBounds)
- [ ] Filter: Layer können ein-/ausgeblendet werden
- [ ] Overlays: Popups können über Markern angezeigt werden
- [ ] Marker setzen: Neue Marker können beliebig gesetzt werden
- [ ] Performance bei 100+ Markern
- [ ] Rotation und Pitch (falls aktiviert)

### 10.2 Bekannte Einschränkungen

**Library-spezifisch (MapLibre v10):**
* **New Architecture Kompatibilität**: v10 nutzt nur Interoperability Layer, was zu Instabilitäten führen kann
* **State-Update-Probleme**: Schnelle State-Änderungen können zu Rendering-Problemen führen
* **Layer-Animationen**: Nicht alle Animationen funktionieren zuverlässig mit dem Interoperability Layer

**Implementierungs-spezifisch:**
* **MarkerView Performance**: Custom React-Komponenten als Marker sollten sparsam eingesetzt werden (Performance-Overhead)
* **Android Callout**: Custom Callouts verhalten sich auf Android anders als auf iOS
* **Animationen**: Einige Animationen sind iOS-only
* **Memory**: Bei sehr vielen Markern (1000+) Memory-Management beachten

**Workarounds:**
- Reduzierung von State-Updates durch Debouncing
- Vermeidung komplexer Animationen bis Migration auf v11
- Nutzung von `SymbolLayer` statt `MarkerView` wo möglich

### 10.3 Performance-Optimierungen

Best Practices:
* `SymbolLayer` statt `MarkerView` wo möglich
* Clustering aktivieren bei >20 Markern
* `iconAllowOverlap` nur wenn nötig (Performance-Impact)
* `memoization` von GeoJSON-Daten
* `useMemo` für Style-Expressions

```javascript
// ✅ Gut: Memoized GeoJSON
const geoJsonData = useMemo(() =>
  featureCollection(locations.map(loc => point([loc.lng, loc.lat], loc))),
  [locations]
);

// ❌ Schlecht: Wird bei jedem Render neu erstellt
const geoJsonData = featureCollection(
  locations.map(loc => point([loc.lng, loc.lat], loc))
);
```

---

## 11. Offene Aufgaben & nächste Schritte

Diese Liste wird fortlaufend ergänzt:

* [ ] Performance-Monitoring in Production
* [ ] Migration auf MapLibre v11 (Alpha) für nativen Support der neuen React Native Architektur
* [ ] Dokumentation von Edge Cases und Workarounds
* [ ] Individualisierungsmöglichkeiten optimieren
* [ ] Offline-Tile-Caching evaluieren

---

## 12. Zielsetzung des Umstiegs

Für Kund/innen und Nutzer/innen bedeutet diese Migration letztlich:

* **Sichtbar bessere Kartenqualität**
* **Mehr Geschwindigkeit und Stabilität**
* **Zukunftssichere Weiterentwicklungen**
* **Grundlage für neue Features** wie dynamische Layer, 3D-Darstellungen oder Offline-Karten
* **Datensouveränität** durch eigene Infrastruktur
* **Keine externen API-Kosten** (mehr)

Für Entwickler/innen bedeutet es:

* Eine modernere, flexiblere Kartenbasis
* Klarere Kontrollmöglichkeiten über die Darstellung und Logik
* Weniger technische Schulden in Zukunft
* Standard-konforme GeoJSON-Architektur
* Bessere Performance durch natives Layer-System
* Zukunftssichere Technologie mit aktiver Community

---

## 13. Fazit

Der Umstieg auf `maplibre-react-native` war notwendig, um das Kartenmodul der Smart Village App zukunftsfähig, performant und optisch hochwertig zu gestalten. Trotz der Herausforderungen bietet MapLibre deutlich bessere technische Perspektiven und passt ideal zu unserem Anspruch, eigene Open-Source-Kartendaten optimal nutzen zu können.

Die Investition in einen eigenen Tile-Server und die moderne GeoJSON-basierte Architektur zahlen sich langfristig durch Unabhängigkeit, Performance und Flexibilität aus.

Dieses Dokument wird laufend erweitert, um alle Schritte der Migration nachvollziehbar festzuhalten.

---

## 14. Ressourcen und Links

### Offizielle Dokumentation
* [MapLibre Native](https://maplibre.org/maplibre-native/)
* [MapLibre React Native](https://github.com/maplibre/maplibre-react-native)
* [MapLibre React Native v11 Migration Guide](https://github.com/maplibre/maplibre-react-native/blob/alpha/docs/content/setup/migrations/v11.md) - Offizieller Upgrade-Guide von v10 auf v11
* [Mapbox Style Specification](https://docs.mapbox.com/style-spec/) (kompatibel mit MapLibre)
* [GeoJSON Specification](https://geojson.org/)

### Interne Ressourcen
* **Branch:** `epic/map`
* **Hauptkomponente:** `src/components/map/MapLibre.tsx`
* **Hook:** `src/hooks/map/mapFeatureConfig.ts`
* **Tile-Server:** `https://tileserver-gl.smart-village.app`
* **Karten-Modul-Doku:** [`docs/module/karten.md`](../module/karten.md)
* **Setup-Dokumentation:** [`docs/dev/setup.md`](setup.md)
* **System-Architektur:** [`docs/system/maptiles.md`](../system/maptiles.md)

### Hilfreiche Tools
* [GeoJSON.io](http://geojson.io/) - GeoJSON visualisieren und erstellen
* [Maputnik](https://maputnik.github.io/) - Visual Style Editor für MapLibre/Mapbox
* [Turf.js](https://turfjs.org/) - GeoJSON-Operationen

### Community
* [MapLibre Slack](https://slack.openstreetmap.us/) (#maplibre-react-native Channel)
* [GitHub Discussions](https://github.com/maplibre/maplibre-react-native/discussions)
