# Smoke Tests für App-Updates

## Einleitung

Smoke Tests (auch Sanity Tests genannt) sind schnelle, grundlegende Tests, die nach jedem App-Update durchgeführt werden sollten, um sicherzustellen, dass die wichtigsten Funktionen der App weiterhin funktionieren. Sie dienen als erste Qualitätskontrolle vor umfangreicheren Tests.

### Was sind Smoke Tests?

Smoke Tests überprüfen die **kritischsten Funktionen** einer Anwendung mit minimalem Aufwand. Der Name stammt aus der Hardware-Entwicklung: Wenn beim Einschalten eines Geräts Rauch aufsteigt, ist ein grundlegendes Problem vorhanden.

In der Software-Entwicklung bedeutet das:
- ✅ **Schnell:** 30-60 Minuten für vollständige Durchführung
- ✅ **Fokussiert:** Nur kritische Funktionen werden getestet
- ✅ **Go/No-Go:** Entscheidung, ob weitere Tests sinnvoll sind

### Warum sind Smoke Tests wichtig?

Nach jedem Update (neue Features, Bug-Fixes, Konfigurationsänderungen) können unerwartete Probleme auftreten:

- **Regressionsfehler:** Neue Änderungen brechen bestehende Funktionen
- **Integrationsprobleme:** Module interagieren nicht mehr korrekt
- **Konfigurationsfehler:** Falsche Einstellungen führen zu Fehlfunktionen
- **Deployment-Probleme:** Build oder Deployment schlägt fehl

Smoke Tests erkennen diese Probleme **frühzeitig**, bevor umfangreichere Tests durchgeführt werden.

## Test-Durchführung

### Wann sollten Smoke Tests durchgeführt werden?

- ✅ **Nach jedem Deployment** (Staging oder Production)
- ✅ **Vor jedem Release** (finale Freigabe)
- ✅ **Nach größeren Updates** (neue Features, Breaking Changes)
- ✅ **Nach Konfigurationsänderungen** (CMS, App-Server)
- ✅ **Täglich/Wöchentlich** (automatisierte Monitoring-Tests)

### Wer führt Smoke Tests durch?

Je nach Team-Struktur:

- **Entwickler:** Vor Merge/Deployment als Selbstcheck
- **QA-Team:** Nach Deployment auf Staging
- **Product Owner:** Vor Release-Freigabe
- **Operations:** Nach Production-Deployment

### Wie werden Smoke Tests durchgeführt?

1. **Test-Gerät vorbereiten:**
   - Aktuelles iOS/Android-Gerät oder Emulator
   - App-Version überprüfen (richtige Version installiert?)
   - Netzwerkverbindung prüfen

2. **Test-Umgebung auswählen:**
   - **Staging:** Für Pre-Release-Tests
   - **Production:** Nach Live-Deployment

3. **Checkliste abarbeiten:**
   - Mit Priorität 1 (P1) starten
   - Bei P1-Fehlern: Tests stoppen, Fehler melden
   - Bei P1-Erfolg: P2 und P3 nach Zeitbudget

