# Service-Kacheln (Service Tiles)

Service-Kacheln sind UI-Komponenten auf dem Startbildschirm der App, die Nutzern schnellen Zugriff auf verschiedene Services und Inhalte ermöglichen. Diese Dokumentation beschreibt die verfügbaren Kachel-Typen und Navigationsoptionen.

---

## Kachel-Typen

Es gibt **4 verschiedene Kachel-Typen**, die sich durch ihre visuelle Darstellung unterscheiden:

### Typ 1: Nur Bild

Kachel mit einem PNG-Bild ohne Text oder Icon.

```json
{
  "tile": "URL zum PNG-Bild",
  "accessibilityLabel": "Beschreibung für Barrierefreiheit",
  "routeName": "...",
  "params": { ... }
}
```

**Was muss angegeben werden:**

- `tile`: URL zum PNG-Bild (z.B. von Minio)
- `accessibilityLabel`: Beschreibungstext für Screenreader
- `routeName`: Siehe [Navigationstypen](#navigationstypen)
- `params`: Abhängig vom gewählten Navigationstyp

---

### Typ 2: Icon + Titel (Standard-Stil)

Kachel mit Icon und Titel im System-Standard-Stil.

```json
{
  "title": "Titel der Kachel",
  "iconName": "Icon-Name aus Expo Icons",
  "icon": "URL zum PNG-Icon (optional)",
  "accessibilityLabel": "Beschreibung für Barrierefreiheit",
  "routeName": "...",
  "params": { ... }
}
```

**Was muss angegeben werden:**

- `title`: Text auf der Kachel (Zeilenumbruch mit `\n` möglich)
- `iconName`: Name aus [Expo Icons](https://icons.expo.fyi/) (z.B. `calendar`, `home`, `car`)
- `icon`: (Optional) URL zum PNG-Icon, überschreibt `iconName`
- `accessibilityLabel`: Beschreibungstext für Screenreader
- `routeName`: Siehe [Navigationstypen](#navigationstypen)
- `params`: Abhängig vom gewählten Navigationstyp

---

### Typ 3: Icon + Titel (Globaler Stil)

Kachel mit Icon und Titel, Styling wird zentral in `globalSettings` definiert.

**Kachel-Konfiguration:**

```json
{
  "title": "Titel der Kachel",
  "iconName": "Icon-Name aus Expo Icons",
  "icon": "URL zum PNG-Icon (optional)",
  "accessibilityLabel": "Beschreibung für Barrierefreiheit",
  "routeName": "...",
  "params": { ... }
}
```

**Global Settings (Main Server → Settings → Global Settings):**

```json
{
  "appDesignSystem": {
    "serviceTiles": {
      "numberOfLines": 2,
      "tileStyle": {
        "backgroundColor": "#7CF7EF",
        "marginBottom": 7,
        "borderRadius": 8,
        "height": 120,
        "alignSelf": "center"
      },
      "fontStyle": {
        "fontFamily": "regular",
        "fontWeight": "600",
        "fontSize": 12,
        "lineHeight": 15,
        "color": "#000",
        "paddingHorizontal": 5
      },
      "iconStyle": {
        "iconSize": 24,
        "color": "#000"
      }
    }
  }
}
```

**Was muss im Global Setting definiert werden:**

- **tileStyle**: Hintergrundfarbe, Abstände, Rundung, Höhe, Ausrichtung
- **fontStyle**: Schriftart, Größe, Farbe, Abstände
- **iconStyle**: Icon-Größe und Farbe
- **numberOfLines**: Maximale Zeilenanzahl für Titel

---

### Typ 4: Icon + Titel (Individueller Stil)

Kachel mit Icon und Titel, Styling wird direkt in der Kachel definiert.

```json
{
  "title": "Titel der Kachel",
  "iconName": "Icon-Name aus Expo Icons",
  "icon": "URL zum PNG-Icon (optional)",
  "accessibilityLabel": "Beschreibung für Barrierefreiheit",
  "routeName": "...",
  "params": { ... },
  "style": {
    "numberOfLines": 2,
    "tileStyle": {
      "backgroundColor": "#5d6a80",
      "marginBottom": 7,
      "borderRadius": 0,
      "height": 120,
      "alignSelf": "center"
    },
    "fontStyle": {
      "fontFamily": "bold",
      "fontWeight": "600",
      "fontSize": 14,
      "lineHeight": 15,
      "color": "#fff",
      "paddingHorizontal": 5
    },
    "iconStyle": {
      "iconSize": 24,
      "color": "#00CABE"
    }
  },
}
```

**Was muss angegeben werden:**

- Alle Felder wie bei Typ 2 und 3
- `tileStyle`: Individuelle Kachel-Formatierung (überschreibt globalen Stil)
- `fontStyle`: Individuelle Schrift-Formatierung (überschreibt globalen Stil)
- `iconStyle`: Individuelle Icon-Formatierung (überschreibt globalen Stil)

---

## Wichtige Hinweise

### Stil-Priorität

Die Anwendung der Styles erfolgt in dieser Reihenfolge:

1. **Individueller Stil** (direkt in der Kachel) → höchste Priorität
2. **Globaler Stil** (in globalSettings)
3. **System-Standard** → niedrigste Priorität

### Icons

- **Expo Icons**: Verwenden Sie `iconName` mit einem Namen aus [Expo Icons Directory](https://icons.expo.fyi/)
  - Beispiele: `home`, `calendar`, `car`, `wallet`, `information-circle`, `map`, `notifications`
- **Eigene Icons**: Verwenden Sie `icon` mit URL zu PNG-Bild
  - Falls beide angegeben sind, wird `icon` verwendet

### Barrierefreiheit

- **Pflichtfeld**: `accessibilityLabel` muss bei jeder Kachel angegeben werden
- Beschreibt die Kachel für Screenreader-Nutzer

### Textformatierung

- Zeilenumbruch im Titel: `\n` verwenden (z.B. `"Mitfahr\ngelegenheit"`)
- Maximale Zeilen: Über `numberOfLines` im Global Setting steuerbar (Standard: 2)

---

## Navigationstypen

Jede Kachel navigiert zu einem Bildschirm. Die folgenden Navigationstypen sind verfügbar:

### 1. HTML-Seite

Zeigt HTML-Inhalt an, der im Main Server unter "Static Contents" hinterlegt ist.

```json
{
  "routeName": "Html",
  "params": {
    "title": "Seitentitel",
    "query": "publicHtmlFile",
    "queryVariables": {
      "name": "nameDerStaticContent"
    }
  }
}
```

**Was muss angegeben werden:**

- `params.title`: Titel des Bildschirms
- `params.queryVariables.name`: Name des Static Contents (kleingeschrieben, ohne Leerzeichen)

---

### 2. WebView

Öffnet eine externe oder interne Webseite.

```json
{
  "routeName": "Web",
  "params": {
    "title": "Seitentitel",
    "webUrl": "https://www.example.com/",
    "isExternal": true
  }
}
```

**Was muss angegeben werden:**

- `params.title`: Titel des Bildschirms
- `params.webUrl`: URL der Webseite
- `params.isExternal`: `true` für externe Links, `false` für interne

---

### 3. Feedback-Formular

Öffnet das App-Feedback-Formular.

```json
{
  "routeName": "Form"
}
```

**Was muss angegeben werden:**

- Keine weiteren Parameter erforderlich

---

### 4. Abfallkalender

Öffnet das Abfallkalender-Modul.

```json
{
  "routeName": "WasteCollection"
}
```

**Was muss angegeben werden:**

- Keine weiteren Parameter erforderlich

---

### 5. Mitfahrbänke

Öffnet das Mitfahrbänke-Modul.

```json
{
  "routeName": "EncounterHome"
}
```

**Was muss angegeben werden:**

- Keine weiteren Parameter erforderlich

---

### 6. Umfragen

Öffnet die Umfragen-Übersicht.

```json
{
  "routeName": "SurveyOverview"
}
```

**Was muss angegeben werden:**

- Keine weiteren Parameter erforderlich

---

### 7. Wallet

Öffnet das Wallet-Modul.

```json
{
  "routeName": "WalletHome",
  "params": {
    "title": "Wallet"
  }
}
```

**Was muss angegeben werden:**

- `params.title`: Titel des Bildschirms

---

### 8. Verschachtelte Navigation

Für mehrstufige Inhalte oder Kategorien.

```json
{
  "routeName": "NestedInfo",
  "params": {
    "name": "eindeutigerName",
    "title": "Seitentitel"
  }
}
```

**Was muss angegeben werden:**

- `params.name`: Eindeutiger Identifier (kleingeschrieben, ohne Leerzeichen)
- `params.title`: (Optional) Titel des Bildschirms

---

### 9. Listen-Ansicht (Index)

Zeigt Listen von Veranstaltungen, News, Kategorien etc. an.

```json
{
  "routeName": "Index",
  "params": {
    "query": "eventRecords",
    "queryVariables": {
      "limit": 15,
      "order": "listDate_ASC"
    },
    "rootRouteName": "EventRecords",
    "title": "Veranstaltungen"
  }
}
```

**Was muss angegeben werden:**

- `params.query`: Datentyp (`eventRecords`, `newsItems`, `categories`, `tours`, `pointsOfInterest`)
- `params.queryVariables.limit`: Anzahl der Einträge
- `params.queryVariables.order`: Sortierung (`listDate_ASC` oder `listDate_DESC`)
- `params.rootRouteName`: Name für die Navigation
- `params.title`: Titel des Bildschirms

**Optionale Parameter:**

- `params.queryVariables.initialFilter`: `"map"` oder `"list"` (Standardansicht)
- `params.isPreviewWithoutNavigation`: `true` für Vorschau ohne Weiternavigation

**Variante: Spezifische Kategorien anzeigen**

```json
{
  "routeName": "Index",
  "params": {
    "query": "categories",
    "queryVariables": {
      "ids": [123, 456, 789]
    },
    "rootRouteName": "categoryExample",
    "title": "Unterkategorien"
  }
}
```

**Was zusätzlich angegeben wird:**

- `params.queryVariables.ids`: Array mit Kategorie-IDs

---

### 10. HTML-Seite mit Button

HTML-Seite mit einem Button, der zu einem anderen Bildschirm navigiert.

```json
{
  "routeName": "Html",
  "params": {
    "title": "Seitentitel",
    "query": "publicHtmlFile",
    "queryVariables": {
      "name": "nameDerStaticContent"
    },
    "rootRouteName": "eindeutigerName",
    "subQuery": {
      "routeName": "Web",
      "buttonTitle": "Button-Beschriftung",
      "webUrl": "https://www.example.com/",
      "isExternal": true
    }
  }
}
```

**Was muss angegeben werden:**

- Alle Parameter wie bei "HTML-Seite"
- `params.subQuery.routeName`: Ziel-Navigation (siehe andere Navigationstypen)
- `params.subQuery.buttonTitle`: Text auf dem Button
- Weitere Parameter je nach `routeName` im `subQuery`

**Mögliche routeNames im subQuery:**

- `Web` → WebView öffnen
- `WasteCollection` → Zum Abfallkalender
- `Index` → Zu einer Listen-Ansicht
- `BBBUSIndex` → Zum BB-BUS Service
- Alle anderen Navigationstypen

---

### 11. HTML-Seite mit mehreren Buttons

HTML-Seite mit mehreren Buttons für unterschiedliche Navigationen.

```json
{
  "routeName": "Html",
  "params": {
    "title": "Seitentitel",
    "query": "publicHtmlFile",
    "queryVariables": {
      "name": "nameDerStaticContent"
    },
    "rootRouteName": "eindeutigerName",
    "subQuery": {
      "routeName": "Web",
      "buttonTitle": "Erster Button",
      "webUrl": "https://www.example1.com/",
      "isExternal": true,
      "buttons": [
        "https://www.direkterLink.com/",
        {
          "routeName": "Web",
          "buttonTitle": "Zweiter Button",
          "webUrl": "https://www.example2.com/",
          "isExternal": true
        },
        {
          "routeName": "Index",
          "buttonTitle": "Dritter Button",
          "paramsForButton": {
            "query": "eventRecords",
            "queryVariables": { "limit": 15 },
            "rootRouteName": "events",
            "title": "Veranstaltungen"
          }
        }
      ]
    }
  }
}
```

**Was muss angegeben werden:**

- Alle Parameter wie bei "HTML-Seite mit Button"
- `params.subQuery.buttons`: Array mit Button-Konfigurationen

**Button-Array kann enthalten:**

1. **String**: Direkte URL als einfacher Link
2. **Object mit routeName**: Navigation zu einem Bildschirm
   - Mit direkten Parametern (wie beim ersten Button)
   - Mit `paramsForButton` für strukturierte Parameter

---

### 12. Schwarzes Brett mit Formular

Schwarzes Brett mit Button zum Erstellen neuer Einträge.

```json
{
  "routeName": "NestedInfo",
  "params": {
    "name": "noticeBoardNavigation",
    "title": "Schwarzes Brett",
    "rootRouteName": "NestedInfo",
    "subQuery": {
      "routeName": "NoticeboardForm",
      "buttonTitle": "Neuer Eintrag",
      "params": {
        "newEntryForm": true,
        "name": "noticeBoardNeueEintrag",
        "rootRouteName": "NoticeboardForm",
        "title": "Neuer Eintrag"
      }
    }
  }
}
```

**Was muss angegeben werden:**

- `params.name`: Eindeutiger Name für die Navigation
- `params.title`: Titel der Übersichtsseite
- `params.subQuery.buttonTitle`: Text auf dem Button
- `params.subQuery.params.newEntryForm`: `true` für neues Formular
- `params.subQuery.params.title`: Titel des Formulars

---

### 13. BB-BUS Service

Spezielle Navigation zum Bürger- und Unternehmensservice.

```json
{
  "routeName": "Html",
  "params": {
    "title": "Bürger- und Unternehmensservice",
    "query": "publicHtmlFile",
    "queryVariables": {
      "name": "bb-bus"
    },
    "rootRouteName": "BBBUS",
    "subQuery": {
      "routeName": "BBBUSIndex",
      "buttonTitle": "Service öffnen",
      "webUrl": "true"
    }
  }
}
```

**Was muss angegeben werden:**

- Spezielle Konfiguration für BB-BUS-Modul
- `params.queryVariables.name`: Muss `"bb-bus"` sein
- `params.subQuery.routeName`: Muss `"BBBUSIndex"` sein
- `params.subQuery.webUrl`: Auf `"true"` setzen

---

## Übersicht: Alle Navigationstypen

| routeName         | Beschreibung      | Parameter erforderlich | Verwendung                |
| ----------------- | ----------------- | ---------------------- | ------------------------- |
| `Html`            | HTML-Inhalt       | ✓                      | Static Contents anzeigen  |
| `Web`             | WebView           | ✓                      | Externe/Interne Webseiten |
| `Form`            | Feedback-Formular | –                      | App-Feedback              |
| `WasteCollection` | Abfallkalender    | –                      | Müllabfuhr-Termine        |
| `EncounterHome`   | Mitfahrbänke      | –                      | Carsharing-Locations      |
| `SurveyOverview`  | Umfragen          | –                      | Umfragen-Liste            |
| `WalletHome`      | Wallet            | –                      | Digitale Tickets/Pässe    |
| `NestedInfo`      | Verschachtelt     | ✓                      | Mehrstufige Navigation    |
| `Index`           | Listen-Ansicht    | ✓                      | Events, News, POIs, etc.  |
| `BBBUSIndex`      | BB-BUS            | Spezial                | Behördenservices          |
| `NoticeboardForm` | Schwarzes Brett   | ✓                      | Community-Pinnwand        |

---

## Vollständige Beispiele

### Beispiel 1: Nur-Bild-Kachel zu WebView

```json
{
  "tile": "https://fileserver.smart-village.app/kacheln/gutscheine.png",
  "accessibilityLabel": "Gutscheine",
  "routeName": "Web",
  "params": {
    "title": "Gutscheine",
    "webUrl": "https://www.example.com/gutscheine",
    "isExternal": true
  }
}
```

---

### Beispiel 2: Icon-Kachel mit globalem Stil zu Veranstaltungen

```json
{
  "title": "Veranstaltungen",
  "iconName": "calendar",
  "accessibilityLabel": "Veranstaltungskalender",
  "routeName": "Index",
  "params": {
    "query": "eventRecords",
    "queryVariables": {
      "limit": 15,
      "order": "listDate_ASC",
      "initialFilter": "list"
    },
    "rootRouteName": "EventRecords",
    "title": "Veranstaltungen"
  }
}
```

---

### Beispiel 3: Individuell gestylte Kachel zum Abfallkalender

```json
{
  "title": "Abfall\nkalender",
  "iconName": "trash",
  "accessibilityLabel": "Abfallkalender",
  "routeName": "WasteCollection",
  "tileStyle": {
    "backgroundColor": "#4CAF50",
    "borderRadius": 12,
    "height": 130
  },
  "fontStyle": {
    "fontSize": 14,
    "color": "#FFF",
    "fontWeight": "600"
  },
  "iconStyle": {
    "iconSize": 28,
    "color": "#FFF"
  }
}
```

---

### Beispiel 4: HTML-Seite mit Button

```json
{
  "title": "Stadtinfo",
  "iconName": "information-circle",
  "accessibilityLabel": "Stadtinformationen",
  "routeName": "Html",
  "params": {
    "title": "Über unsere Stadt",
    "query": "publicHtmlFile",
    "queryVariables": {
      "name": "stadtinfo"
    },
    "rootRouteName": "CityInfo",
    "subQuery": {
      "routeName": "Web",
      "buttonTitle": "Zur Webseite",
      "webUrl": "https://www.stadt-example.de",
      "isExternal": true
    }
  }
}
```

---

### Beispiel 5: Schwarzes Brett mit Formular

```json
{
  "title": "Schwarzes\nBrett",
  "iconName": "md-heart-half",
  "accessibilityLabel": "Schwarzes Brett - Anzeigen veröffentlichen",
  "routeName": "NestedInfo",
  "params": {
    "name": "noticeboard",
    "title": "Schwarzes Brett",
    "rootRouteName": "NestedInfo",
    "subQuery": {
      "routeName": "NoticeboardForm",
      "buttonTitle": "Neue Anzeige",
      "params": {
        "newEntryForm": true,
        "name": "noticeboardNewEntry",
        "rootRouteName": "NoticeboardForm",
        "title": "Neue Anzeige erstellen"
      }
    }
  }
}
```

---

## Praktische Hinweise

### Wo werden Service-Kacheln konfiguriert?

Service-Kacheln werden im **Main Server** unter **Settings → Global Settings** konfiguriert.

**JSON-Struktur:**

```json
{
  "serviceTiles": [
    { ... },
    { ... }
  ]
}
```

### Bilder hochladen

- **PNG-Bilder** für Kacheln und Icons werden auf **Minio** hochgeladen
- URL-Format: `https://fileserver.smart-village.app/[umgebung]/kacheln/bildname.png`
- Empfohlene Größe für Kachel-Bilder: 300x300 Pixel
- Empfohlene Größe für Icons: 64x64 Pixel
- Dateigröße: Maximal 200KB

### HTML-Inhalte erstellen

HTML-Inhalte werden im **Main Server** unter **Settings → Static Contents** erstellt:

1. Neuen Static Content anlegen
2. **Name**: Eindeutiger Name (kleingeschrieben, ohne Leerzeichen)
3. **Data type**: `HTML` auswählen
4. **Content**: HTML-Code eingeben
5. Speichern

Der Name wird dann in der Kachel-Konfiguration unter `queryVariables.name` verwendet.

### Global Settings für Kachel-Styling

Global Settings werden im **Main Server** unter **Settings → Global Settings** als JSON konfiguriert:

```json
{
  "appDesignSystem": {
    "serviceTiles": {
      "numberOfLines": 2,
      "tileStyle": { ... },
      "fontStyle": { ... },
      "iconStyle": { ... }
    }
  }
}
```

### Tipps für barrierefreie Kacheln

- **Kontrast**: Mindestens 4.5:1 (WCAG 2.1 AA Standard)
- **Schriftgröße**: Mindestens 12px
- **Touch-Target**: Mindestens 44x44 Pixel
- **accessibilityLabel**: Immer aussagekräftig formulieren
- **Farben**: Nicht nur Farbe zur Unterscheidung nutzen

---

## Fehlerbehebung

### Kachel wird nicht angezeigt

**Mögliche Ursachen:**

- JSON-Syntaxfehler → Überprüfen Sie die JSON-Struktur
- Fehlender `routeName` → Pflichtfeld prüfen
- Fehlender `accessibilityLabel` → Pflichtfeld ergänzen

### Icon wird nicht angezeigt

**Mögliche Ursachen:**

- Falscher `iconName` → Prüfen Sie [Expo Icons Directory](https://icons.expo.fyi/)
- Bild-URL nicht erreichbar → Testen Sie die URL im Browser
- Icon-Farbe = Hintergrundfarbe → Kontrast prüfen

### Button auf HTML-Seite fehlt

**Mögliche Ursachen:**

- `subQuery` fehlt oder falsch konfiguriert
- `buttonTitle` fehlt → Pflichtfeld im subQuery
- Falsche Parameter im `subQuery` → Je nach `routeName` prüfen

### Styling wird nicht angewendet

**Mögliche Ursachen:**

- Global Settings nicht gespeichert → Speichern und App neu starten
- Falsche JSON-Syntax im Style → Farbcodes mit `#`, Zahlen ohne Anführungszeichen
- Individueller Stil überschreibt globalen → Prüfen Sie die Priorität

---

## Versionshinweise

**Unterstützte Versionen:** Smart Village App v4.0.0+

**Erweiterte Features ab v4.1.1:**

- HTML-Seiten mit mehreren Buttons
- Erweiterte Styling-Optionen
- Zusätzliche Navigationstypen

---

## Weitere Ressourcen

- **Expo Icons**: [https://icons.expo.fyi/](https://icons.expo.fyi/)
- **WCAG Richtlinien**: [https://www.w3.org/WAI/WCAG21/quickref/](https://www.w3.org/WAI/WCAG21/quickref/)
- **JSON Validator**: [https://jsonlint.com/](https://jsonlint.com/)
