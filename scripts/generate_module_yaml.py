#!/usr/bin/env python3
"""
Module YAML Generator for Smart Village App Documentation

This script generates complete YAML module files by merging:
1. Global common data from yml/global.yml
2. Module-specific data from yml/modules/[name].yml

It also automatically registers modules in city_app.yml.
"""

import sys
import yaml
import json
import argparse
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime
import jsonschema
from jsonschema import validate, ValidationError


class Colors:
    """ANSI color codes for terminal output"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'


def load_yaml(file_path: Path) -> Optional[Dict[str, Any]]:
    """Load and parse a YAML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"{Colors.RED}✗ Error loading {file_path}: {e}{Colors.END}")
        return None


def save_yaml(data: Dict[str, Any], file_path: Path, header_comment: str = None) -> bool:
    """Save data to YAML file with optional header comment"""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            if header_comment:
                f.write(header_comment + '\n\n')
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        return True
    except Exception as e:
        print(f"{Colors.RED}✗ Error saving {file_path}: {e}{Colors.END}")
        return False


def load_schema(schema_path: Path) -> Optional[Dict[str, Any]]:
    """Load JSON schema for validation"""
    try:
        with open(schema_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"{Colors.RED}✗ Error loading schema {schema_path}: {e}{Colors.END}")
        return None


def validate_against_schema(data: Dict[str, Any], schema: Dict[str, Any]) -> tuple[bool, str]:
    """Validate YAML data against JSON schema"""
    try:
        validate(instance=data, schema=schema)
        return True, ""
    except ValidationError as e:
        path = " → ".join(str(x) for x in e.absolute_path) if e.absolute_path else "root"
        error_msg = f"Path: {path}\nError: {e.message}"
        return False, error_msg
    except Exception as e:
        return False, f"Unexpected error: {e}"


