#!/usr/bin/env python3
"""
Schema Validator for Smart Village App Documentation

This script validates YAML files against their corresponding JSON schemas:
- city_app.yml against city-app-schema.json
- All yml/*.yml files against app-module.schema.json (default)
- With --minimal: validates only nachrichten.yml and veranstaltungen.yml (legacy mode)
"""

import sys
import yaml
import json
import jsonschema
import argparse
from jsonschema import validate, ValidationError
from pathlib import Path
from typing import Tuple, List


class Colors:
    """ANSI color codes for terminal output"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'


def load_yaml(file_path: Path) -> dict:
    """Load and parse a YAML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"{Colors.RED}✗ Error loading {file_path}: {e}{Colors.END}")
        return None


def load_schema(schema_path: Path) -> dict:
    """Load and parse a JSON schema file"""
    try:
        with open(schema_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"{Colors.RED}✗ Error loading schema {schema_path}: {e}{Colors.END}")
        return None


def validate_file(yaml_path: Path, schema_path: Path) -> Tuple[bool, str]:
    """
    Validate a YAML file against a JSON schema

    Returns:
        Tuple[bool, str]: (success, error_message)
    """
    yaml_data = load_yaml(yaml_path)
    if yaml_data is None:
        return False, "Failed to load YAML file"

    schema = load_schema(schema_path)
    if schema is None:
        return False, "Failed to load schema"

    try:
        validate(instance=yaml_data, schema=schema)
        return True, ""
    except ValidationError as e:
        path = " → ".join(str(x) for x in e.absolute_path) if e.absolute_path else "root"
        error_msg = f"Path: {path}\nError: {e.message}"
        if hasattr(e, 'instance') and len(str(e.instance)) < 100:
            error_msg += f"\nValue: {e.instance}"
        return False, error_msg
    except Exception as e:
        return False, f"Unexpected error: {e}"


def main():
    """Main validation function"""
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='Validate YAML files against JSON schemas',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        '--minimal',
        action='store_true',
        help='Validate only nachrichten.yml and veranstaltungen.yml (legacy mode)'
    )
    args = parser.parse_args()

    print(f"{Colors.BOLD}{Colors.BLUE}{'=' * 70}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}Schema Validation for Smart Village App Documentation{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'=' * 70}{Colors.END}\n")

    # Define base directory
    base_dir = Path(__file__).parent

    # Define validation tasks
    validation_tasks = [
        {
            'name': 'City App Configuration',
            'yaml': base_dir / 'city_app.yml',
            'schema': base_dir / 'schema' / 'city-app-schema.json'
        }
    ]

    if args.minimal:
        # Validate only default module files (legacy mode)
        validation_tasks.extend([
            {
                'name': 'Nachrichten Module',
                'yaml': base_dir / 'yml' / 'nachrichten.yml',
                'schema': base_dir / 'schema' / 'app-module.schema.json'
            },
            {
                'name': 'Veranstaltungen Module',
                'yaml': base_dir / 'yml' / 'veranstaltungen.yml',
                'schema': base_dir / 'schema' / 'app-module.schema.json'
            }
        ])
    else:
        # Validate all yml/*.yml files (default)
        module_schema = base_dir / 'schema' / 'app-module.schema.json'
        yml_dir = base_dir / 'yml'

        if yml_dir.exists():
            yaml_files = sorted(yml_dir.glob('*.yml'))
            print(f"{Colors.BLUE}Validating all module YAML files in yml/ directory...{Colors.END}\n")

            for yaml_file in yaml_files:
                # Skip global.yml as it's only a template, not a complete module
                if yaml_file.name == 'global.yml':
                    print(f"{Colors.YELLOW}Skipping: {yaml_file.name} (template file){Colors.END}\n")
                    continue

                validation_tasks.append({
                    'name': f'Module: {yaml_file.stem}',
                    'yaml': yaml_file,
                    'schema': module_schema
                })

    results: List[Tuple[str, bool, str]] = []

    # Validate each file
    for task in validation_tasks:
        print(f"{Colors.BOLD}Validating: {task['name']}{Colors.END}")
        print(f"  File:   {task['yaml'].name}")
        print(f"  Schema: {task['schema'].name}")

        success, error = validate_file(task['yaml'], task['schema'])
        results.append((task['name'], success, error))

        if success:
            print(f"  {Colors.GREEN}✓ Validation successful{Colors.END}\n")
        else:
            print(f"  {Colors.RED}✗ Validation failed{Colors.END}")
            print(f"  {Colors.YELLOW}{error}{Colors.END}\n")

    # Print summary
    print(f"{Colors.BOLD}{Colors.BLUE}{'=' * 70}{Colors.END}")
    print(f"{Colors.BOLD}Validation Summary{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'=' * 70}{Colors.END}\n")

    success_count = sum(1 for _, success, _ in results if success)
    total_count = len(results)

    for name, success, _ in results:
        status = f"{Colors.GREEN}✓ PASS{Colors.END}" if success else f"{Colors.RED}✗ FAIL{Colors.END}"
        print(f"  {status}  {name}")

    print(f"\n{Colors.BOLD}Result: {success_count}/{total_count} validations passed{Colors.END}\n")

    # Exit with appropriate code
    if success_count == total_count:
        print(f"{Colors.GREEN}{Colors.BOLD}All validations successful! 🎉{Colors.END}\n")
        sys.exit(0)
    else:
        print(f"{Colors.RED}{Colors.BOLD}Some validations failed. Please check the errors above.{Colors.END}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
