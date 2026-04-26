# Change: Smoke-Test-Checkliste für App-Updates

**Change ID:** `add-smoke-test-checklist`
**Status:** DRAFT
**Created:** 2025-11-17
**Owner:** Smart Village Solutions

## Problem Statement

Nach App-Updates (neue Version, Feature-Deployment, Bug-Fixes) gibt es aktuell keine systematische Checkliste für manuelle Smoke Tests. Tester müssen ad-hoc entscheiden, welche Funktionen getestet werden sollen, was zu inkonsistenten Tests und potenziell übersehenen Problemen führt.

**Aktuell:**
- Keine dokumentierte Test-Strategie für Updates
- Unsicherheit, welche Module/Funktionen prioritär zu testen sind
- Keine Unterscheidung zwischen kritischen und optionalen Tests
- Kein einheitliches Vorgehen zwischen verschiedenen Testern

**Ziel:**
- Klare, priorisierte Checkliste für Smoke Tests
- Abdeckung aller kritischen App-Funktionen
- Zeiteffiziente Test-Durchführung (30-60 Minuten)
- Reproduzierbare und konsistente Test-Ergebnisse

## What Changes

### Neue Dokumentation

**Datei:** `docs/dev/smoke-tests.md`

Enthält:
1. **Einleitung & Zweck der Smoke Tests**
2. **Test-Durchführung** (Wann, Wer, Wie)
3. **Priorisierte Test-Checkliste** nach Modulen
4. **Test-Dokumentation** (Template für Test-Reports)

### Test-Kategorien

#### Priorität 1: Kritische Basisfunktionen (MUSS)
- App-Start & Navigation
- Content-Abruf (Nachrichten, Veranstaltungen)
- Push-Benachrichtigungen
- Such-Funktion
- Einstellungen

#### Priorität 2: Interaktive Module (SOLLTE)
- Mängelmelder
- Feedback-Formular
- Merkliste/Favoriten
- Abfallkalender

#### Priorität 3: Erweiterte Features (KANN)
- Karten & POIs
- Externe Integrationen
- Spezial-Module (je nach Kommune)

### Module-Matrix

Für jedes aktive Modul aus `city_app.yml`:

| Modul | Priorität | Testfälle | Geschätzte Dauer |
|-------|-----------|-----------|------------------|
| App-Intro | P1 | 2 | 2 min |
| Navigation | P1 | 3 | 3 min |
| Nachrichten | P1 | 4 | 5 min |
| Veranstaltungen | P1 | 4 | 5 min |
| Suche | P1 | 3 | 3 min |
| Push-Benachrichtigungen | P1 | 2 | 3 min |
| Einstellungen | P1 | 3 | 3 min |
| Merkliste/Favoriten | P2 | 3 | 3 min |
| Mängelmelder | P2 | 5 | 8 min |
| Abfallkalender | P2 | 3 | 3 min |
| Karten | P3 | 4 | 5 min |

**Gesamt P1:** ~24 Minuten
**Gesamt P1+P2:** ~41 Minuten
**Gesamt P1+P2+P3:** ~46 Minuten

## Why This Approach

### Vorteile

1. **Systematisch:** Reproduzierbare Tests mit klaren Kriterien
2. **Priorisiert:** Kritische Funktionen zuerst, optionale Features später
3. **Zeiteffizient:** Klare Zeitvorgaben ermöglichen Planung
4. **Modular:** An individuelle App-Konfiguration anpassbar
5. **Dokumentiert:** Test-Reports ermöglichen Nachvollziehbarkeit

### Ausrichtung an bestehender Architektur

- Basiert auf der Modul-Struktur aus `city_app.yml`
- Nutzt vorhandene Modul-Beschreibungen (`yml/*.yml`)
- Integriert sich in bestehende Dev-Dokumentation
- Kompatibel mit CI/CD-Workflows (zukünftig)

## Implementation Scope

### In Scope

- ✅ Dokumentation der Smoke-Test-Checkliste
- ✅ Priorisierung nach Modulen
- ✅ Testfall-Beschreibungen für alle aktiven Module
- ✅ Template für Test-Reports
- ✅ Best Practices für manuelle Tests

