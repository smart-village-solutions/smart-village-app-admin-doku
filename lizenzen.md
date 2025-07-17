# Integration von Lizenzinformationen

Um den Anforderungen der GPLv3 sowie gängigen Transparenz- und Compliance-Standards gerecht zu werden, sollten in der App **Lizenzinformationen** bereitgestellt werden. Diese Seite beschreibt, wie Sie dies korrekt umsetzen.



## Wo sollten die Lizenzinformationen erscheinen?

Wir empfehlen, die Lizenzinformationen **im Bereich „Infos“ oder „Mehr“** der App bereitzustellen – dort, wo auch das Impressum oder die Datenschutzerklärung zu finden sind. Technisch wird dafür ein zusätzlicher Menüpunkt in der entsprechenden JSON-Konfiguration eingefügt.



## Menüpunkt in der App-Konfiguration hinzufügen

Fügen Sie in der Konfigurationsdatei des Bereichs folgenden Eintrag hinzu:

```json
...},
{
  "title": "Softwarelizenzen",
  "routeName": "NestedInfo",
  "params": {
    "title": "Softwarelizenzen",
    "name": "softwarelizenzen"
  }
},
...
```



## Erstellung der Datei `softwarelizenzen`

Diese JSON-Datei beschreibt den Inhalt der Seite, auf die der Menüpunkt verweist. Sie kombiniert einleitenden Text mit einer Liste von Unterpunkten:

```json
{
  "content": "softwarelizenzenContent",
  "title": "",
  "children": [
    {
      "title": "GNU GPL-3.0",
      "routeName": "Html",
      "params": {
        "title": "GNU GPL-3.0",
        "query": "publicHtmlFile",
        "queryVariables": {
          "name": "gnu-gpl-30"
        },
        "subQuery": "false"
      }
    },
    {
      "title": "Softwarepakete der mobilen App",
      "routeName": "Web",
      "params": {
        "title": "Softwarepakete der mobilen App",
        "webUrl": "https://lizenz-generator-22161c.usercontent.opencode.de/App.html"
      }
    },
    {
      "title": "Softwarepakete des App-Servers",
      "routeName": "Web",
      "params": {
        "title": "Softwarepakete des App-Servers",
        "webUrl": "https://lizenz-generator-22161c.usercontent.opencode.de/Mainserver.html"
      }
    },
    {
      "title": "Softwarepakete des Redaktionssystems",
      "routeName": "Web",
      "params": {
        "title": "Softwarepakete des Redaktionssystems",
        "webUrl": "https://lizenz-generator-22161c.usercontent.opencode.de/CMS.html"
      }
    },
    {
      "title": "Identitätsmanagement",
      "routeName": "Web",
      "params": {
        "title": "Identitätsmanagement",
        "webUrl": "https://github.com/keycloak/keycloak/blob/main/LICENSE.txt"
      }
    },
    {
      "title": "Karte",
      "routeName": "Html",
      "params": {
        "title": "Karte",
        "query": "publicHtmlFile",
        "queryVariables": {
          "name": "lizenzen-karte"
        },
        "subQuery": "false"
      }
    }
  ]
}
```



## Inhalt der Datei `softwarelizenzenContent`

Diese zusätzliche "statische Seite" bietet den einleitenden Text:

```html
<p>Diese App basiert auf der quelloffenen Smart Village App,
die durch die Stadt Bad Belzig unter der GNU GPL-3.0 lizensiert
wurde.</p>

<p>Im Folgenden findest du den Lizenztext der App sowie eine
Übersicht der genutzten Software-Bibliotheken und ihrer Lizenzen
(bei mehrfachen Lizenzoptionen gilt die zur GPLv3 kompatible Lizenz).</p>
```

Die Datei wird unter dem Namen `softwarelizenzenContent` im CMS als statische Seite hinterlegt.



## Inhalt der Datei `gnu-gpl-30`

Diese zusätzliche "statische Seite" enthält den vollständigen [Lizenztext der GNU GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.de.html) oder verlinkt darauf:

