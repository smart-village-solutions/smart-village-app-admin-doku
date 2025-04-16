---
layout: default
title: Main-Server "Settings"
---

# Einstellungen im Backend / auf dem Main-Server
Hier werden Einstellungen in den "Settings" des Main-Servers beschrieben


## Categories
tbd

## Data Ressources 
tbd


## Static Content




### ⚙️ App-Konfiguration: `globalSettings`

Type: *json* <br><br>
Diese Datei beschreibt die zentralen globalen Einstellungen der Smart-Village-App. Die Konfigurationswerte beeinflussen das Verhalten und die Darstellung von Inhalten innerhalb der App.

---

#### 📁 filter

Steuert, welche Inhaltsarten im Filterbereich der App angezeigt oder deaktiviert sind.

```json
"filter": {
  "news": false,
  "events": true,
  "eventLocations": true
}
```

- `news`: Wenn `true`, können Nachrichten gefiltert werden.
- `events`: Wenn `true`, können Veranstaltungen gefiltert werden.
- `eventLocations`: Wenn `true`, können Veranstaltungsorte im Filter genutzt werden.

> Beispielhafte Darstellung:  
> ![Platzhalter-Bild](filter-placeholder.png)

---

#### 🖼️ showImageRights

Zeigt oder versteckt die Angabe der Bildrechte bei Bildern in der App.

```json
"showImageRights": true
```

- `true`: Urhebervermerk bei Bildern wird angezeigt.
- `false`: Urhebervermerk wird unterdrückt.

> Beispiel: Bild mit eingeblendeten Bildrechten  
> ![Logo](/smart-village-app-admin-doku/images/imagerights.jpg)

---

#### 📚 sections

Definiert, welche Sektionen in der App erscheinen und wie sie betitelt werden.

##### 🔹 Sichtbarkeit

```json
"showNews": true,
"showPointsOfInterestAndTours": false,
"showEvents": true
```

- Zeigt oder verbirgt komplette Bereiche der App (z. B. News, POIs, Events).

#### 🔹 Headlines und Buttons

Diese Texte erscheinen als Überschrift oder Aktionsbutton in der App:

```json
"headlineNews": "Nachrichten",
"buttonNews": "Alle Nachrichten anzeigen",
"headlineEvents": "Veranstaltungen",
"buttonEvents": "Alle Veranstaltungen anzeigen",
...
```

#### 🔹 Kategoriezuweisung (Beispiel für News)

```json
"categoriesNews": [
  {
    "categoryId": 854,
    "categoryTitle": "Nachrichten",
    "categoryTitleDetail": "Nachricht",
    "categoryButton": "Alle Nachrichten anzeigen"
  }
]
```

> Beispielhafte App-Darstellung mit angepasster Buttonbeschriftung:  
> ![Platzhalter-Bild](sections-placeholder.png)

---

### 📆 eventListIntro

Ein Einführungstext oberhalb der Veranstaltungsübersicht inkl. Aktionsbutton.

```json
"eventListIntro": {
  "buttonType": "top",
  "introText": "Es fehlt eine Veranstaltung im Kalender? Auf den Button klicken und über das jeweilige Formular melden!",
  "buttonTitle": "Veranstaltung hinzufügen",
  "url": "https://www.smarte-region-linz.de/veranstaltungen-ort"
}
```

- `introText`: Text zur Erklärung der Funktion
- `buttonTitle`: Beschriftung des Buttons
- `url`: Zieladresse beim Klick auf den Button

> Vorschau mit Einleitungstext und Button:  
> ![Platzhalter-Bild](event-intro-placeholder.png)

---

### ⚙️ settings

#### ▶️ Slider

```json
"sliderPauseButton": {
  "show": true,
  "size": 15,
  "horizontalPosition": "right",
  "verticalPosition": "bottom"
},
"sliderSettings": {
  "autoplayInterval": 8000
}
```

- Aktiviert einen Pause-Button im Bildslider
- `autoplayInterval`: Dauer in Millisekunden zwischen Slides

#### 🔄 Personalisierte Kacheln & Ansichten

```json
"personalizedTiles": true,
"switchBetweenListAndMap": "bottom-floating-button"
```

- `personalizedTiles`: Kacheln werden individuell angepasst
- `switchBetweenListAndMap`: Umschaltmöglichkeit zwischen Listen- und Kartenansicht

#### 📲 Push-Mitteilungen

```json
"pushNotifications": true
```

- Aktiviert die Nutzung von Push-Nachrichten

#### 🗓️ Event-Kalender

```json
"eventCalendar": {
  "dotCount": 1,
  "subList": true
}
```

- `dotCount`: Anzahl an Punkten pro Tag in der Kalenderansicht
- `subList`: Wenn `true`, wird eine Unterliste mit Events angezeigt

#### 📅 Kalenderumschaltung

```json
"calendarToggle": true
```

- Zeigt einen Schalter zum Wechsel zwischen verschiedenen Kalenderansichten

> Beispielhafte Slider- und Kalenderdarstellung:  
> ![Platzhalter-Bild](slider-calendar-placeholder.png)

---

### 📈 Matomo (Tracking)

```json
"matomo": {
  "urlBase": "https://matomo.common.smart-village.app",
  "siteId": 11
}
```

- Konfiguration für datenschutzkonformes Besuchertracking via Matomo

---

### 📍 locationService

```json
"locationService": {
  "defaultAlternativePosition": {
    "lat": 50.569494,
    "lng": 7.285771
  }
}
```

- Fallback-Koordinaten, falls der Nutzer keinen Standort freigibt

---

### 🚌 busBb

```json
"busBb": {
  "uri": "https://v2.rlp-bus.smart-village.app/graphql",
  "v2": {
    "areaId": 40842
  },
  "initialFilter": [
    "search",
    "aToZ"
  ],
  "isMultiCity": true
}
```

- Einbindung des ÖPNV-Angebots für mehrere Städte/Gemeinden

---

### 🚀 onboarding

```json
"onboarding": true
```

- Wenn `true`, wird ein Onboarding für neue Nutzer aktiviert

---

### 🗑️ wasteAddresses

```json
"wasteAddresses": {
  "isInputAutoFocus": true,
  "twoStep": true
}
```

- Steuerung der Adresssuche für Müllkalender

> Beispieldarstellung der Müllkalender-Suche:  
> ![Platzhalter-Bild](waste-placeholder.png)

---

### 🧩 widgets

Steuern die Anzeige von Mini-Modulen auf der Startseite.

```json
"widgets": [
  "weather",
  {
    "widgetName": "event",
    "text": "Events"
  },
  {
    "widgetName": "custom",
    "text": "Orte",
    "additionalProps": {
      "iconName": "location",
      "accessibilityLabel": "Orte",
      "routeName": "TilesScreen",
      "params": {
        "title": "Stadt und Ortsgemeinden",
        "staticJsonName": "stadt-ortsgemeinden",
        "rootRouteName": "Stadt und Ortsgemeinden"
      }
    }
  }
]
```

> Darstellung eines Event-Widgets:  
> ![Platzhalter-Bild](widget-placeholder.png)

---

### 📝 Hinweis

Alle Werte können über das Admin-Backend angepasst und bei Bedarf versioniert werden.  
Stimmen Sie sich vor größeren Änderungen mit dem technischen Team ab.


### 2.  `Home Carousel`  

tbd.