### Out of Scope

- ❌ Automatisierte Tests (separates Proposal)
- ❌ CI/CD Integration (separates Proposal)
- ❌ Performance-Tests
- ❌ Security-Tests
- ❌ Barrierefreiheits-Tests (separate Checkliste)

## Affected Components

- **Neue Datei:** `docs/dev/smoke-tests.md` (Hauptdokumentation)
- **Optional:** `docs/dev/test-report-template.md` (Vorlage für Reports)
- **Update:** `docs/dev/setup.md` (Link zu Smoke Tests)
- **Update:** `mkdocs.yml` (Navigation erweitern)

## Dependencies & Requirements

### Voraussetzungen

- ✅ Modul-Beschreibungen existieren (`yml/*.yml`)
- ✅ city_app.yml definiert aktive Module
- ✅ Dokumentations-Struktur vorhanden

### Keine neuen Dependencies

## Open Questions

1. **Frequenz:** Wie oft sollen Smoke Tests durchgeführt werden?
   - Nach jedem Deployment?
   - Vor jedem Release?
   - Wöchentlich/Täglich?

2. **Verantwortlichkeit:** Wer führt die Tests durch?
   - Entwickler vor Merge?
   - QA-Team nach Deployment?
   - Product Owner vor Release?

3. **Test-Umgebung:** Welche Umgebungen sollen getestet werden?
   - Staging only?
   - Production nach Deployment?
   - Beide?

4. **Dokumentation der Ergebnisse:** Wo werden Test-Reports gespeichert?
   - GitHub Issues?
   - Confluence/Wiki?
   - Separate Test-Management-Software?

5. **Module-Spezifität:** Soll es generische oder kommune-spezifische Checklisten geben?
   - Eine Checkliste für alle?
   - Anpassbare Checklisten je Kommune?

## Success Criteria

- ✅ Smoke-Test-Dokumentation ist vollständig
- ✅ Alle 12 aktiven Module haben Test-Fälle
- ✅ Priorisierung ist klar definiert (P1/P2/P3)
- ✅ Zeitschätzungen für jeden Test vorhanden
- ✅ Test-Report-Template ist nutzbar
- ✅ Dokumentation ist in MkDocs integriert
- ✅ Mindestens ein erfolgreicher Test-Durchlauf dokumentiert

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Checkliste wird nicht genutzt | Hoch | Schulung, Integration in Workflow |
| Zu zeitaufwendig | Mittel | Priorisierung (nur P1 bei Zeitdruck) |
| Module-Änderungen machen Checkliste obsolet | Mittel | Regelmäßige Reviews der Checkliste |
| Unklare Verantwortlichkeit | Hoch | Explizite Zuweisung im Team-Agreement |

## Timeline

- **Phase 0 (Setup):** 0.5 Tage
    - Feature-Branch erstellen: `feature/smoke-test-checklist`
    - Git-Workflow vorbereiten

- **Phase 1 (Dokumentation):** 1-2 Tage
    - Checkliste erstellen
    - Testfälle beschreiben
    - Template entwickeln
    - **Commit nach jedem Abschnitt**

- **Phase 2 (Review & Feedback):** 1 Tag
    - Team-Review
    - Anpassungen basierend auf Feedback
    - **Commit nach Anpassungen**

- **Phase 3 (Integration):** 0.5 Tage
    - MkDocs-Integration
    - Cross-Links zu anderen Docs
    - **Final Commit**

- **Phase 4 (Pull Request):** 0.5 Tage
    - PR erstellen für Team-Review
    - Feedback einarbeiten
    - Merge nach Approval

**Gesamt:** 3-4 Tage

## Approval

- [ ] Product Owner
- [ ] QA Lead
- [ ] Development Team Lead

## Related Changes

- Zukünftig: `add-automated-smoke-tests` (CI/CD Integration)
- Zukünftig: `add-e2e-test-suite` (Umfassende automatisierte Tests)
- Referenz: `add-module-descriptions-system` (Modul-Dokumentation als Basis)
