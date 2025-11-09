# Change: Systematische Erzeugung strukturierter Modulbeschreibungen

## Why

Die Smart Village App besteht aus über 60 verschiedenen Modulen, die dokumentiert werden müssen. Aktuell existieren nur 2 vollständige YAML-Beschreibungen (Nachrichten und Veranstaltungen). Das manuelle Erstellen aller Modulbeschreibungen ist zeitaufwändig und fehleranfällig.

Es wird ein systematischer Ansatz benötigt, um:
- Konsistente Modulbeschreibungen über alle 60+ Module zu erstellen
- Gemeinsame Informationen (wie deployed_in_municipalities, opencode_repository) zentral zu verwalten
- Den Prozess zur Erstellung neuer Modulbeschreibungen zu standardisieren
- Die Pflege und Aktualisierung der Beschreibungen zu vereinfachen

## What Changes

- Template-System für Modulbeschreibungen mit gemeinsamen und individuellen Feldern
- Gemeinsame Daten (global.yml) für alle Module
- Interaktives CLI-Tool zur Modulerstellung mit geführtem Workflow
- Python-Skript zur Generierung vollständiger YAML-Dateien aus Teilinformationen
- **Automatische Registrierung neuer Module in city_app.yml**
- **Git-Workflow mit automatischer Branch-Erstellung und Pull Request**
- Dokumentation des Prozesses für zukünftige Modulbeschreibungen
- Erstellung aller 60+ Modulbeschreibungen gemäß app-module.schema.json

### Betroffene Module (initial zu erstellen):

1. Abfallkalender
2. App-Intro
3. App-Server inkl. Benutzerverwaltung
4. Augmented-Reality
5. Baustellen/Verkehrsstörungen
6. Bilderslider
7. Branchenbuch/Marktplatz
8. Branchenbuch/Wegweiser
9. Bürgerbeteiligung
10. Bund.ID und Keycloak
11. Car-/Bikesharing-Angebote
12. Chatbot
13. CMS
14. Content-Sharing
15. Data Hub
16. Dashboard
17. Datenvisualisierungen
18. Einstellungen
19. Feedback-Formular
20. Fristenmelder
21. Gastro-Angebote
22. Gutscheine
23. Gruppen/Soziales Netzwerk
24. Hinweisgebersystem
25. HumHub
26. Karten (inkl. Standortnutzung)
27. Mängelmelder
28. Mängelmelder (einfach)
29. Mängelmelder (mit Schnittstelle)
30. Merkliste
31. Merkliste/Favoriten
32. Nachrichten/Informationen (✓ bereits vorhanden)
33. Navigation
34. Nutzertracking
35. ÖPNV-Daten (Abfahrtspläne)
36. Open Street Map
37. Persönliches Profil (optional mit Bund.ID)
38. Postfach
39. Produkte und Dienstleistungen
40. Push-Nachrichten
41. Rathaus-Informationssystem
42. Redaktionssystem (CMS) inkl. 50 GB Dateispeicher
43. Schwarzes Brett
44. Service-Links
45. Smartes Trampen
46. Sonstige Seiten
47. Statische Listen/Kacheln
48. Statische Seiten
49. Stellenanzeigen
50. Störer
51. Suche
52. Terminbuchung
53. Treueclub/Vorteilssystem
54. Umfrage-Modul
55. Umfragen
56. Veranstaltungen (✓ bereits vorhanden)
57. Warnmeldungen
58. Wassertemperatur
59. Webview
60. Wetter
61. Widgets
62. Zuständigkeitsfinder

## Impact

### Affected Specs
- Neu: `module-description-workflow` (Prozess zur Modulbeschreibung)
- Neu: `module-template-system` (Template-System)

### Affected Code
- Neu: `yml/global.yml` (Gemeinsame Daten)
- Neu: `yml/modules/` (Verzeichnis für Modul-Teilinformationen)
- Neu: `scripts/create_module.py` (Interaktives Erstellungstool)
- Neu: `scripts/generate_module_yaml.py` (YAML-Generator)
- Erweitert: `validate_schemas.py` (Validierung aller neuen Module)
- **Erweitert: `city_app.yml` (Automatische Modul-Registrierung)**
- **Neu: `.github/PULL_REQUEST_TEMPLATE.md` (PR-Template für Module)**
- Neu: 60 YAML-Dateien in `yml/`

### Benutzer-Impact
- Redakteure können neue Modulbeschreibungen schneller und konsistenter erstellen
- Gemeinsame Informationen müssen nur einmal aktualisiert werden
- Automatische Validierung verhindert Fehler
- **Module werden automatisch in city_app.yml registriert und sind sofort verfügbar**
- **Git-Workflow mit PRs ermöglicht Code-Review vor Integration**
- **CI/CD-Validierung vor Merge in main**

## Breaking Changes

Keine Breaking Changes. Dies ist eine reine Erweiterung der bestehenden Struktur.

## Migration Plan

1. Bestehende Module (nachrichten.yml, veranstaltungen.yml) bleiben unverändert
2. Neue Module werden schrittweise hinzugefügt
3. Template-System ist optional; direkte YAML-Erstellung bleibt möglich
