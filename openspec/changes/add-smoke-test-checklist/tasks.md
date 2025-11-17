# Implementation Tasks: Smoke-Test-Checkliste

## 0. Git-Workflow Setup

### 0.1 Branch erstellen

- [x] Feature-Branch erstellen: `git checkout -b feature/smoke-test-checklist`
- [x] Branch auf GitHub pushen: `git push -u origin feature/smoke-test-checklist`

### 0.2 Commit-Strategie

**Nach jedem Abschnitt committen:**
- [x] Nach 1.1-1.4: `docs: add smoke-tests main documentation` (Commit: 2265bef)
- [x] Nach 2.1: `docs: integrate smoke tests in mkdocs` (Commit: fb35f4c)
- [x] Nach 2.2: `docs: add cross-references to smoke tests` (Commit: 52f6896)
- [x] OpenSpec Proposal: `docs: add openspec proposal for smoke-test checklist` (Commit: 058b093)
- [ ] Nach 3.3: `docs: update smoke tests based on feedback`
- [ ] Nach 4.1: `docs: finalize smoke-test documentation`

### 0.3 Pull Request

- [x] PR erstellen mit Template (PR #16)
- [ ] Review-Team zuweisen
- [ ] Feedback einarbeiten
- [ ] Nach Approval mergen

## 1. Dokumentation erstellen

### 1.1 Hauptdokumentation: smoke-tests.md

- [x] Datei `docs/dev/smoke-tests.md` erstellen
- [x] Einleitung schreiben (Was sind Smoke Tests? Warum wichtig?)
- [x] Test-Durchführung dokumentieren (Wann, Wer, Wie)
- [x] Allgemeine Best Practices

### 1.2 Priorisierte Checkliste erstellen

- [x] Priorität 1: Kritische Basisfunktionen (P1)
  - [x] App-Intro & Onboarding (2 Testfälle)
  - [x] Navigation (3 Testfälle)
  - [x] Nachrichten/Informationen (4 Testfälle)
  - [x] Veranstaltungen (4 Testfälle)
  - [x] Suche (3 Testfälle)
  - [x] Push-Benachrichtigungen (2 Testfälle)
  - [x] Einstellungen (3 Testfälle)

- [x] Priorität 2: Interaktive Module (P2)
  - [x] Merkliste/Favoriten (3 Testfälle)
  - [x] Mängelmelder (5 Testfälle)
  - [x] Abfallkalender (3 Testfälle)

- [x] Priorität 3: Erweiterte Features (P3)
  - [x] Karten & POIs (4 Testfälle)
  - [x] Externe Integrationen (je nach Setup)

### 1.3 Testfälle pro Modul ausarbeiten

Für jedes Modul:

#### 1.3.1 App-Intro

- [x] Testfall 1: Intro-Screens werden beim ersten Start angezeigt
- [x] Testfall 2: Skip-Funktion funktioniert, Intro kann übersprungen werden

#### 1.3.2 Navigation

- [x] Testfall 1: Drawer-Navigation öffnet und schließt korrekt (falls aktiviert)
- [x] Testfall 2: Tabbar-Navigation zeigt alle konfigurierten Items (falls aktiviert)
- [x] Testfall 3: Navigation zu allen Hauptbereichen funktioniert

#### 1.3.3 Nachrichten/Informationen

- [x] Testfall 1: Nachrichten-Liste lädt und zeigt aktuelle Artikel
- [x] Testfall 2: Detailansicht eines Artikels öffnet mit allen Inhalten
- [x] Testfall 3: Kategoriefilter funktioniert (falls aktiviert)
- [x] Testfall 4: Teilen-Funktion funktioniert (Social Media, Apps)

#### 1.3.4 Veranstaltungen

- [x] Testfall 1: Veranstaltungsliste lädt und zeigt aktuelle Events
- [x] Testfall 2: Kalenderansicht zeigt Termine korrekt
- [x] Testfall 3: Detailansicht mit allen Informationen (Datum, Ort, Beschreibung)
- [x] Testfall 4: Filter nach Kategorien/Zeitraum funktioniert

#### 1.3.5 Suche

- [x] Testfall 1: Suchfeld ist erreichbar und funktioniert
- [x] Testfall 2: Suchergebnisse werden angezeigt (min. 1 Ergebnis)
- [x] Testfall 3: Suche über mehrere Content-Typen (News, Events, POIs)

#### 1.3.6 Push-Benachrichtigungen

- [x] Testfall 1: Push-Registrierung beim ersten Start (Permission-Dialog)
- [x] Testfall 2: Test-Push wird empfangen und angezeigt (via CMS)

#### 1.3.7 Einstellungen

- [x] Testfall 1: Einstellungen-Bildschirm öffnet
- [x] Testfall 2: Push-Einstellungen können geändert werden
- [x] Testfall 3: App-Informationen werden angezeigt (Version, Impressum)

#### 1.3.8 Merkliste/Favoriten

- [x] Testfall 1: Inhalt kann als Favorit markiert werden (Stern/Herz)
- [x] Testfall 2: Merkliste zeigt gespeicherte Inhalte
- [x] Testfall 3: Favorit kann wieder entfernt werden

#### 1.3.9 Mängelmelder

- [x] Testfall 1: Mängelmelder-Formular öffnet
- [x] Testfall 2: Foto kann aufgenommen/hochgeladen werden
- [x] Testfall 3: Standort wird automatisch erfasst oder kann gewählt werden
- [x] Testfall 4: Meldung kann abgesendet werden
- [x] Testfall 5: Bestätigung nach erfolgreichem Versand

#### 1.3.10 Abfallkalender

- [x] Testfall 1: Kalenderansicht zeigt Abfuhrtermine
- [x] Testfall 2: Adresse/PLZ kann eingegeben werden (falls konfiguriert)
- [x] Testfall 3: Push-Erinnerungen können aktiviert werden

#### 1.3.11 Karten

- [x] Testfall 1: Kartenansicht lädt und zeigt Standort
- [x] Testfall 2: POIs werden als Marker angezeigt
- [x] Testfall 3: Marker-Details öffnen bei Tap
- [x] Testfall 4: Zoom und Pan funktionieren

### 1.4 Test-Report-Template erstellen

- [x] Template-Datei `docs/dev/test-report-template.md` erstellen (in smoke-tests.md integriert)
- [x] Felder definieren:
  - [x] Datum & Uhrzeit
  - [x] Tester-Name
  - [x] App-Version
  - [x] Test-Umgebung (Staging/Production)
  - [x] Getestete Module (P1/P2/P3)
  - [x] Testergebnisse (Pass/Fail pro Testfall)
  - [x] Gefundene Bugs
  - [x] Anmerkungen
- [x] Beispiel-Report als Referenz

## 2. Integration in Dokumentation

### 2.1 MkDocs-Konfiguration

- [x] `mkdocs.yml` erweitern (Navigation)
- [x] Smoke Tests unter "Entwicklung" einordnen
- [x] Cross-Links zu anderen Dev-Docs

### 2.2 Cross-References erstellen

- [x] Link von `docs/dev/README.md` zu Smoke Tests (neu erstellt)
- [x] Link von smoke-tests.md zu Modul-Beschreibungen
- [x] Verweis auf Modul-Beschreibungen (`yml/*.yml`)

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

**Phase 0 (Git-Workflow):** 9/11 Tasks (82%)
**Phase 1 (Dokumentation):** 32/32 Tasks (100%) ✅
**Phase 2 (Integration):** 3/3 Tasks (100%) ✅
**Phase 3 (Review):** 0/7 Tasks (0%)
**Phase 4 (Finalisierung):** 0/4 Tasks (0%)
**Phase 5 (Nacharbeiten):** 0/3 Tasks (0%)

**Gesamt:** 44/60 Tasks (73%)## Timeline

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
