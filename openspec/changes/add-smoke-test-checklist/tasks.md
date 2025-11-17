# Implementation Tasks: Smoke-Test-Checkliste

## 0. Git-Workflow Setup

### 0.1 Branch erstellen

- [ ] Feature-Branch erstellen: `git checkout -b feature/smoke-test-checklist`
- [ ] Branch auf GitHub pushen: `git push -u origin feature/smoke-test-checklist`

### 0.2 Commit-Strategie

**Nach jedem Abschnitt committen:**
- [ ] Nach 1.1: `docs: add smoke-tests main documentation`
- [ ] Nach 1.2: `docs: add prioritized test checklist`
- [ ] Nach 1.3: `docs: add detailed test cases per module`
- [ ] Nach 1.4: `docs: add test report template`
- [ ] Nach 2.1: `docs: integrate smoke tests in mkdocs`
- [ ] Nach 2.2: `docs: add cross-references to smoke tests`
- [ ] Nach 3.3: `docs: update smoke tests based on feedback`
- [ ] Nach 4.1: `docs: finalize smoke-test documentation`

### 0.3 Pull Request

- [ ] PR erstellen mit Template
- [ ] Review-Team zuweisen
- [ ] Feedback einarbeiten
- [ ] Nach Approval mergen

## 1. Dokumentation erstellen

### 1.1 Hauptdokumentation: smoke-tests.md

- [ ] Datei `docs/dev/smoke-tests.md` erstellen
- [ ] Einleitung schreiben (Was sind Smoke Tests? Warum wichtig?)
- [ ] Test-Durchführung dokumentieren (Wann, Wer, Wie)
- [ ] Allgemeine Best Practices

### 1.2 Priorisierte Checkliste erstellen

- [ ] Priorität 1: Kritische Basisfunktionen (P1)
  - [ ] App-Intro & Onboarding (2 Testfälle)
  - [ ] Navigation (3 Testfälle)
  - [ ] Nachrichten/Informationen (4 Testfälle)
  - [ ] Veranstaltungen (4 Testfälle)
  - [ ] Suche (3 Testfälle)
  - [ ] Push-Benachrichtigungen (2 Testfälle)
  - [ ] Einstellungen (3 Testfälle)

- [ ] Priorität 2: Interaktive Module (P2)
  - [ ] Merkliste/Favoriten (3 Testfälle)
  - [ ] Mängelmelder (5 Testfälle)
  - [ ] Abfallkalender (3 Testfälle)

- [ ] Priorität 3: Erweiterte Features (P3)
  - [ ] Karten & POIs (4 Testfälle)
  - [ ] Externe Integrationen (je nach Setup)

### 1.3 Testfälle pro Modul ausarbeiten

Für jedes Modul:

#### 1.3.1 App-Intro

- [ ] Testfall 1: Intro-Screens werden beim ersten Start angezeigt
- [ ] Testfall 2: Skip-Funktion funktioniert, Intro kann übersprungen werden

#### 1.3.2 Navigation

- [ ] Testfall 1: Drawer-Navigation öffnet und schließt korrekt (falls aktiviert)
- [ ] Testfall 2: Tabbar-Navigation zeigt alle konfigurierten Items (falls aktiviert)
- [ ] Testfall 3: Navigation zu allen Hauptbereichen funktioniert

#### 1.3.3 Nachrichten/Informationen

- [ ] Testfall 1: Nachrichten-Liste lädt und zeigt aktuelle Artikel
- [ ] Testfall 2: Detailansicht eines Artikels öffnet mit allen Inhalten
- [ ] Testfall 3: Kategoriefilter funktioniert (falls aktiviert)
- [ ] Testfall 4: Teilen-Funktion funktioniert (Social Media, Apps)

#### 1.3.4 Veranstaltungen

- [ ] Testfall 1: Veranstaltungsliste lädt und zeigt aktuelle Events
- [ ] Testfall 2: Kalenderansicht zeigt Termine korrekt
- [ ] Testfall 3: Detailansicht mit allen Informationen (Datum, Ort, Beschreibung)
- [ ] Testfall 4: Filter nach Kategorien/Zeitraum funktioniert

#### 1.3.5 Suche

- [ ] Testfall 1: Suchfeld ist erreichbar und funktioniert
- [ ] Testfall 2: Suchergebnisse werden angezeigt (min. 1 Ergebnis)
- [ ] Testfall 3: Suche über mehrere Content-Typen (News, Events, POIs)

#### 1.3.6 Push-Benachrichtigungen

- [ ] Testfall 1: Push-Registrierung beim ersten Start (Permission-Dialog)
- [ ] Testfall 2: Test-Push wird empfangen und angezeigt (via CMS)

#### 1.3.7 Einstellungen

- [ ] Testfall 1: Einstellungen-Bildschirm öffnet
- [ ] Testfall 2: Push-Einstellungen können geändert werden
- [ ] Testfall 3: App-Informationen werden angezeigt (Version, Impressum)

#### 1.3.8 Merkliste/Favoriten

- [ ] Testfall 1: Inhalt kann als Favorit markiert werden (Stern/Herz)
- [ ] Testfall 2: Merkliste zeigt gespeicherte Inhalte
- [ ] Testfall 3: Favorit kann wieder entfernt werden

