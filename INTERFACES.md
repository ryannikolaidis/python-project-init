# Interface Index

This document links to all public interfaces in the python-project-init codebase.

## CLI Interfaces

- [**ProjectInitCLI**](docs/interfaces/ProjectInitCLI.md) - Main command-line interface for project initialization

## Core Interfaces

- [**ProjectConfig**](docs/interfaces/ProjectConfig.md) - Project configuration data structure
- [**TemplateEngine**](docs/interfaces/TemplateEngine.md) - Jinja2 template processing engine
- [**ProjectGenerator**](docs/interfaces/ProjectGenerator.md) - Main project generation orchestrator
- [**ConfigManager**](docs/interfaces/ConfigManager.md) - YAML configuration management

## Interface Stability

- **stable**: Ready for production use, changes will be backward compatible
- **experimental**: Under active development, breaking changes possible

## Finding Interfaces

All interfaces are marked in the code with annotations like:

```python
# @interface InterfaceName | stability:stable | owner:@username
```

Use grep to find them:

```bash
grep -r "@interface" python_project_init/
```