```html
<p>Die App steht unter der GNU General Public License v3.0. Den vollständigen Lizenztext findest du hier:</p>
<p><a href="https://www.gnu.org/licenses/gpl-3.0.de.html" target="_blank" rel="noopener noreferrer">https://www.gnu.org/licenses/gpl-3.0.de.html</a></p>
```

Die Datei wird unter dem Namen `gnu-gpl-30` im CMS als statische Seite hinterlegt.




##  Webansichten der Lizenzgeneratoren

Die Web-URLs zeigen stets die aktuellste Liste der verwendeten Bibliotheken. Diese werden vom Smart Village App Projekt regelmäßig gepflegt. Eine manuelle Einpflege wird **nicht empfohlen**, da sich die Abhängigkeiten mit jeder App-Version ändern können.


## Weitere optionale Inhalte

### Beispiel „Karte“

Die Datei `lizenzen-karte` könnte z. B. so aussehen:

```html
<h3>Lizenzen der Karte</h3>
<p>Diese App nutzt Drittkomponenten und Daten für die Kartendarstellung:</p>

<ul>
  <li>
    <strong>openstreetmap-tile-server</strong><br>
    © 2019 Alexander Overvoorde – lizenziert unter der <a href="https://www.apache.org/licenses/LICENSE-2.0" target="_blank">Apache License 2.0</a>
  </li>
  <li>
    <strong>OpenStreetMap-Daten</strong><br>
    © OpenStreetMap-Mitwirkende – bereitgestellt unter der <a href="https://www.openstreetmap.org/copyright" target="_blank">Open Database License (ODbL) 1.0</a>
  </li>
</ul>
```

### Beispiel "Identitätsmanagement (Keycloak)"

Falls die App eine Benutzeranmeldung oder andere Funktionen mit Keycloak nutzt, sollte die verwendete Software und ihre Lizenz transparent gemacht werden.

### Eintrag in der JSON `softwarelizenzen`

Füge diesen Block innerhalb des `children`-Arrays ein:

```json
{
  "title": "Identitätsmanagement",
  "routeName": "Web",
  "params": {
    "title": "Identitätsmanagement",
    "webUrl": "[https://github.com/keycloak/keycloak/tree/main?tab=Apache-2.0-1-ov-file#readme](https://github.com/keycloak/keycloak/blob/main/LICENSE.txt)"
  }
}
```

### Hintergrund

Keycloak ist ein Open-Source-Projekt, das unter der **Apache License 2.0** steht. Da Keycloak ein eigenständiger und nicht immer genutzter Bestandteil der App-Infrastruktur ist (z. B. für rollenbasierten Zugriff, redaktionelle Workflows oder SSO), wird der Eintrag nur bei aktiver Nutzung empfohlen.

Die Lizenzseite von Keycloak auf GitHub ist über den oben genannten Link direkt erreichbar und stellt die Lizenzbedingungen transparent dar.


### Alternativ: Statische Seite (optional)

Falls du statt der WebView eine eigene statische HTML-Seite anlegen möchtest, könnte der Inhalt beispielsweise so aussehen:

```html
<h3>Lizenz für das Identitätsmanagement</h3>
<p>Diese App nutzt zur Benutzerverwaltung gegebenenfalls <strong>Keycloak</strong>, eine Open-Source-Identitäts- und Zugriffsverwaltungslösung, die unter der Apache License 2.0 steht.</p>
<p>Weitere Informationen und die vollständige Lizenz findest du hier:</p>
<p><a href="https://github.com/keycloak/keycloak/tree/main?tab=Apache-2.0-1-ov-file#readme" target="_blank" rel="noopener noreferrer">https://github.com/keycloak/keycloak/tree/main</a></p>
```

Dann müsste dein `children`-Eintrag entsprechend mit `routeName: "Html"` und einer `queryVariables.name` wie `lizenzen-identitaet` referenzieren.