#### 1.3.9 Mängelmelder

- [ ] Testfall 1: Mängelmelder-Formular öffnet
- [ ] Testfall 2: Foto kann aufgenommen/hochgeladen werden
- [ ] Testfall 3: Standort wird automatisch erfasst oder kann gewählt werden
- [ ] Testfall 4: Meldung kann abgesendet werden
- [ ] Testfall 5: Bestätigung nach erfolgreichem Versand

#### 1.3.10 Abfallkalender

- [ ] Testfall 1: Kalenderansicht zeigt Abfuhrtermine
- [ ] Testfall 2: Adresse/PLZ kann eingegeben werden (falls konfiguriert)
- [ ] Testfall 3: Push-Erinnerungen können aktiviert werden

#### 1.3.11 Karten

- [ ] Testfall 1: Kartenansicht lädt und zeigt Standort
- [ ] Testfall 2: POIs werden als Marker angezeigt
- [ ] Testfall 3: Marker-Details öffnen bei Tap
- [ ] Testfall 4: Zoom und Pan funktionieren

### 1.4 Test-Report-Template erstellen

- [ ] Template-Datei `docs/dev/test-report-template.md` erstellen
- [ ] Felder definieren:
  - [ ] Datum & Uhrzeit
  - [ ] Tester-Name
  - [ ] App-Version
  - [ ] Test-Umgebung (Staging/Production)
  - [ ] Getestete Module (P1/P2/P3)
  - [ ] Testergebnisse (Pass/Fail pro Testfall)
  - [ ] Gefundene Bugs
  - [ ] Anmerkungen
- [ ] Beispiel-Report als Referenz

## 2. Integration in Dokumentation

### 2.1 MkDocs-Konfiguration

- [ ] `mkdocs.yml` erweitern (Navigation)
- [ ] Smoke Tests unter "Entwicklung" einordnen
- [ ] Cross-Links zu anderen Dev-Docs

### 2.2 Cross-References erstellen

- [ ] Link von `docs/dev/setup.md` zu Smoke Tests
- [ ] Link von `docs/dev/testing.md` (falls vorhanden)
- [ ] Verweis auf Modul-Beschreibungen (`yml/*.yml`)

## 3. Review & Feedback

### 3.1 Team-Review

- [ ] Checkliste mit QA-Team reviewen
- [ ] Feedback von Entwicklern einholen
- [ ] Product Owner Approval

### 3.2 Pilot-Test durchführen

- [ ] Einen vollständigen Smoke-Test durchführen
- [ ] Zeitaufwand messen (P1, P1+P2, P1+P2+P3)
- [ ] Test-Report ausfüllen
- [ ] Lessons Learned dokumentieren

### 3.3 Anpassungen basierend auf Feedback

- [ ] Testfälle anpassen (zu detailliert/zu vage?)
- [ ] Priorisierung überprüfen
- [ ] Zeitschätzungen korrigieren
- [ ] Template verbessern

## 4. Finalisierung

### 4.1 Dokumentation finalisieren

- [ ] Alle Markdown-Linting-Fehler beheben
- [ ] Screenshots/Diagramme hinzufügen (optional)
- [ ] Formatierung prüfen

### 4.2 Freigabe & Deployment

- [ ] Final Approval von Stakeholdern
- [ ] Merge in main branch
- [ ] MkDocs neu bauen und deployen
- [ ] Team über neue Smoke-Test-Checkliste informieren

## 5. Nacharbeiten (Optional)

### 5.1 Schulung & Onboarding

- [ ] Kurze Schulung für Tester
- [ ] Walkthrough der Checkliste
- [ ] Q&A Session

### 5.2 Monitoring & Iteration

- [ ] Nach 1 Woche: Feedback von Testern sammeln
- [ ] Nach 1 Monat: Review der Checkliste
- [ ] Kontinuierliche Verbesserung basierend auf Nutzung

## Progress Tracking

**Phase 0 (Git-Workflow):** 0/11 Tasks
**Phase 1 (Dokumentation):** 0/32 Tasks
**Phase 2 (Integration):** 0/3 Tasks
**Phase 3 (Review):** 0/7 Tasks
**Phase 4 (Finalisierung):** 0/4 Tasks
**Phase 5 (Nacharbeiten):** 0/3 Tasks

**Gesamt:** 0/60 Tasks (0%)## Timeline

- **Tag 0:** Phase 0 (Git-Workflow Setup)
- **Tag 1-2:** Phase 1 (Dokumentation erstellen, Commits nach Abschnitten)
- **Tag 2:** Phase 2 (Integration, Final Commit)
- **Tag 3:** Phase 3 (Review & Pilot-Test, Feedback-Commit)
- **Tag 3-4:** Phase 4 (Finalisierung, PR erstellen)
- **Woche 1-2:** Phase 5 (Nacharbeiten nach Merge)

**Geschätzte Gesamtdauer:** 3-4 Tage (+ laufende Iteration)

## Git-Workflow Summary

1. Branch: `feature/smoke-test-checklist`
2. Commits: Nach jedem Dokumentations-Abschnitt
3. Push: Regelmäßig während der Arbeit
4. PR: Am Ende für Team-Review
5. Merge: Nach Approval durch Team
