# Project Context

## Purpose

This project provides comprehensive documentation for the Smart Village App - an open-source, modular application platform for municipalities. The documentation covers:

- **User Documentation**: Guides for administrators, editors, and end-users
- **Developer Documentation**: Technical setup, API references, and contribution guidelines
- **Module Documentation**: Detailed specifications for app modules (news, events, etc.)
- **Schema Definitions**: JSON Schema files for validating YAML configuration files

The documentation is built with MkDocs and serves as the central knowledge base for the Smart Village App ecosystem.

## Tech Stack

- **Documentation Generator**: MkDocs (Python-based static site generator)
- **Content Format**: Markdown (.md files)
- **Configuration**: YAML (.yml files)
- **Schema Validation**: JSON Schema (Draft 7)
- **Validation Scripts**: Python 3
- **Version Control**: Git
- **Hosting**: GitHub Pages
- **Repository**: GitLab (OpenCode.de) and GitHub (documentation)

### Key Dependencies
- `mkdocs` - Documentation site generator
- `pyyaml` - YAML file processing
- `jsonschema` - Schema validation

## Project Conventions

### Code Style

**Markdown Files:**
- Use ATX-style headings (`#`, `##`, `###`)
- Maintain blank lines around headings and lists
- Use fenced code blocks with language identifiers
- Follow German language for user-facing documentation
- Use English for technical/developer documentation

**YAML Files:**
- Use 2-space indentation
- Follow schema definitions strictly
- Include descriptive comments where helpful
- Use ISO 8601 date format (YYYY-MM-DD)

**Python Scripts:**
- Follow PEP 8 style guide
- Use type hints where applicable
- Include docstrings for functions and classes
- Use descriptive variable and function names

### Architecture Patterns

**Documentation Structure:**
```
docs/
├── index.md              # Landing page
├── einleitung/           # Introduction and overview
├── admins/               # Admin documentation
├── redaktion/            # Editor documentation
├── dev/                  # Developer documentation
├── module/               # Module specifications
├── kommunen/             # Municipality guidance
└── kontakt/              # Contact and support
```

**Schema-Driven Configuration:**
- All YAML files must validate against corresponding JSON schemas
- Two main schemas:
  - `city-app-schema.json` - For city app configurations
  - `app-module.schema.json` - For module definitions

**Validation Workflow:**
- Use `validate_schemas.py` to check all YAML files before commits
- Schemas define optional and required fields
- Maintain backward compatibility when updating schemas

### Testing Strategy

**Schema Validation:**
- Run `validate_schemas.py` before committing changes
- All YAML files must pass validation
- Exit code 0 indicates success, 1 indicates failures

**Documentation Testing:**
- Build documentation locally with `mkdocs serve`
- Verify all internal links work
- Check rendering of code blocks and formatting

**Manual Review:**
- Peer review for content accuracy
- Check for broken links and images
- Verify examples and code snippets

### Git Workflow

**Commit Conventions:**
- Use Conventional Commits format: `type(scope): description`
- Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
- Examples:
  - `feat(schema): Add roadmap field to app-module schema`
  - `docs(module): Update news module documentation`
  - `fix(validation): Correct YAML parsing error`

**Branch Strategy:**
- `main` - Production-ready documentation
- Feature branches for significant changes
- Create pull requests for review

## Domain Context

**Smart Village App Ecosystem:**
- Open-source platform for digital municipal services
- Modular architecture with pluggable features
- Serves 40+ municipalities in Germany
- Built on React Native (mobile apps) and Ruby on Rails (backend)

**Key Concepts:**
- **Module**: A functional unit providing specific features (news, events, feedback, etc.)
- **City App**: A configured instance for a specific municipality
- **Data Provider**: External sources feeding content into the app
- **Roadmap**: Planned features for future development

**User Roles:**
- **Administrators**: System configuration and user management
- **Editors/Redakteure**: Content creation and publication
- **Citizens**: End-users consuming information and services
- **Developers**: Contributing to the open-source project

## Important Constraints

**Technical Constraints:**
- All schemas must be JSON Schema Draft 7 compliant
- YAML files must use UTF-8 encoding
- Documentation must be accessible (WCAG guidelines)
- Maintain backward compatibility in schema changes

**Content Constraints:**
- Primary language: German (for user documentation)
- Technical docs may use English
- Follow municipal communication standards
- Respect data privacy regulations (DSGVO/GDPR)

**Licensing:**
- Documentation: Open licensing model
- Smart Village App: GNU GPL v3
- Ensure all content can be freely shared and modified

## External Dependencies

**Documentation Platform:**
- MkDocs Material theme for enhanced UI
- GitHub Pages for hosting
- GitLab OpenCode for source code repository

**Smart Village App Components:**
- **Backend**: Ruby on Rails GraphQL API
- **Frontend**: React Native mobile apps (iOS/Android)
- **CMS**: Content management interface
- **Keycloak**: Authentication and user management
- **MinIO**: Object storage for media files
- **PostgreSQL**: Database backend

**External Services:**
- RSS/Atom feeds for news aggregation
- iCal/ICS for event imports
- OpenStreetMap for mapping features
- Various municipal APIs and data sources
