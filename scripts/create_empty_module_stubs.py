#!/usr/bin/env python3
"""
Create Empty Module Stubs

Erstellt für eine Liste von Modulen leere YAML-Strukturen (Stubs) gemäß Schema,
falls diese noch nicht existieren. Dies ermöglicht es, alle Module vorzubereiten
und sie dann Schritt für Schritt mit Inhalten zu füllen.

Usage:
    python scripts/create_empty_module_stubs.py
    python scripts/create_empty_module_stubs.py --dry-run
"""

import argparse
import sys
import json
import yaml
from pathlib import Path
from typing import Dict, Any, List
from datetime import datetime

# ANSI color codes
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
RED = '\033[91m'
BOLD = '\033[1m'
RESET = '\033[0m'


# Liste der Module (aus User-Anfrage)
MODULES = [
    "app-intro",
    "einstellungen",
    "suche",
    "navigation",
    "merkliste-favoriten",
    "push-nachrichten",
    "nachrichten-informationen",
    "veranstaltungen",
    "bilderslider",
    "statische-seiten",
    "statische-listen-kacheln",
    "schwarzes-brett",
    "stoerer",
    "buergerbeteiligung-consul",
    "feedback-formular",
    "umfragen",
    "terminbuchung",
    "postfach",
    "zustaendigkeitsfinder",
    "rathaus-informationssystem",
    "content-sharing",
    "maengelmelder-einfach",
    "maengelmelder-mit-schnittstelle",
    "hinweisgebersystem",
    "fristenmelder",
    "warnmeldungen",
    "baustellen-verkehrsstoerungen",
    "wetter",
    "wassertemperatur",
    "abfallkalender",
    "oepnv-daten-abfahrtsplaene",
    "datenvisualisierungen",
    "dashboard",
    "branchenbuch-wegweiser",
    "stellenanzeigen",
    "produkte-und-dienstleistungen",
    "gastro-angebote",
    "gutscheine",
    "treueclub-vorteilssystem",
    "karten-standortnutzung",
    "car-bikesharing-angebote",
    "smartes-trampen",
    "gruppen-soziales-netzwerk",
    "persoenliches-profil-bund-id",
    "augmented-reality",
    "chatbot",
    "nutzertracking",
    "webview",
    "widgets"
]


# Topic-Mapping (intelligente Zuordnung basierend auf Modulnamen)
TOPIC_MAPPING = {
    'app-intro': 'hilfe-und-faq',
    'einstellungen': 'hilfe-und-faq',
    'suche': 'hilfe-und-faq',
    'navigation': 'tourismusinformationen',
    'merkliste-favoriten': 'hilfe-und-faq',
    'push-nachrichten': 'push-benachrichtigungen',
    'nachrichten-informationen': 'nachrichten',
    'veranstaltungen': 'veranstaltungskalender',
    'bilderslider': 'tourismusinformationen',
    'statische-seiten': 'nachrichten',
    'statische-listen-kacheln': 'nachrichten',
    'schwarzes-brett': 'nachrichten',
    'stoerer': 'nachrichten',
    'buergerbeteiligung-consul': 'bürgerbeteiligung',
    'feedback-formular': 'feedbackmodul',
    'umfragen': 'bürgerbeteiligung',
    'terminbuchung': 'terminbuchung',
    'postfach': 'bürgerservices',
    'zustaendigkeitsfinder': 'bürgerservices',
    'rathaus-informationssystem': 'kontaktverzeichnis',
    'content-sharing': 'bürgerservices',
    'maengelmelder-einfach': 'maengelmelder',
    'maengelmelder-mit-schnittstelle': 'maengelmelder',
    'hinweisgebersystem': 'maengelmelder',
    'fristenmelder': 'notfallwarnungen',
    'warnmeldungen': 'notfallwarnungen',
    'baustellen-verkehrsstoerungen': 'notfallwarnungen',
    'wetter': 'wetterinformationen',
    'wassertemperatur': 'wetterinformationen',
    'abfallkalender': 'abfallkalender',
    'oepnv-daten-abfahrtsplaene': 'oepnv-auskunft',
    'datenvisualisierungen': 'nachrichten',
    'dashboard': 'nachrichten',
    'branchenbuch-wegweiser': 'branchenverzeichnis',
    'stellenanzeigen': 'stellenangebote',
    'produkte-und-dienstleistungen': 'marktplatz',
    'gastro-angebote': 'tourismusinformationen',
    'gutscheine': 'marktplatz',
    'treueclub-vorteilssystem': 'marktplatz',
    'karten-standortnutzung': 'tourismusinformationen',
    'car-bikesharing-angebote': 'mobilitätsdienste',
    'smartes-trampen': 'mobilitätsdienste',
    'gruppen-soziales-netzwerk': 'sozialdienste',
    'persoenliches-profil-bund-id': 'bürgerservices',
    'augmented-reality': 'tourismusinformationen',
    'chatbot': 'hilfe-und-faq',
    'nutzertracking': 'hilfe-und-faq',
    'webview': 'nachrichten',
    'widgets': 'nachrichten'
}