def merge_module_data(global_data: Dict[str, Any], module_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge global and module-specific data.
    Module values override global values.

    Priority:
    1. Module-specific values (highest)
    2. Global common values
    3. Schema defaults (lowest)
    """
    result = {}

    # Start with global common values
    if 'common' in global_data:
        result.update(global_data['common'])

    # Override with module-specific values
    result.update(module_data)

    # Build technical_documentation URL if base exists and not overridden
    if 'technical_documentation_base' in result and 'technical_documentation' not in module_data:
        base_url = result.pop('technical_documentation_base')
        module_name = module_data.get('name', '').lower().replace(' ', '-').replace('/', '-')
        result['technical_documentation'] = f"{base_url}/{module_name}"
    else:
        result.pop('technical_documentation_base', None)

    return result


def register_in_city_app(module_name: str, city_app_path: Path, repo_base_url: str) -> bool:
    """
    Register module in city_app.yml if not already present.
    Preserves YAML structure and comments.
    """
    try:
        # Load city_app.yml preserving comments
        with open(city_app_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Build module URL
        module_url = f"{repo_base_url}/yml/{module_name}.yml"

        # Check if already registered
        for line in lines:
            if module_url in line:
                print(f"  {Colors.YELLOW}ℹ Module already registered in city_app.yml{Colors.END}")
                return True

        # Find modules: section and add entry
        in_modules_section = False
        insert_index = None

        for i, line in enumerate(lines):
            if line.strip().startswith('modules:'):
                in_modules_section = True
            elif in_modules_section and line.strip().startswith('-'):
                insert_index = i + 1
            elif in_modules_section and line.strip() and not line.strip().startswith('#') and not line.strip().startswith('-'):
                # End of modules section
                break

        if insert_index is None:
            # No modules found, add after modules: line
            for i, line in enumerate(lines):
                if line.strip().startswith('modules:'):
                    insert_index = i + 1
                    break

        if insert_index is not None:
            # Insert new module URL
            new_line = f'  - "{module_url}"\n'
            lines.insert(insert_index, new_line)

            # Save updated file
            with open(city_app_path, 'w', encoding='utf-8') as f:
                f.writelines(lines)

            print(f"  {Colors.GREEN}✓ Registered module in city_app.yml{Colors.END}")
            return True
        else:
            print(f"  {Colors.RED}✗ Could not find modules: section in city_app.yml{Colors.END}")
            return False

    except Exception as e:
        print(f"  {Colors.RED}✗ Error registering in city_app.yml: {e}{Colors.END}")
        return False


def generate_module(module_name: str, base_dir: Path, register_city_app: bool = True) -> bool:
    """Generate a complete module YAML file from sources"""

    print(f"\n{Colors.BOLD}{Colors.BLUE}Generating module: {module_name}{Colors.END}")

    # Paths
    global_yml = base_dir / 'yml' / 'global.yml'
    module_yml = base_dir / 'yml' / 'modules' / f'{module_name}.yml'
    output_yml = base_dir / 'yml' / f'{module_name}.yml'
    schema_json = base_dir / 'schema' / 'app-module.schema.json'
    city_app_yml = base_dir / 'city_app.yml'

    # Load global data
    print(f"  Loading global data...")
    global_data = load_yaml(global_yml)
    if global_data is None:
        return False

    # Load module data
    print(f"  Loading module data...")
    if not module_yml.exists():
        print(f"  {Colors.RED}✗ Module file not found: {module_yml}{Colors.END}")
        return False

    module_data = load_yaml(module_yml)
    if module_data is None:
        return False

    # Merge data
    print(f"  Merging data...")
    merged_data = merge_module_data(global_data, module_data)

    # Load schema
    print(f"  Loading schema...")
    schema = load_schema(schema_json)
    if schema is None:
        return False

    # Validate
    print(f"  Validating against schema...")
    is_valid, error = validate_against_schema(merged_data, schema)
    if not is_valid:
        print(f"  {Colors.RED}✗ Validation failed:{Colors.END}")
        print(f"  {Colors.YELLOW}{error}{Colors.END}")
        return False

    # Generate header comment
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = f"""# AUTO-GENERATED FROM yml/modules/{module_name}.yml + yml/global.yml
# DO NOT EDIT THIS FILE DIRECTLY - Edit the source files instead
# Last generated: {timestamp}"""

    # Save merged YAML
    print(f"  Writing output file...")
    if not save_yaml(merged_data, output_yml, header):
        return False

    print(f"  {Colors.GREEN}✓ Generated: {output_yml}{Colors.END}")

    # Register in city_app.yml
    if register_city_app and city_app_yml.exists():
        print(f"  Registering in city_app.yml...")
        repo_base = "https://raw.githubusercontent.com/smart-village-solutions/smart-village-app-admin-doku/main"
        register_in_city_app(module_name, city_app_yml, repo_base)

    return True


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Generate complete module YAML files from global and module-specific sources'
    )
    parser.add_argument(
        '--module', '-m',
        help='Module name (without .yml extension)'
    )
    parser.add_argument(
        '--all', '-a',
        action='store_true',
        help='Generate all modules in yml/modules/'
    )
    parser.add_argument(
        '--no-register',
        action='store_true',
        help='Skip registering in city_app.yml'
    )

    args = parser.parse_args()

    base_dir = Path(__file__).parent.parent

    print(f"{Colors.BOLD}{Colors.BLUE}{'=' * 70}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}Module YAML Generator{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'=' * 70}{Colors.END}")

    if args.all:
        # Generate all modules
        modules_dir = base_dir / 'yml' / 'modules'
        module_files = sorted(modules_dir.glob('*.yml'))

        if not module_files:
            print(f"\n{Colors.YELLOW}No module files found in {modules_dir}{Colors.END}")
            return 1

        print(f"\nFound {len(module_files)} module(s) to generate\n")

        success_count = 0
        for module_file in module_files:
            module_name = module_file.stem
            if generate_module(module_name, base_dir, not args.no_register):
                success_count += 1

        print(f"\n{Colors.BOLD}{'=' * 70}{Colors.END}")
        print(f"{Colors.BOLD}Summary: {success_count}/{len(module_files)} modules generated successfully{Colors.END}")

        return 0 if success_count == len(module_files) else 1

    elif args.module:
        # Generate single module
        success = generate_module(args.module, base_dir, not args.no_register)
        return 0 if success else 1

    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
