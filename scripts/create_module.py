#!/usr/bin/env python3
"""
Interactive module creation tool for Smart Village App modules.

This script guides users through creating a new module description with:
- Interactive prompts for all necessary fields
- Git workflow (feature branch creation)
- Automatic generation of complete YAML
- Conventional commits
- GitHub PR creation (if gh CLI available)
"""

import os
import sys
import json
import yaml
import subprocess
from pathlib import Path
from datetime import datetime

# Color codes for terminal output
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_header(text):
    """Print a formatted header"""
    print(f"\n{Colors.BLUE}{Colors.BOLD}{'=' * 70}{Colors.END}")
    print(f"{Colors.BLUE}{Colors.BOLD}  {text}{Colors.END}")
    print(f"{Colors.BLUE}{Colors.BOLD}{'=' * 70}{Colors.END}\n")

def print_success(text):
    """Print success message"""
    print(f"{Colors.GREEN}✓ {text}{Colors.END}")

def print_error(text):
    """Print error message"""
    print(f"{Colors.RED}✗ {text}{Colors.END}")

def print_info(text):
    """Print info message"""
    print(f"{Colors.CYAN}ℹ {text}{Colors.END}")

def print_warning(text):
    """Print warning message"""
    print(f"{Colors.YELLOW}⚠ {text}{Colors.END}")

def run_command(cmd, cwd=None):
    """Run shell command and return output"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True
        )
        return result.returncode == 0, result.stdout.strip(), result.stderr.strip()
    except Exception as e:
        return False, "", str(e)

def get_project_root():
    """Get the project root directory"""
    return Path(__file__).parent.parent

def load_schema(schema_path):
    """Load JSON schema"""
    with open(schema_path, 'r') as f:
        return json.load(f)

def get_topic_choices(schema):
    """Extract topic enum values from schema"""
    return schema.get('properties', {}).get('topic', {}).get('enum', [])

def prompt_input(prompt, required=True, default=None):
    """Prompt user for input"""
    suffix = f" [{default}]" if default else ""
    suffix += ": " if required else " (optional): "

    while True:
        value = input(f"{Colors.CYAN}{prompt}{suffix}{Colors.END}").strip()

        if not value and default:
            return default

        if not value and not required:
            return None

        if value or not required:
            return value

        print_error("Dieses Feld ist erforderlich!")

def prompt_multiline(prompt):
    """Prompt user for multiline input"""
    print(f"{Colors.CYAN}{prompt}{Colors.END}")
    print(f"{Colors.YELLOW}(Beende mit einer Leerzeile){Colors.END}")

    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)

    return "\n".join(lines) if lines else None

def prompt_choice(prompt, choices):
    """Prompt user to select from choices"""
    print(f"\n{Colors.CYAN}{prompt}{Colors.END}")

    # Display choices in columns
    for i, choice in enumerate(choices, 1):
        print(f"  {i:2}. {choice}")

    while True:
        try:
            selection = input(f"\n{Colors.CYAN}Wähle Nummer [1-{len(choices)}]: {Colors.END}").strip()
            index = int(selection) - 1

            if 0 <= index < len(choices):
                return choices[index]

            print_error(f"Bitte eine Zahl zwischen 1 und {len(choices)} eingeben!")
        except ValueError:
            print_error("Bitte eine gültige Zahl eingeben!")

def prompt_list(prompt, example=None):
    """Prompt user for list input"""
    print(f"\n{Colors.CYAN}{prompt}{Colors.END}")
    if example:
        print(f"{Colors.YELLOW}Beispiel: {example}{Colors.END}")
    print(f"{Colors.YELLOW}(Eine pro Zeile, Leerzeile zum Beenden){Colors.END}")

    items = []
    while True:
        item = input(f"  - ").strip()
        if not item:
            break
        items.append(item)

    return items if items else None

def confirm(prompt, default=True):
    """Prompt user for yes/no confirmation"""
    suffix = " [Y/n]" if default else " [y/N]"
    response = input(f"{Colors.CYAN}{prompt}{suffix}: {Colors.END}").strip().lower()

    if not response:
        return default

    return response in ['y', 'yes', 'ja', 'j']

def create_git_branch(module_name):
    """Create Git feature branch"""
    branch_name = f"feature/module-{module_name}"

    success, _, error = run_command(f"git checkout -b {branch_name}")

    if success:
        print_success(f"Git-Branch erstellt: {branch_name}")
        return branch_name
    else:
        print_error(f"Branch konnte nicht erstellt werden: {error}")
        return None

def git_commit(message, files):
    """Create a Git commit"""
    # Stage files
    for file in files:
        run_command(f"git add {file}")

    # Commit
    success, _, error = run_command(f'git commit -m "{message}"')

    if success:
        print_success(f"Commit erstellt: {message}")
        return True
    else:
        print_error(f"Commit fehlgeschlagen: {error}")
        return False

def create_pull_request(branch_name, module_name):
    """Create GitHub pull request using gh CLI"""
    # Check if gh CLI is available
    success, _, _ = run_command("gh --version")

    if not success:
        print_warning("GitHub CLI (gh) ist nicht installiert")
        print_info("PR manuell erstellen: https://github.com/smart-village-solutions/smart-village-app-admin-doku/compare")
        return False

    # Create PR
    title = f"feat(module): Add {module_name} module description"
    body = f"""## Neues Modul: {module_name}

