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

### `Liveticker (laufender Text) auf dem Homescreen der Smart Village App`
Static Content name: `homeLiveTicker`

**Verfügbar ab Version 4.1.1**

#### Ziel

Ein farblich hervorgehobener, horizontal durchlaufender Text („Liveticker“) soll prominent auf dem Homescreen der App angezeigt werden, um wichtige Informationen schnell sichtbar zu machen.


#### Einrichtung im Main Server

1. Navigiere im Main Server zu:
`Settings > Static Contents`


2. Lege dort einen neuen Static Content an mit folgenden Einstellungen:

| Feld     | Wert         |
|----------|--------------|
| Name     | `homeLiveTicker` |
| Version  | *(frei lassen)* |
| Data type | `JSON`         |
| Content  | Siehe Code-Snippet (reinkopieren) |

#### Beispiel-JSON für Content-Feld:

```json
{
  "text": "Smart Village App ❤️",
  "liveTickerSettings": {
    "speed": 0.5,
    "style": {
      "backgroundColor": "#E5BFF7",
      "paddingVertical": 20 // optional
    }
  }
}
```

#### Erläuterungen zu den Einstellungen

- `text`
Der sichtbare Text des Livetickers.  
Optional kann HTML verwendet werden (z. B. `<b>` oder `<i>`).  
⚠Vorsicht bei komplexeren HTML-Strukturen – **keine Skripte einbetten.**



- `speed`
Legt die Laufgeschwindigkeit fest:

| Wert | Beschreibung             |
|------|--------------------------|
| 0.0  | kein Lauftext (steht still) |
| 1.0  | Standardgeschwindigkeit  |
| 2.0  | sehr schnell             |

**Wichtig:** Verwende einen **Punkt** als Dezimaltrennzeichen, **kein Komma**.

- `style.backgroundColor`
Hex-Code zur Festlegung der Hintergrundfarbe des Laufbandes (z. B. `#E5BFF7`).  
Kann frei gewählt werden, sollte aber aus Gründen der **Barrierefreiheit kontrastreich** sein.

- `style.paddingVertical`
Vertikaler Innenabstand *(Padding)* innerhalb des Laufbandes in Pixeln.  
**Der Wert `20` ist Standard und aus UI/UX-Sicht empfohlen.**


#### Hinweise zur Nutzung

- Der Ticker erscheint auf dem **Homescreen unterhalb des App-Headers**  
  und **oberhalb des Titelbilds/Karussells bzw. der Widget-Leiste**.

- Der Ticker ist **nur sichtbar**, wenn er **korrekt angelegt** wurde.  
  Bei **fehlerhaftem JSON-Code** wird **nichts angezeigt**.

- Änderungen im Ticker sind in der Regel **innerhalb weniger Sekunden** in der App sichtbar.

- **Lange Texte** werden **nicht abgeschnitten**, sondern **fortlaufend angezeigt** –  
  sie **laufen automatisch durch**.

### `Global Settings`  
Type: *json*

Attribute:

- Bildrechte / Copyright anzeigen <br>
Code: "showImageRights": boolean -> true / false <br>
Erklärung: In den Bildern wird ein "Copyright" des Rechteinhabers angezeigt <br>
Beispiel:
![Logo](/smart-village-app-admin-doku/images/imagerights.jpg)

- Filter <br>
Code: <br>
{ <br>
  "filter": { <br>
    "news": false, <br>
    "events": true, <br>
    "eventLocations": true <br>
  }, <br>
Erklärung: <br>
Beispiel: <br>


### `Home Carousel`  

tbd.