4. **Ergebnisse dokumentieren:**
   - Test-Report ausfüllen (siehe [Template](#test-report-template))
   - Bugs in Issue-Tracker eintragen
   - Team informieren

## Priorisierte Test-Checkliste

Die Checkliste ist in drei Prioritätsstufen unterteilt:

### Priorität 1: Kritische Basisfunktionen (P1) 🔴

**MUSS getestet werden** - Diese Funktionen sind essentiell für die App-Nutzung.

**Geschätzte Dauer:** ~24 Minuten

| Modul | Testfälle | Dauer |
|-------|-----------|-------|
| [App-Intro & Onboarding](#app-intro-onboarding) | 2 | 2 min |
| [Navigation](#navigation) | 3 | 3 min |
| [Nachrichten/Informationen](#nachrichteninformationen) | 4 | 5 min |
| [Veranstaltungen](#veranstaltungen) | 4 | 5 min |
| [Suche](#suche) | 3 | 3 min |
| [Push-Benachrichtigungen](#push-benachrichtigungen) | 2 | 3 min |
| [Einstellungen](#einstellungen) | 3 | 3 min |

**Bei Fehlern in P1:** Tests abbrechen und Fehler sofort melden!

### Priorität 2: Interaktive Module (P2) 🟡

**SOLLTE getestet werden** - Wichtige interaktive Features.

**Geschätzte Dauer:** +17 Minuten (gesamt ~41 min)

| Modul | Testfälle | Dauer |
|-------|-----------|-------|
| [Merkliste/Favoriten](#merklistefavoriten) | 3 | 3 min |
| [Mängelmelder](#maengelmelder) | 5 | 8 min |
| [Abfallkalender](#abfallkalender) | 3 | 3 min |

### Priorität 3: Erweiterte Features (P3) 🟢

**KANN getestet werden** - Erweiterte Funktionen, falls Zeit vorhanden.

**Geschätzte Dauer:** +5 Minuten (gesamt ~46 min)

| Modul | Testfälle | Dauer |
|-------|-----------|-------|
| [Karten & POIs](#karten-pois) | 4 | 5 min |

---

## Detaillierte Testfälle

### App-Intro & Onboarding

**Modul:** App-Intro
**Priorität:** P1
**Voraussetzung:** Neu-Installation oder Cache gelöscht

#### Testfall 1.1: Intro-Screens beim ersten Start

**Schritte:**
1. App neu installieren oder App-Daten löschen
2. App starten
3. Intro-Bildschirme durchgehen

**Erwartetes Ergebnis:**
- Intro-Bildschirme werden angezeigt
- Alle Screens sind lesbar und Bilder werden geladen
- "Weiter"-Button funktioniert

**Status:** ⬜ Pass / ⬜ Fail

#### Testfall 1.2: Skip-Funktion

**Schritte:**
1. Intro-Bildschirme starten
2. "Überspringen"-Button antippen

**Erwartetes Ergebnis:**
- App springt zur Hauptansicht
- Kein Crash oder Fehlverhalten

**Status:** ⬜ Pass / ⬜ Fail

---

### Navigation

**Modul:** Navigation
**Priorität:** P1

#### Testfall 2.1: Drawer-Navigation (falls aktiviert)

**Schritte:**
1. Hamburger-Menü öffnen
2. Navigation durchgehen
3. Menü schließen

**Erwartetes Ergebnis:**
- Drawer öffnet sich smooth
- Alle Menüpunkte sind sichtbar
- Drawer schließt korrekt

**Status:** ⬜ Pass / ⬜ Fail / ⬜ N/A

#### Testfall 2.2: Tabbar-Navigation (falls aktiviert)

**Schritte:**
1. Alle Tabs in der Bottom-Navigation antippen
2. Prüfen, ob alle Icons korrekt angezeigt werden

**Erwartetes Ergebnis:**
- Alle konfigurierten Tabs werden angezeigt
- Tab-Wechsel funktioniert ohne Verzögerung
- Aktiver Tab ist hervorgehoben

**Status:** ⬜ Pass / ⬜ Fail / ⬜ N/A

#### Testfall 2.3: Navigation zu Hauptbereichen

**Schritte:**
1. Zu jedem Hauptbereich navigieren (News, Events, Einstellungen)
2. Zurück-Navigation testen

**Erwartetes Ergebnis:**
- Alle Bereiche sind erreichbar
- Keine Navigation führt zu Fehlern
- Zurück-Button funktioniert

**Status:** ⬜ Pass / ⬜ Fail

---

### Nachrichten/Informationen

**Modul:** Nachrichten
**Priorität:** P1

#### Testfall 3.1: Nachrichten-Liste laden

**Schritte:**
1. Zum Nachrichten-Bereich navigieren
2. Liste laden lassen

**Erwartetes Ergebnis:**
- Aktuelle Nachrichten werden angezeigt
- Bilder und Texte laden korrekt
- Keine leere Liste (außer bei leerem CMS)

**Status:** ⬜ Pass / ⬜ Fail

#### Testfall 3.2: Detailansicht öffnen

**Schritte:**
1. Einen Artikel aus der Liste auswählen
2. Detailansicht öffnen
3. Scrollen durch den Artikel

**Erwartetes Ergebnis:**
- Artikel öffnet mit vollem Text
- Bilder und Formatierung korrekt
- Scrolling funktioniert smooth

**Status:** ⬜ Pass / ⬜ Fail

#### Testfall 3.3: Kategoriefilter (optional)

**Schritte:**
1. Filter-Funktion öffnen
2. Kategorie auswählen
3. Gefilterte Liste prüfen

**Erwartetes Ergebnis:**
- Filter-Optionen werden angezeigt
- Filterung funktioniert korrekt
- Filter kann zurückgesetzt werden

**Status:** ⬜ Pass / ⬜ Fail / ⬜ N/A

#### Testfall 3.4: Teilen-Funktion

**Schritte:**
1. Artikel öffnen
2. Teilen-Button antippen
3. Share-Sheet prüfen

**Erwartetes Ergebnis:**
- Share-Dialog öffnet
- Artikel-Link wird korrekt geteilt
- Zurück zur App funktioniert

**Status:** ⬜ Pass / ⬜ Fail

---

### Veranstaltungen

**Modul:** Veranstaltungen
**Priorität:** P1

#### Testfall 4.1: Veranstaltungsliste laden

**Schritte:**
1. Zum Veranstaltungs-Bereich navigieren
2. Liste der Events prüfen

**Erwartetes Ergebnis:**
- Aktuelle Veranstaltungen werden angezeigt
- Datum und Titel sind lesbar
- Bilder laden korrekt

**Status:** ⬜ Pass / ⬜ Fail

#### Testfall 4.2: Kalenderansicht

**Schritte:**
1. Zur Kalenderansicht wechseln
2. Monat durchblättern
3. Termin im Kalender antippen

**Erwartetes Ergebnis:**
- Kalender zeigt Termine an
- Navigation zwischen Monaten funktioniert
- Tap auf Termin öffnet Details

**Status:** ⬜ Pass / ⬜ Fail

#### Testfall 4.3: Event-Details

**Schritte:**
1. Event aus Liste auswählen
2. Detailansicht prüfen
3. Alle Informationen durchgehen

**Erwartetes Ergebnis:**
- Datum, Uhrzeit, Ort korrekt angezeigt
- Beschreibung vollständig
- Bilder und weitere Infos sichtbar

**Status:** ⬜ Pass / ⬜ Fail

#### Testfall 4.4: Filter nach Kategorien/Zeitraum

**Schritte:**
1. Filter-Funktion öffnen
2. Kategorie oder Zeitraum auswählen
3. Gefilterte Liste prüfen

**Erwartetes Ergebnis:**
- Filter-Optionen verfügbar
- Filterung funktioniert
- Filter zurücksetzen möglich

**Status:** ⬜ Pass / ⬜ Fail / ⬜ N/A

---

### Suche

**Modul:** Suche
**Priorität:** P1

#### Testfall 5.1: Suchfeld erreichbar

**Schritte:**
1. Suchfeld finden (Icon oder Tab)
2. Suchfeld antippen
3. Tastatur erscheint

**Erwartetes Ergebnis:**
- Suchfeld ist sichtbar
- Tap öffnet Eingabe
- Tastatur erscheint korrekt

**Status:** ⬜ Pass / ⬜ Fail

#### Testfall 5.2: Suchergebnisse anzeigen

**Schritte:**
1. Begriff eingeben (z.B. "Rathaus")
2. Suche ausführen
3. Ergebnisse prüfen

**Erwartetes Ergebnis:**
- Suchergebnisse werden angezeigt
- Mindestens 1 Ergebnis (wenn vorhanden)
- Ergebnis ist relevant

**Status:** ⬜ Pass / ⬜ Fail

#### Testfall 5.3: Suche über mehrere Content-Typen

**Schritte:**
1. Begriff eingeben
2. Ergebnisse aus verschiedenen Bereichen prüfen (News, Events, POIs)

**Erwartetes Ergebnis:**
- Verschiedene Content-Typen in Ergebnissen
- Typ ist erkennbar (Icon/Label)
- Tap öffnet korrekten Content

**Status:** ⬜ Pass / ⬜ Fail

---

### Push-Benachrichtigungen

**Modul:** Push-Nachrichten
**Priorität:** P1

#### Testfall 6.1: Push-Registrierung

**Schritte:**
1. Neu-Installation der App
2. Beim ersten Start auf Permission-Dialog achten
3. Push-Berechtigung erlauben

**Erwartetes Ergebnis:**
- Permission-Dialog erscheint
- Erlauben funktioniert
- Keine Fehlermeldung

**Status:** ⬜ Pass / ⬜ Fail

#### Testfall 6.2: Test-Push empfangen

**Schritte:**
1. Test-Push über CMS versenden
2. Push-Benachrichtigung prüfen
3. Auf Push tippen → App öffnen

**Erwartetes Ergebnis:**
- Push wird empfangen und angezeigt
- Titel und Text korrekt
- Tap öffnet richtigen Content

**Status:** ⬜ Pass / ⬜ Fail

---

### Einstellungen

**Modul:** Einstellungen
**Priorität:** P1

#### Testfall 7.1: Einstellungen öffnen

**Schritte:**
1. Zu Einstellungen navigieren
2. Einstellungs-Screen prüfen

**Erwartetes Ergebnis:**
- Einstellungen-Screen lädt
- Alle Optionen sind sichtbar
- Kein Layout-Fehler

**Status:** ⬜ Pass / ⬜ Fail

#### Testfall 7.2: Push-Einstellungen ändern

**Schritte:**
1. Push-Benachrichtigungen aktivieren/deaktivieren
2. Kategorien an/ausschalten (falls vorhanden)
3. Änderungen speichern

**Erwartetes Ergebnis:**
- Toggle funktioniert
- Änderungen werden gespeichert
- Keine Fehlermeldung

**Status:** ⬜ Pass / ⬜ Fail

#### Testfall 7.3: App-Informationen

**Schritte:**
1. "Über die App" oder "Info" öffnen
2. Version, Impressum, Datenschutz prüfen

**Erwartetes Ergebnis:**
- App-Version wird angezeigt
- Impressum/Datenschutz sind erreichbar
- Links funktionieren

**Status:** ⬜ Pass / ⬜ Fail

---

### Merkliste/Favoriten

**Modul:** Merkliste/Favoriten
**Priorität:** P2

#### Testfall 8.1: Favorit markieren

**Schritte:**
1. Einen Artikel/Event öffnen
2. Favoriten-Icon (Stern/Herz) antippen
3. Bestätigung prüfen

**Erwartetes Ergebnis:**
- Icon ändert sich (gefüllt)
- Feedback (Animation/Toast)
- Inhalt ist gespeichert

**Status:** ⬜ Pass / ⬜ Fail

#### Testfall 8.2: Merkliste öffnen

**Schritte:**
1. Zur Merkliste navigieren
2. Gespeicherte Inhalte prüfen

**Erwartetes Ergebnis:**
- Merkliste zeigt Favoriten
- Alle markierten Inhalte sichtbar
- Tap öffnet Original-Inhalt

**Status:** ⬜ Pass / ⬜ Fail

#### Testfall 8.3: Favorit entfernen

**Schritte:**
1. In Merkliste oder Detail-View
2. Favoriten-Icon erneut antippen
3. Aus Merkliste prüfen

**Erwartetes Ergebnis:**
- Icon wird ungefüllt
- Inhalt verschwindet aus Merkliste
- Keine Fehlermeldung

**Status:** ⬜ Pass / ⬜ Fail

---

### Mängelmelder

**Modul:** Mängelmelder
**Priorität:** P2
**Hinweis:** Nur wenn Modul aktiviert ist

#### Testfall 9.1: Formular öffnen

**Schritte:**
1. Zum Mängelmelder navigieren
2. "Meldung erstellen" antippen
3. Formular prüfen

**Erwartetes Ergebnis:**
- Formular wird angezeigt
- Alle Felder sind editierbar
- Kein Layout-Fehler

**Status:** ⬜ Pass / ⬜ Fail

#### Testfall 9.2: Foto aufnehmen/hochladen

**Schritte:**
1. Foto-Button antippen
2. Kamera oder Galerie auswählen
3. Foto hinzufügen

**Erwartetes Ergebnis:**
- Kamera/Galerie öffnet
- Foto wird im Formular angezeigt
- Mehrere Fotos möglich (falls konfiguriert)

**Status:** ⬜ Pass / ⬜ Fail

#### Testfall 9.3: Standort erfassen

**Schritte:**
1. Standort-Erfassung prüfen
2. GPS-Position oder Karten-Auswahl

**Erwartetes Ergebnis:**
- Standort wird automatisch erfasst ODER
- Karte öffnet zur manuellen Auswahl
- Standort wird im Formular angezeigt

**Status:** ⬜ Pass / ⬜ Fail

#### Testfall 9.4: Meldung absenden

**Schritte:**
1. Formular ausfüllen (Titel, Beschreibung)
2. Foto und Standort hinzufügen
3. "Absenden"-Button antippen

**Erwartetes Ergebnis:**
- Keine Validierungsfehler
- Meldung wird versendet
- Keine Fehlermeldung

**Status:** ⬜ Pass / ⬜ Fail

#### Testfall 9.5: Bestätigung nach Versand

**Schritte:**
1. Nach Absenden Bestätigung prüfen
2. Meldungs-ID oder Referenz erhalten (optional)

**Erwartetes Ergebnis:**
- Erfolgs-Meldung wird angezeigt
- Formular wird geleert oder zurückgesetzt
- Rückkehr zur Übersicht möglich

**Status:** ⬜ Pass / ⬜ Fail

---

### Abfallkalender

**Modul:** Abfallkalender
**Priorität:** P2
**Hinweis:** Nur wenn Modul aktiviert ist

#### Testfall 10.1: Kalenderansicht

**Schritte:**
1. Zum Abfallkalender navigieren
2. Aktuelle Termine prüfen
3. Durch Monate blättern

**Erwartetes Ergebnis:**
- Abfuhrtermine werden angezeigt
- Farbcodierung nach Abfallart
- Monats-Navigation funktioniert

**Status:** ⬜ Pass / ⬜ Fail

#### Testfall 10.2: Adresse/PLZ eingeben

**Schritte:**
1. Adress-Eingabe öffnen (falls konfiguriert)
2. PLZ oder Adresse eingeben
3. Termine für Adresse prüfen

**Erwartetes Ergebnis:**
- Eingabefeld funktioniert
- Termine für Adresse werden geladen
- Keine Fehlermeldung bei gültiger Adresse

**Status:** ⬜ Pass / ⬜ Fail / ⬜ N/A

#### Testfall 10.3: Push-Erinnerungen

**Schritte:**
1. Push-Erinnerungen aktivieren
2. Einstellungen prüfen (Vorabend/Morgen)

**Erwartetes Ergebnis:**
- Erinnerungs-Option verfügbar
- Aktivierung funktioniert
- Zeitpunkt wählbar (falls konfiguriert)

**Status:** ⬜ Pass / ⬜ Fail / ⬜ N/A

---

### Karten & POIs

**Modul:** Karten
**Priorität:** P3

#### Testfall 11.1: Kartenansicht laden

**Schritte:**
1. Zur Karte navigieren
2. Karte laden lassen
3. Standort prüfen

**Erwartetes Ergebnis:**
- Karte wird angezeigt (OpenStreetMap)
- Aktueller Standort wird angezeigt (falls Berechtigung)
- Keine leere Karte

**Status:** ⬜ Pass / ⬜ Fail

#### Testfall 11.2: POIs als Marker

**Schritte:**
1. Karte durchsehen
2. POI-Marker prüfen
3. Verschiedene POI-Typen identifizieren

**Erwartetes Ergebnis:**
- POIs werden als Marker angezeigt
- Icons sind erkennbar
- Marker clustern bei vielen POIs

**Status:** ⬜ Pass / ⬜ Fail

#### Testfall 11.3: Marker-Details

**Schritte:**
1. Auf Marker tippen
2. Info-Bubble oder Detail-View prüfen
3. Zum Detail-Screen navigieren

**Erwartetes Ergebnis:**
- Info-Bubble zeigt Basis-Infos
- Tap auf Info öffnet Details
- Zurück zur Karte funktioniert

**Status:** ⬜ Pass / ⬜ Fail

#### Testfall 11.4: Zoom und Pan

**Schritte:**
1. Karte zoomen (Pinch-Geste)
2. Karte verschieben (Pan)
3. Zoom-Buttons testen (falls vorhanden)

**Erwartetes Ergebnis:**
- Zoom smooth und ohne Ruckeln
- Pan funktioniert flüssig
- Karte lädt neue Tiles nach

**Status:** ⬜ Pass / ⬜ Fail

---

## Test-Report-Template

Nach Abschluss der Smoke Tests sollte ein Test-Report erstellt werden. Hier ist eine Vorlage:

```markdown
# Smoke Test Report

## Test-Informationen

- **Datum:** [YYYY-MM-DD]
- **Uhrzeit:** [HH:MM]
- **Tester:** [Name]
- **App-Version:** [z.B. 2.5.0 (Build 123)]
- **Test-Umgebung:** [Staging / Production]
- **Plattform:** [iOS 17 / Android 14]
- **Gerät:** [iPhone 14 / Samsung Galaxy S23]

## Getestete Module

- ☑ Priorität 1 (P1) - Vollständig
- ☑ Priorität 2 (P2) - Vollständig / Teilweise
- ☐ Priorität 3 (P3) - Nicht getestet / Teilweise

## Test-Ergebnisse Übersicht

| Modul | P | Tests | Pass | Fail | N/A | Status |
|-------|---|-------|------|------|-----|--------|
| App-Intro | P1 | 2 | 2 | 0 | 0 | ✅ PASS |
| Navigation | P1 | 3 | 3 | 0 | 0 | ✅ PASS |
| Nachrichten | P1 | 4 | 3 | 1 | 0 | ❌ FAIL |
| Veranstaltungen | P1 | 4 | 4 | 0 | 0 | ✅ PASS |
| Suche | P1 | 3 | 3 | 0 | 0 | ✅ PASS |
| Push | P1 | 2 | 2 | 0 | 0 | ✅ PASS |
| Einstellungen | P1 | 3 | 3 | 0 | 0 | ✅ PASS |
| Merkliste | P2 | 3 | 3 | 0 | 0 | ✅ PASS |
| Mängelmelder | P2 | 5 | 5 | 0 | 0 | ✅ PASS |
| Abfallkalender | P2 | 3 | 0 | 0 | 3 | ⚪ N/A |
| Karten | P3 | 4 | 0 | 0 | 4 | ⚪ N/A |

**Gesamt:** 21 Pass / 1 Fail / 7 N/A

## Gefundene Bugs

### Bug #1: Nachrichten-Kategoriefilter funktioniert nicht

**Severity:** Mittel
**Testfall:** 3.3 - Kategoriefilter
**Beschreibung:** Beim Auswählen einer Kategorie im Filter wird die Liste nicht aktualisiert. Alle Artikel bleiben sichtbar.
**Reproduzierbar:** Ja
**Steps to Reproduce:**
1. Nachrichten-Liste öffnen
2. Filter-Icon antippen
3. Kategorie "Rathaus" auswählen
4. Ergebnis: Liste unverändert

**Erwartetes Verhalten:** Nur Artikel der Kategorie "Rathaus" sollten angezeigt werden.
**Screenshot/Video:** [Link zu Screenshot]
**Issue:** [#123](https://github.com/.../issues/123)

## Anmerkungen

- P1-Tests erfolgreich bis auf Kategoriefilter
- P2-Tests vollständig durchgeführt
- P3 nicht getestet (Zeitlimit)
- Abfallkalender nicht aktiv in dieser App-Konfiguration

## Empfehlung

❌ **NO-GO** - Bug #1 muss vor Release behoben werden

☑ **GO** - Release kann fortgesetzt werden (nach Bug-Fix)
```

---

## Best Practices

### Vor dem Testen

- ✅ **Richtige App-Version:** Überprüfe Build-Nummer in Einstellungen
- ✅ **Stabile Netzwerkverbindung:** WLAN bevorzugt
- ✅ **Test-Daten verfügbar:** CMS hat aktuelle Inhalte
- ✅ **Berechtigungen erteilt:** Location, Camera, Notifications (falls nötig für Tests)

### Während des Testens

- ✅ **Fokussiert bleiben:** Keine Ablenkung, zügig arbeiten
- ✅ **Screenshots machen:** Bei Fehlern sofort dokumentieren
- ✅ **Fehler reproduzieren:** Mindestens 2x versuchen vor Meldung
- ✅ **Notizen machen:** Unklarheiten oder Auffälligkeiten notieren

### Nach dem Testen

- ✅ **Report ausfüllen:** Direkt nach Tests, nicht später
- ✅ **Bugs melden:** In Issue-Tracker eintragen mit allen Details
- ✅ **Team informieren:** Bei kritischen Bugs (P1) sofort Bescheid geben
- ✅ **Follow-up:** Nach Bug-Fixes erneut testen

### Tipps

- **Zeitmanagement:** P1 zuerst, dann P2, P3 nur bei Zeit
- **Bei Blockern stoppen:** P1-Fehler = Tests abbrechen
- **Realistische Szenarien:** Als echter User testen
- **Edge Cases beachten:** Leere Listen, Offline-Mode, etc.

---

## Automatisierung (Zukunft)

Diese Checkliste ist für **manuelle Tests** konzipiert. Zukünftig können viele Tests automatisiert werden:

- **CI/CD Integration:** Automatische Smoke Tests nach jedem Build
- **E2E-Test-Frameworks:** Appium, Detox, Maestro
- **Monitoring:** Kontinuierliche Überprüfung in Production

Siehe auch: [Roadmap für automatisierte Tests](#) (coming soon)

---

## Weitere Ressourcen

- [Modul-Beschreibungen](../../yml/) - Technische Details zu allen Modulen
- [Setup-Anleitung](setup.md) - Entwicklungsumgebung einrichten
- [API-Dokumentation](api.md) - Backend-Schnittstellen

---

**Letzte Aktualisierung:** 2025-11-17
**Version:** 1.0
**Maintainer:** Smart Village Solutions
