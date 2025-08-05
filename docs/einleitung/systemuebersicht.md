# Systemübersicht & Komponenten

Die Smart Village App ist kein monolithisches System, sondern ein modular aufgebautes, modernes Software-Ökosystem. Es besteht aus mehreren eigenständigen, aber eng verzahnten Komponenten, die gemeinsam die Funktionsvielfalt der App ermöglichen – sowohl für Bürger:innen als auch für Verwaltungen, Redaktionen und technische Partner.

## Architekturprinzip

Im Zentrum steht eine **Headless-Architektur** mit einer gemeinsamen GraphQL-API („DataHub“), an die alle Frontends und Tools angebunden sind. Inhalte werden zentral gepflegt und stehen plattformübergreifend zur Verfügung – in der nativen App, der Web-App und im CMS.

## Hauptkomponenten im Überblick

### 1. React Native App

- Das zentrale Interface für Bürger:innen auf iOS- und Android-Geräten
- Modular aufgebaut – Module können gezielt aktiviert werden
- Unterstützt Push-Nachrichten, Offline-Nutzung, Lokalisierung u. v. m.

### 2. Tailwind Web-App (in Vorbereitung)

- Leichtgewichtige, barrierearme Web-App mit Fokus auf Performance und Design
- Greift auf dieselbe API wie die mobile App zu
- Ideal für Geräte ohne App Store (z. B. PCs, öffentliche Terminals)

### 3. GraphQL API

- Zentrale Schnittstelle für Datenabfragen und -änderungen
- Einheitliches Datenmodell für alle Clients (App, CMS, Schnittstellen)
- Flexibel erweiterbar mit wenig Overhead

### 4. CMS (Content Management System)

- Webbasiertes Redaktionssystem mit rollenbasierter Rechteverwaltung
- Ermöglicht die Pflege aller Inhalte durch Kommunen, Vereine, Institutionen etc.
- Unterstützt Uploads, mehrsprachige Inhalte, Medien, Verlinkungen etc.

### 5. Rails App-Server (Backend)

- Steuert Geschäftslogik, Validierung, Rechtevergabe und Hintergrunddienste
- Bindeglied zwischen API, Datenbank, Keycloak, MinIO und Drittanbindungen
- Ermöglicht z. B. E-Mail-Versand, Push-Queue, geplante Prozesse

### 6. Keycloak (Authentifizierung)

- Rollenbasiertes OpenID-Connect-System für sichere Logins
- Verwaltung von Redakteur:innen, Admins, Entwickelnden u. a.
- Ermöglicht Mandantenfähigkeit und SSO-Szenarien

### 7. MinIO / S3 (Dateispeicher)

- Speichert Bilder, PDFs, Dokumente u. v. m.
- Integration in CMS und App zur Anzeige und zum Download
- Kompatibel mit gängigen Backup- und CDN-Systemen

### 8. MapTiles-Server

- Bereitstellung von Kartendaten auf Basis von OpenStreetMap
- Grundlage für Module wie den Kunstwanderweg, Mobilität oder Points of Interest

### 9. Monitoring & Logging

- Systemüberwachung mit Tools wie Netdata, Grafana, Sentry oder UptimeRobot
- Ermöglicht verlässlichen Betrieb und schnelle Fehlersuche

### 10. Importer & Schnittstellen

- Automatischer Datenimport aus verschiedenen Quellen, z. B.:
    - OParl (Ratsinformationssysteme)
    - xZuFi / BUS (Verwaltungsleistungen)
    - OpenStreetMap (POI)
    - MoWaS (Katastrophenwarnungen)
- Individuelle Anbindung per Node-RED, n8n oder eigene Skripte

## Warum dieser Aufbau?

Diese Architektur erlaubt eine modulare, skalierbare und zukunftssichere Weiterentwicklung – sowohl auf technischer als auch auf organisatorischer Ebene. Jede Kommune kann entscheiden, welche Komponenten sie nutzen oder betreiben möchte – im Selbstbetrieb oder als „Open Source as a Service“.

Die klare Trennung der Schichten ermöglicht:

- **Unabhängigkeit einzelner Komponenten** (z. B. CMS-Update ohne App-Update)
- **Einfache Erweiterbarkeit** für neue Module oder Schnittstellen
- **Transparenz und Wartbarkeit** durch Open Source und Standardtechnologien