def load_schema(schema_path: Path) -> Dict[str, Any]:
    """Lädt das JSON Schema."""
    with open(schema_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def create_empty_stub(name: str, schema: Dict[str, Any]) -> Dict[str, Any]:
    """Erstellt leere Modul-Struktur gemäß Schema."""

    # Bestimme Topic
    topic = TOPIC_MAPPING.get(name, 'nachrichten')  # Default: nachrichten

    # Erstelle Stub mit Pflichtfeldern (minimal ausgefüllt)
    stub = {
        'name': name,
        'topic': topic,
        'short_description': '[TODO: Kurzbeschreibung ergänzen]',
        'usage_scenario': '[TODO: Hauptszenario beschreiben]',
        'description': f'[TODO: Ausführliche Beschreibung für {name} ergänzen]'
    }

    # Füge optionale Felder als Kommentare/Platzhalter hinzu
    # (werden nicht ins YAML geschrieben, um es minimal zu halten)

    return stub


def check_existing_modules(modules_dir: Path, yml_dir: Path) -> Dict[str, str]:
    """Prüft welche Module bereits existieren."""
    status = {}

    for module in MODULES:
        partial_exists = (modules_dir / f"{module}.yml").exists()
        draft_exists = (modules_dir / f"DRAFT-{module}.yml").exists()
        complete_exists = (yml_dir / f"{module}.yml").exists()

        if complete_exists:
            status[module] = 'complete'
        elif partial_exists:
            status[module] = 'partial'
        elif draft_exists:
            status[module] = 'draft'
        else:
            status[module] = 'missing'

    return status


def create_stub_file(name: str, stub_data: Dict[str, Any], modules_dir: Path) -> Path:
    """Erstellt STUB-Datei mit Header."""
    stub_path = modules_dir / f"STUB-{name}.yml"

    header = f"""# STUB MODULE: {name}
# Status: LEER - Muss noch ausgefüllt werden
#
# Dies ist eine leere Struktur gemäß Schema. Bitte ausfüllen:
# 1. Kurzbeschreibung (short_description)
# 2. Hauptszenario (usage_scenario)
# 3. Ausführliche Beschreibung (description)
# 4. Optionale Felder ergänzen (interfaces, dependencies, etc.)
#
# Nach dem Ausfüllen:
# 1. Datei umbenennen von STUB-{name}.yml zu {name}.yml
# 2. Review: python scripts/review_module.py --name {name}
# 3. Finalisierung: python scripts/finalize_module.py --name {name} --full
#
# Erstellt am: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

"""

    with open(stub_path, 'w', encoding='utf-8') as f:
        f.write(header)
        yaml.dump(stub_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

    return stub_path


def main():
    parser = argparse.ArgumentParser(
        description='Erstellt leere Modul-Stubs für fehlende Module',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('--dry-run', action='store_true',
                       help='Zeigt nur, was erstellt würde (ohne Dateien zu schreiben)')

    args = parser.parse_args()

    # Paths
    root_dir = Path(__file__).parent.parent
    schema_path = root_dir / 'schema' / 'app-module.schema.json'
    modules_dir = root_dir / 'yml' / 'modules'
    yml_dir = root_dir / 'yml'

    print(f"{BOLD}{CYAN}=== Create Empty Module Stubs ==={RESET}\n")

    if args.dry_run:
        print(f"{YELLOW}DRY-RUN Modus: Keine Dateien werden erstellt{RESET}\n")

    # Lade Schema
    try:
        schema = load_schema(schema_path)
    except Exception as e:
        print(f"{RED}Fehler beim Laden des Schemas: {e}{RESET}")
        return 1

    # Prüfe Status aller Module
    print(f"{BOLD}Prüfe Status von {len(MODULES)} Modulen...{RESET}\n")
    status = check_existing_modules(modules_dir, yml_dir)

    # Statistiken
    complete = sum(1 for s in status.values() if s == 'complete')
    partial = sum(1 for s in status.values() if s == 'partial')
    draft = sum(1 for s in status.values() if s == 'draft')
    missing = sum(1 for s in status.values() if s == 'missing')

    print(f"{BOLD}Status-Übersicht:{RESET}")
    print(f"  {GREEN}✓{RESET} Vollständig: {complete}")
    print(f"  {BLUE}◐{RESET} Partial vorhanden: {partial}")
    print(f"  {YELLOW}◔{RESET} Draft vorhanden: {draft}")
    print(f"  {RED}○{RESET} Fehlend: {missing}")
    print()

    # Zeige fehlende Module
    missing_modules = [name for name, s in status.items() if s == 'missing']

    if not missing_modules:
        print(f"{GREEN}✓ Alle Module haben bereits eine Datei!{RESET}")
        return 0

    print(f"{BOLD}Fehlende Module ({len(missing_modules)}):{RESET}")
    for module in missing_modules:
        topic = TOPIC_MAPPING.get(module, 'nachrichten')
        print(f"  {RED}○{RESET} {module} (Topic: {CYAN}{topic}{RESET})")
    print()

    # Erstelle Stubs
    if not args.dry_run:
        print(f"{BOLD}Erstelle Stubs...{RESET}\n")
        created = []

        for module in missing_modules:
            try:
                stub_data = create_empty_stub(module, schema)
                stub_path = create_stub_file(module, stub_data, modules_dir)
                created.append(module)
                print(f"{GREEN}✓{RESET} Erstellt: {CYAN}STUB-{module}.yml{RESET}")
            except Exception as e:
                print(f"{RED}✗{RESET} Fehler bei {module}: {e}")

        print(f"\n{BOLD}{GREEN}=== Fertig ==={RESET}")
        print(f"\n{GREEN}✓{RESET} {len(created)} Stubs erstellt")
        print(f"\n{BOLD}Nächste Schritte:{RESET}")
        print(f"1. Öffne die STUB-Dateien in {CYAN}yml/modules/{RESET}")
        print(f"2. Fülle die TODO-Felder aus")
        print(f"3. Benenne STUB-[name].yml → [name].yml um")
        print(f"4. Review: {BOLD}python scripts/review_module.py --name [module]{RESET}")
        print(f"5. Finalisierung: {BOLD}python scripts/finalize_module.py --name [module] --full{RESET}")
    else:
        print(f"\n{YELLOW}Im DRY-RUN Modus würden {len(missing_modules)} Stubs erstellt werden.{RESET}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
