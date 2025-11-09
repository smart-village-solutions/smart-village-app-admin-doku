#!/usr/bin/env python3
"""
Draft Module Creator

Schritt 1 des neuen Workflows: Erstellt einen AI-basierten Entwurf eines Moduls
als DRAFT-[name].yml basierend auf dem Modulnamen. Die KI generiert automatisch
einen vollständigen Vorschlag, der dann im Editor zur Review geöffnet wird.

Der Mensch überprüft, korrigiert und ergänzt den AI-Vorschlag mit Domänenwissen.

Usage:
    python scripts/draft_module.py --name abfallkalender
    python scripts/draft_module.py --name push-nachrichten --editor code
"""

import argparse
import sys
import json
import yaml
import subprocess
import os
from pathlib import Path
from typing import Dict, Any, Optional

# ANSI color codes
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
RED = '\033[91m'
BOLD = '\033[1m'
RESET = '\033[0m'


def load_schema(schema_path: Path) -> Dict[str, Any]:
    """Lädt das JSON Schema für Module."""
    with open(schema_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_topic_options(schema: Dict[str, Any]) -> list:
    """Extrahiert verfügbare Topics aus dem Schema."""
    return schema['properties']['topic']['enum']


def generate_ai_draft(name: str, schema: Dict[str, Any]) -> Dict[str, Any]:
    """Generiert AI-basierten Entwurf für ein Modul basierend auf dem Namen."""

    # Mapping: Modulname → Topic (intelligente Zuordnung)
    topic_mapping = {
        'push-nachrichten': 'push-benachrichtigungen',
        'push': 'push-benachrichtigungen',
        'abfallkalender': 'abfallkalender',
        'maengelmelder': 'maengelmelder',
        'karten': 'tourismusinformationen',
        'veranstaltungen': 'veranstaltungskalender',
        'nachrichten': 'nachrichten',
        'wetter': 'wetterinformationen',
        'oepnv': 'oepnv-auskunft',
        'parkplatz': 'parkinformationen',
        'termin': 'terminbuchung',
        'feedback': 'feedbackmodul',
        'formular': 'formularservice',
        'notfall': 'notfallwarnungen',
        'umfrage': 'bürgerbeteiligung',
        'jobs': 'stellenangebote',
        'stellenanzeigen': 'stellenangebote',
        'branchenbuch': 'branchenverzeichnis',
        'tourismus': 'tourismusinformationen',
        'kultur': 'kulturveranstaltungen',
        'bildung': 'bildungsinformationen',
        'hilfe': 'hilfe-und-faq',
        'faq': 'hilfe-und-faq',
    }

    # Bestimme Topic
    topic = topic_mapping.get(name.lower(), 'nachrichten')  # Default: nachrichten

    # Modul-spezifische Templates
    templates = {
        'push-nachrichten': {
            'topic': 'push-benachrichtigungen',
            'short_description': 'Ermöglicht das Versenden von Push-Benachrichtigungen an App-Nutzer',
            'usage_scenario': 'Verwaltung informiert Bürger per Push über wichtige Ereignisse wie Straßensperrungen oder Veranstaltungsabsagen',
            'description': '''Das Push-Nachrichten-Modul ermöglicht es Redakteuren, zeitkritische Informationen direkt an die Smartphones der Bürger zu senden.

**Funktionen:**
- Erstellung und Versand von Push-Benachrichtigungen
- Zeitgesteuerte Zustellung (sofort oder geplant)
- Zielgruppen-Segmentierung nach Themen/Interessen
- Statistiken über Zustellung und Klickrate
- Verlinkung zu Inhalten in der App

**Anwendungsfälle:**
- Eilmeldungen und Warnungen
- Erinnerungen an Veranstaltungen
- Hinweise auf neue Inhalte
- Service-Informationen (z.B. Rathaus-Schließung)''',
            'interfaces': [
                'REST API für Push-Versand',
                'CMS-Integration für Redakteure',
                'Analytics-Schnittstelle für Statistiken'
            ],
            'dependencies': [
                'cms',
                'app-server'
            ],
            'external_services': ['Firebase Cloud Messaging (FCM)', 'Apple Push Notification Service (APNs)'],
            'customization_options': [
                'Push-Kategorien konfigurieren',
                'Zeitfenster für Zustellung festlegen',
                'Maximale Push-Frequenz pro Nutzer',
                'Standard-Icons und -Töne'
            ],
            'involved_actors': [
                {'name': 'Administrator', 'role': 'Verwaltet Push-Nachrichten im CMS'},
                {'name': 'Bürger', 'role': 'Empfängt Push-Benachrichtigungen'}
            ],
            'last_update': '2025-11-09',
            'roadmap': []
        },
        'app-intro': {
            'topic': 'hilfe-und-faq',
            'short_description': 'Einführungsbildschirme beim ersten App-Start zur Vorstellung der Funktionen',
            'usage_scenario': 'Neuer Nutzer öffnet die App zum ersten Mal und erhält eine Übersicht der wichtigsten Features',
            'description': '''Das App-Intro-Modul zeigt beim ersten App-Start eine Reihe von Einführungsbildschirmen, die die Hauptfunktionen der App vorstellen.

**Funktionen:**
- Mehrseitige Einführung mit Bildern und Texten
- Skip-Funktion zum Überspringen
- Nur beim ersten Start (danach ausblendbar)
- Anpassbare Inhalte und Designs

**Anwendungsfälle:**
- Onboarding neuer Nutzer
- Vorstellung der wichtigsten Features
- Erklärung von Bedienkonzepten''',
            'interfaces': ['App-interne Konfiguration'],
            'customization_options': [
                'Anzahl der Intro-Seiten',
                'Bilder und Texte anpassen',
                'Farben und Styling',
                'Reihenfolge der Screens'
            ],
            'involved_actors': [
                {'name': 'Administrator', 'role': 'Konfiguriert Intro-Inhalte und Einstellungen'},
                {'name': 'Bürger', 'role': 'Sieht und durchläuft das Intro beim ersten App-Start'}
            ],
            'external_services': [],
            'last_update': '2025-11-09',
            'roadmap': []
        }
    }

    # Hole Template oder erstelle generisches
    if name.lower() in templates:
        template = templates[name.lower()]
    else:
        # Generisches Template
        template = {
            'topic': topic,
            'short_description': f'Modul für {name.replace("-", " ").title()}',
            'usage_scenario': f'Bürger nutzt {name.replace("-", " ")} Funktionalität in der App',
            'description': f'''Das {name.replace("-", " ").title()}-Modul bietet Funktionen für [BESCHREIBUNG ERGÄNZEN].

**Funktionen:**
- [FUNKTION 1]
- [FUNKTION 2]
- [FUNKTION 3]

**Anwendungsfälle:**
- [ANWENDUNGSFALL 1]
- [ANWENDUNGSFALL 2]''',
            'interfaces': ['[SCHNITTSTELLEN ERGÄNZEN]'],
            'customization_options': ['[OPTIONEN ERGÄNZEN]'],
            'involved_actors': [{'name': '[AKTEUR 1]', 'role': '[ROLLE/AKTION]'}],
            'external_services': [],
            'last_update': '2025-11-09',
            'roadmap': []
        }

    # Basis-Daten - topic ist jetzt im template enthalten
    module_data = {
        'name': name,
        **template
    }

    return module_data


def prompt_with_options(prompt: str, options: list, default: Optional[str] = None) -> str:
    """Zeigt Optionen an und fragt Benutzer nach Auswahl."""
    print(f"\n{BLUE}{prompt}{RESET}")
    for i, option in enumerate(options, 1):
        marker = f" {GREEN}(default){RESET}" if option == default else ""
        print(f"  {i}. {option}{marker}")

    while True:
        choice = input(f"\n{CYAN}Auswahl (Nummer oder Text):{RESET} ").strip()

        if not choice and default:
            return default

        # Versuche als Nummer
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                return options[idx]
        except ValueError:
            pass

        # Versuche als Text
        if choice in options:
            return choice

        print(f"{RED}Ungültige Auswahl. Bitte erneut versuchen.{RESET}")


def prompt_text(prompt: str, default: Optional[str] = None, multiline: bool = False) -> str:
    """Fragt Benutzer nach Text-Eingabe."""
    default_hint = f" [{default}]" if default else ""
    multiline_hint = " (Mehrere Zeilen möglich, beende mit leerer Zeile)" if multiline else ""

    print(f"\n{BLUE}{prompt}{default_hint}{multiline_hint}{RESET}")

    if multiline:
        lines = []
        print(f"{CYAN}>{RESET} ", end="")
        while True:
            line = input()
            if not line:
                break
            lines.append(line)
            print(f"{CYAN}>{RESET} ", end="")
        result = "\n".join(lines)
    else:
        result = input(f"{CYAN}>{RESET} ").strip()

    if not result and default:
        return default

    return result


def prompt_list(prompt: str, item_type: str = "Item") -> list:
    """Fragt Benutzer nach Liste von Items."""
    print(f"\n{BLUE}{prompt}{RESET}")
    print(f"{YELLOW}Gib '{item_type}' ein (leer zum Beenden):{RESET}")

    items = []
    while True:
        item = input(f"{CYAN}{len(items)+1}. {RESET}").strip()
        if not item:
            break
        items.append(item)

    return items


def prompt_yes_no(prompt: str, default: bool = False) -> bool:
    """Fragt Benutzer nach Ja/Nein."""
    default_hint = " [J/n]" if default else " [j/N]"
    print(f"\n{BLUE}{prompt}{default_hint}{RESET}")

    choice = input(f"{CYAN}>{RESET} ").strip().lower()

    if not choice:
        return default

    return choice in ['j', 'ja', 'y', 'yes']


def create_draft_yaml(name: str, data: Dict[str, Any], modules_dir: Path) -> Path:
    """Erstellt DRAFT-[name].yml mit gesammelten Daten."""
    draft_path = modules_dir / f"DRAFT-{name}.yml"

    # Füge Header-Kommentar hinzu
    header = f"""# DRAFT MODULE: {name}
# Status: ENTWURF - Noch nicht finalisiert
#
# Dies ist ein AI-generierter Entwurf. Bitte überprüfen, korrigieren und ergänzen:
# - Sind alle Angaben korrekt?
# - Fehlen wichtige Informationen?
# - Sind die Beschreibungen verständlich?
# - Sind alle relevanten Akteure erfasst?
# - Sind alle Schnittstellen dokumentiert?
#
# Nach der Überprüfung: python scripts/review_module.py --name {name}

"""

    with open(draft_path, 'w', encoding='utf-8') as f:
        f.write(header)
        yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

    return draft_path


def open_in_editor(file_path: Path, editor: Optional[str] = None):
    """Öffnet Datei im Editor."""
    if not editor:
        # Auto-detect editor
        editor = os.environ.get('EDITOR', 'nano')

        # Versuche VS Code zu erkennen
        if subprocess.run(['which', 'code'], capture_output=True).returncode == 0:
            editor = 'code'

    print(f"\n{YELLOW}Öffne {file_path.name} im Editor ({editor})...{RESET}")

    try:
        if editor == 'code':
            subprocess.run(['code', '--wait', str(file_path)])
        else:
            subprocess.run([editor, str(file_path)])
    except Exception as e:
        print(f"{RED}Fehler beim Öffnen des Editors: {e}{RESET}")
        print(f"{YELLOW}Bitte bearbeite die Datei manuell: {file_path}{RESET}")


def main():
    parser = argparse.ArgumentParser(
        description='Erstellt AI-Entwurf eines Moduls (Schritt 1: Draft)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Beispiele:
  %(prog)s --name push-nachrichten
  %(prog)s --name abfallkalender --editor vim
  %(prog)s --name karten --no-editor
        """
    )
    parser.add_argument('--name', required=True, help='Name des Moduls (z.B. abfallkalender)')
    parser.add_argument('--editor', help='Editor zum Öffnen (default: $EDITOR oder auto-detect)')
    parser.add_argument('--no-editor', action='store_true', help='Datei nicht automatisch öffnen')

    args = parser.parse_args()

    # Paths
    root_dir = Path(__file__).parent.parent
    schema_path = root_dir / 'schema' / 'app-module.schema.json'
    modules_dir = root_dir / 'yml' / 'modules'

    print(f"{BOLD}{CYAN}=== Draft Module Creator ==={RESET}\n")
    print(f"Erstelle Entwurf für Modul: {BOLD}{args.name}{RESET}")

    # Prüfe ob DRAFT schon existiert
    draft_path = modules_dir / f"DRAFT-{args.name}.yml"
    if draft_path.exists():
        print(f"\n{YELLOW}⚠ DRAFT-{args.name}.yml existiert bereits!{RESET}")
        if not prompt_yes_no("Überschreiben?", default=False):
            print(f"{RED}Abgebrochen.{RESET}")
            return 1

    # Lade Schema
    try:
        schema = load_schema(schema_path)
    except Exception as e:
        print(f"{RED}Fehler beim Laden des Schemas: {e}{RESET}")
        return 1

    # Generiere AI-basierten Entwurf
    print(f"\n{BOLD}Generiere AI-Vorschlag...{RESET}")

    try:
        module_data = generate_ai_draft(args.name, schema)
        print(f"{GREEN}✓ AI-Vorschlag generiert{RESET}")

        # Zeige Vorschau
        print(f"\n{BOLD}{BLUE}Vorschau des generierten Entwurfs:{RESET}")
        print(f"{CYAN}Topic:{RESET} {module_data['topic']}")
        print(f"{CYAN}Kurzbeschreibung:{RESET} {module_data['short_description']}")
        print(f"{CYAN}Hauptszenario:{RESET} {module_data['usage_scenario']}")

        # Zeige ob weitere Felder vorhanden
        optional_count = sum(1 for k in ['interfaces', 'dependencies', 'external_services',
                                        'customization_options', 'involved_actors']
                           if k in module_data and module_data[k])
        if optional_count > 0:
            print(f"{GREEN}✓ {optional_count} optionale Felder bereits ausgefüllt{RESET}")
        else:
            print(f"{YELLOW}○ Optionale Felder müssen noch ergänzt werden{RESET}")

    except Exception as e:
        print(f"{RED}Fehler bei AI-Generierung: {e}{RESET}")
        return 1

    # Erstelle DRAFT
    print(f"\n{BOLD}Erstelle DRAFT-{args.name}.yml...{RESET}")

    try:
        draft_path = create_draft_yaml(args.name, module_data, modules_dir)
        print(f"{GREEN}✓ DRAFT erstellt: {draft_path}{RESET}")
    except Exception as e:
        print(f"{RED}Fehler beim Erstellen des DRAFTs: {e}{RESET}")
        return 1

    # Öffne im Editor
    if not args.no_editor:
        open_in_editor(draft_path, args.editor)

    # Abschluss
    print(f"\n{BOLD}{GREEN}=== Draft erstellt ==={RESET}\n")
    print(f"Datei: {CYAN}{draft_path}{RESET}")
    print(f"\n{YELLOW}Nächste Schritte:{RESET}")
    print(f"1. Überprüfe und ergänze {BOLD}DRAFT-{args.name}.yml{RESET}")
    print(f"2. Führe aus: {BOLD}python scripts/review_module.py --name {args.name}{RESET}")
    print(f"\n{BLUE}Der DRAFT kann beliebig oft bearbeitet werden, bevor du ihn finalisierst.{RESET}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
