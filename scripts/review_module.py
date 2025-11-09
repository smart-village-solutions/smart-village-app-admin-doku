#!/usr/bin/env python3
"""
Module Review Tool

Schritt 2 des neuen Workflows: Zeigt eine Zusammenfassung des DRAFT-Moduls,
fragt nach Bereitschaft zur Finalisierung und ermöglicht weitere Iterationen.

Dieser Schritt ist der explizite "Human in the Loop" Checkpoint.

Usage:
    python scripts/review_module.py --name abfallkalender
    python scripts/review_module.py --name push-nachrichten --verbose
"""

import argparse
import sys
import yaml
import json
import subprocess
from pathlib import Path
from typing import Dict, Any, List
from jsonschema import validate, ValidationError

# ANSI color codes
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
RED = '\033[91m'
BOLD = '\033[1m'
RESET = '\033[0m'


def load_yaml(path: Path) -> Dict[str, Any]:
    """Lädt YAML-Datei."""
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def load_schema(schema_path: Path) -> Dict[str, Any]:
    """Lädt JSON Schema."""
    with open(schema_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def validate_draft(data: Dict[str, Any], schema: Dict[str, Any]) -> tuple[bool, List[str]]:
    """Validiert DRAFT gegen Schema."""
    errors = []
    try:
        validate(instance=data, schema=schema)
        return True, []
    except ValidationError as e:
        errors.append(str(e.message))
        return False, errors


def print_summary(data: Dict[str, Any], verbose: bool = False):
    """Zeigt Zusammenfassung des Moduls."""
    print(f"\n{BOLD}{BLUE}=== Modul-Übersicht ==={RESET}\n")

    # Basis-Info
    print(f"{BOLD}Name:{RESET} {data.get('name', 'N/A')}")
    print(f"{BOLD}Topic:{RESET} {data.get('topic', 'N/A')}")
    print(f"{BOLD}Kurzbeschreibung:{RESET} {data.get('short_description', 'N/A')}")

    # Usage Scenario
    if 'usage_scenario' in data:
        print(f"\n{BOLD}Hauptszenario:{RESET}")
        print(f"  {data['usage_scenario']}")

    # Description
    if 'description' in data:
        print(f"\n{BOLD}Beschreibung:{RESET}")
        desc_lines = data['description'].split('\n')
        if len(desc_lines) > 5 and not verbose:
            for line in desc_lines[:5]:
                print(f"  {line}")
            print(f"  {YELLOW}... ({len(desc_lines) - 5} weitere Zeilen, nutze --verbose für Details){RESET}")
        else:
            for line in desc_lines:
                print(f"  {line}")

    # Optional fields
    optional_fields = {
        'interfaces': 'Schnittstellen',
        'dependencies': 'Abhängigkeiten',
        'external_services': 'Externe Dienste',
        'customization_options': 'Konfigurations-Optionen',
        'involved_actors': 'Beteiligte Akteure'
    }

    print(f"\n{BOLD}Optionale Felder:{RESET}")
    for field, label in optional_fields.items():
        if field in data and data[field]:
            print(f"  {GREEN}✓{RESET} {label}: {len(data[field])} Item(s)")
            if verbose:
                for item in data[field]:
                    print(f"    - {item}")
        else:
            print(f"  {YELLOW}○{RESET} {label}: Nicht gesetzt")

    # Overrides from global
    override_fields = ['development_status', 'deployed_in_municipalities', 'cost']
    overrides = {k: v for k, v in data.items() if k in override_fields}

    if overrides:
        print(f"\n{BOLD}{YELLOW}Overrides (weichen von global.yml ab):{RESET}")
        for field, value in overrides.items():
            if isinstance(value, list):
                print(f"  • {field}: {len(value)} Item(s)")
            else:
                print(f"  • {field}: {value}")


def check_completeness(data: Dict[str, Any]) -> List[str]:
    """Prüft Vollständigkeit und gibt Hinweise."""
    warnings = []

    # Prüfe wichtige optionale Felder
    if 'interfaces' not in data or not data['interfaces']:
        warnings.append("Keine Schnittstellen definiert - ist das korrekt?")

    if 'involved_actors' not in data or not data['involved_actors']:
        warnings.append("Keine beteiligten Akteure definiert - wer nutzt das Modul?")

    # Prüfe Beschreibungs-Länge
    desc = data.get('description', '')
    if len(desc) < 100:
        warnings.append(f"Beschreibung ist sehr kurz ({len(desc)} Zeichen) - evtl. mehr Details hinzufügen?")

    # Prüfe Short Description
    short = data.get('short_description', '')
    if len(short) > 150:
        warnings.append(f"Kurzbeschreibung ist lang ({len(short)} Zeichen) - sollte prägnant sein")

    return warnings


def open_editor(file_path: Path, editor: str = None):
    """Öffnet Datei im Editor."""
    if not editor:
        editor = 'code' if subprocess.run(['which', 'code'], capture_output=True).returncode == 0 else 'nano'

    print(f"{YELLOW}Öffne {file_path.name} im Editor...{RESET}")
    try:
        if editor == 'code':
            subprocess.run(['code', '--wait', str(file_path)])
        else:
            subprocess.run([editor, str(file_path)])
    except Exception as e:
        print(f"{RED}Fehler: {e}{RESET}")


def prompt_yes_no(prompt: str, default: bool = False) -> bool:
    """Fragt Benutzer nach Ja/Nein."""
    default_hint = " [J/n]" if default else " [j/N]"
    print(f"\n{BLUE}{prompt}{default_hint}{RESET}")

    choice = input(f"{CYAN}>{RESET} ").strip().lower()

    if not choice:
        return default

    return choice in ['j', 'ja', 'y', 'yes']


def main():
    parser = argparse.ArgumentParser(
        description='Review und Freigabe eines DRAFT-Moduls (Schritt 2: Review)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Beispiele:
  %(prog)s --name push-nachrichten
  %(prog)s --name abfallkalender --verbose
  %(prog)s --name karten --editor vim
        """
    )
    parser.add_argument('--name', required=True, help='Name des Moduls')
    parser.add_argument('--verbose', '-v', action='store_true', help='Zeige alle Details')
    parser.add_argument('--editor', help='Editor für Bearbeitung')

    args = parser.parse_args()

    # Paths
    root_dir = Path(__file__).parent.parent
    draft_path = root_dir / 'yml' / 'modules' / f"DRAFT-{args.name}.yml"
    schema_path = root_dir / 'schema' / 'app-module.schema.json'

    print(f"{BOLD}{CYAN}=== Module Review Tool ==={RESET}\n")
    print(f"Review für Modul: {BOLD}{args.name}{RESET}")

    # Prüfe ob DRAFT existiert
    if not draft_path.exists():
        print(f"\n{RED}✗ DRAFT-{args.name}.yml nicht gefunden!{RESET}")
        print(f"{YELLOW}Erstelle zuerst einen DRAFT mit:{RESET}")
        print(f"  python scripts/draft_module.py --name {args.name}")
        return 1

    # Lade DRAFT und Schema
    try:
        draft_data = load_yaml(draft_path)
        schema = load_schema(schema_path)
    except Exception as e:
        print(f"{RED}Fehler beim Laden: {e}{RESET}")
        return 1

    # Zeige Zusammenfassung
    print_summary(draft_data, args.verbose)

    # Validierung
    print(f"\n{BOLD}{BLUE}=== Validierung ==={RESET}\n")
    is_valid, errors = validate_draft(draft_data, schema)

    if is_valid:
        print(f"{GREEN}✓ Schema-Validierung erfolgreich{RESET}")
    else:
        print(f"{RED}✗ Schema-Validierung fehlgeschlagen:{RESET}")
        for error in errors:
            print(f"  {RED}•{RESET} {error}")
        print(f"\n{YELLOW}Bitte korrigiere die Fehler vor der Finalisierung.{RESET}")

    # Vollständigkeits-Prüfung
    warnings = check_completeness(draft_data)
    if warnings:
        print(f"\n{BOLD}{YELLOW}Hinweise zur Vollständigkeit:{RESET}")
        for warning in warnings:
            print(f"  {YELLOW}⚠{RESET} {warning}")

    # Interaktive Freigabe-Schleife
    print(f"\n{BOLD}{BLUE}=== Freigabe-Entscheidung ==={RESET}\n")

    while True:
        print(f"\n{BOLD}Was möchtest du tun?{RESET}")
        print(f"  {GREEN}1.{RESET} Modul ist bereit → Finalisieren")
        print(f"  {YELLOW}2.{RESET} Noch Änderungen nötig → Im Editor öffnen")
        print(f"  {BLUE}3.{RESET} Zusammenfassung erneut anzeigen")
        print(f"  {RED}4.{RESET} Abbrechen")

        choice = input(f"\n{CYAN}Auswahl (1-4):{RESET} ").strip()

        if choice == '1':
            # Finale Bestätigung
            if not is_valid:
                print(f"\n{RED}⚠ Modul hat noch Validierungs-Fehler!{RESET}")
                if not prompt_yes_no("Trotzdem finalisieren?", default=False):
                    continue

            if prompt_yes_no(f"Modul {BOLD}{args.name}{RESET} wirklich finalisieren?", default=True):
                print(f"\n{GREEN}✓ Modul bereit zur Finalisierung!{RESET}")
                print(f"\n{BOLD}Nächster Schritt:{RESET}")
                print(f"  python scripts/finalize_module.py --name {args.name}")
                print(f"\n{YELLOW}Optional mit Flags:{RESET}")
                print(f"  --no-git      Keine Git-Commits")
                print(f"  --no-pr       Keinen Pull Request erstellen")
                print(f"  --full        Git + PR (default)")
                return 0

        elif choice == '2':
            # Editor öffnen
            open_editor(draft_path, args.editor)

            # Neu laden
            try:
                draft_data = load_yaml(draft_path)
                print(f"\n{GREEN}✓ DRAFT neu geladen{RESET}")
                print_summary(draft_data, args.verbose)

                # Neu validieren
                is_valid, errors = validate_draft(draft_data, schema)
                if is_valid:
                    print(f"{GREEN}✓ Validierung erfolgreich{RESET}")
                else:
                    print(f"{RED}✗ Validierung fehlgeschlagen{RESET}")
                    for error in errors:
                        print(f"  {RED}•{RESET} {error}")
            except Exception as e:
                print(f"{RED}Fehler beim Neu-Laden: {e}{RESET}")

        elif choice == '3':
            # Zusammenfassung erneut
            print_summary(draft_data, verbose=True)

            # Validierung erneut
            is_valid, errors = validate_draft(draft_data, schema)
            if is_valid:
                print(f"\n{GREEN}✓ Validierung erfolgreich{RESET}")
            else:
                print(f"\n{RED}✗ Validierung fehlgeschlagen{RESET}")

        elif choice == '4':
            # Abbrechen
            print(f"\n{YELLOW}Review abgebrochen. DRAFT bleibt erhalten.{RESET}")
            return 1

        else:
            print(f"{RED}Ungültige Auswahl{RESET}")


if __name__ == '__main__':
    sys.exit(main())