Diese PR fügt die Modulbeschreibung für **{module_name}** hinzu.

### Änderungen
- ✅ Modul-Partial erstellt (`yml/modules/{module_name}.yml`)
- ✅ Vollständige YAML generiert (`yml/{module_name}.yml`)
- ✅ In `city_app.yml` registriert

### Validierung
- [ ] Schema-Validierung durchgeführt
- [ ] Inhalte geprüft
- [ ] Screenshots hinzugefügt (falls verfügbar)

Generiert mit `create_module.py`
"""

    cmd = f'gh pr create --title "{title}" --body "{body}" --base main'
    success, output, error = run_command(cmd)

    if success:
        print_success("Pull Request erstellt!")
        print_info(f"URL: {output}")
        return True
    else:
        print_error(f"PR konnte nicht erstellt werden: {error}")
        return False

def collect_module_data(schema):
    """Interactively collect module data from user"""
    print_header("Modul-Informationen")

    data = {}

    # Required fields
    data['name'] = prompt_input("Modulname (z.B. 'Abfallkalender')")

    # Topic selection
    topics = get_topic_choices(schema)
    data['topic'] = prompt_choice("Thema/Kategorie auswählen", topics)

    data['short_description'] = prompt_input("Kurzbeschreibung (eine Zeile)")

    data['last_update'] = datetime.now().strftime("%Y-%m-%d")

    # Optional multiline fields
    print_header("Detaillierte Beschreibungen")

    if confirm("Nutzungsszenario hinzufügen?"):
        data['usage_scenario'] = prompt_multiline("Nutzungsszenario (Markdown)")

    if confirm("Detaillierte Beschreibung hinzufügen?"):
        data['description'] = prompt_multiline("Beschreibung (Markdown)")

    # Optional list fields
    print_header("Technische Details")

    if confirm("Schnittstellen hinzufügen?"):
        data['interfaces'] = prompt_list(
            "Schnittstellen",
            "REST-API, GraphQL, WebSocket"
        )

    if confirm("Abhängigkeiten hinzufügen?"):
        data['dependencies'] = prompt_list(
            "Abhängigkeiten",
            "Push-Benachrichtigungen, Authentifizierung"
        )

    if confirm("Externe Services hinzufügen?"):
        services = []
        while True:
            service_name = prompt_input("Service-Name", required=False)
            if not service_name:
                break

            service_desc = prompt_input("Service-Beschreibung")
            services.append({
                'name': service_name,
                'description': service_desc
            })

            if not confirm("Weiteren Service hinzufügen?", default=False):
                break

        if services:
            data['external_services'] = services

    if confirm("Anpassungsoptionen hinzufügen?"):
        data['customization_options'] = prompt_list(
            "Anpassungsoptionen",
            "Farbschema, Logo, Benachrichtigungen"
        )

    # Actors
    print_header("Beteiligte Akteure")

    if confirm("Akteure hinzufügen?"):
        actors = []
        while True:
            actor_name = prompt_input("Akteur-Name", required=False)
            if not actor_name:
                break

            actor_role = prompt_input("Rolle/Aufgabe")
            actors.append({
                'name': actor_name,
                'role': actor_role
            })

            if not confirm("Weiteren Akteur hinzufügen?", default=False):
                break

        if actors:
            data['involved_actors'] = actors

    return data

def main():
    """Main execution"""
    print_header("Smart Village App - Modul erstellen")

    project_root = get_project_root()
    schema_path = project_root / "schema" / "app-module.schema.json"

    # Load schema
    print_info("Lade Schema...")
    schema = load_schema(schema_path)

    # Collect data
    module_data = collect_module_data(schema)

    module_name = module_data['name'].lower().replace(' ', '-')
    module_file = project_root / "yml" / "modules" / f"{module_name}.yml"

    # Show summary
    print_header("Zusammenfassung")
    print(f"Modulname: {module_data['name']}")
    print(f"Topic: {module_data['topic']}")
    print(f"Datei: yml/modules/{module_name}.yml")
    print()

    if not confirm("Modul erstellen?"):
        print_info("Abgebrochen")
        return

    # Git workflow
    print_header("Git Workflow")

    if confirm("Git-Branch erstellen?"):
        branch_name = create_git_branch(module_name)
        if not branch_name:
            print_error("Branch-Erstellung fehlgeschlagen - Workflow abgebrochen")
            return
    else:
        branch_name = None
        print_warning("Kein Branch erstellt - arbeite auf aktuellem Branch")

    # Save module data
    print_info(f"Speichere Modul-Datei...")
    module_file.parent.mkdir(parents=True, exist_ok=True)

    with open(module_file, 'w') as f:
        yaml.dump(module_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print_success(f"Datei erstellt: {module_file}")

    # Commit 1: Add module partial
    if branch_name:
        git_commit(
            f"feat(module): add {module_name} partial",
            [str(module_file.relative_to(project_root))]
        )

    # Generate complete YAML
    print_header("YAML Generierung")
    print_info("Führe generate_module_yaml.py aus...")

    success, output, error = run_command(
        f"python3 scripts/generate_module_yaml.py --module {module_name}",
        cwd=project_root
    )

    if success:
        print_success("YAML erfolgreich generiert")
        print(output)

        # Commit 2: Add generated YAML
        if branch_name:
            git_commit(
                f"feat(module): generate {module_name} complete YAML",
                [f"yml/{module_name}.yml"]
            )

        # Commit 3: Update city_app.yml
        if branch_name:
            git_commit(
                f"feat(module): register {module_name} in city_app.yml",
                ["city_app.yml"]
            )
    else:
        print_error(f"YAML-Generierung fehlgeschlagen:\n{error}")
        return

    # Create PR
    if branch_name:
        print_header("Pull Request")

        if confirm("Pull Request erstellen?"):
            create_pull_request(branch_name, module_data['name'])
        else:
            print_info(f"PR manuell erstellen mit: gh pr create --base main")

    print_header("Fertig!")
    print_success(f"Modul '{module_data['name']}' wurde erfolgreich erstellt")

    if branch_name:
        print_info(f"Branch: {branch_name}")
        print_info("Next: Review PR und merge in main")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n")
        print_warning("Abgebrochen durch Benutzer")
        sys.exit(1)
    except Exception as e:
        print_error(f"Fehler: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
