# ProjectConfig

- **Stability:** stable
- **Owner:** @ryannikolaidis
- **Location:** project_init/models.py
- **Summary:** Data structure that holds all project configuration and metadata, with conversion to template variables.

## Inputs/Outputs

**Inputs:**
- Project metadata from user input or programmatic creation

**Outputs:**
- Structured configuration data
- Template variables dictionary via `to_template_vars()`

## Examples

```python
from project_init.models import ProjectConfig
from pathlib import Path

config = ProjectConfig(
    project_name="my-awesome-project",
    project_type="python",
    description="A Python project",
    author_name="John Doe",
    author_email="john@example.com",
    github_username="johndoe",
    target_directory=Path("./my-awesome-project"),
    python_version="3.12",
    package_name="my_awesome_project",
    entry_point=True,
    extra_context={},
)

# Get template variables
variables = config.to_template_vars()
# Returns: {'project_name': 'my-awesome-project', ...}

# Bash projects can provide additional template context
bash_config = ProjectConfig(
    project_name="shell-tools",
    project_type="bash",
    description="Utility scripts",
    author_name="Shell User",
    author_email="shell@example.com",
    github_username="shelluser",
    target_directory=Path("./shell-tools"),
    extra_context={"script_name": "run.sh", "script_description": "Entrypoint script"},
)
```

## Fields

- `project_name`: Display name for the project
- `project_type`: Selected project template type (e.g., `python`, `bash`)
- `description`: Brief project description
- `author_name`, `author_email`: Author metadata
- `github_username`: GitHub username for URLs and metadata
- `target_directory`: Output directory path
- `python_version`: Optional Python version (Python projects)
- `package_name`: Optional Python package/module name
- `entry_point`: Whether to scaffold a CLI entry point (Python projects)
- `create_api`: Whether to include FastAPI scaffolding (Python projects)
- `extra_context`: Additional template variables (e.g., Bash script names)

## Change Log

- **v0.1.0**: Initial implementation with all core project fields
- **v0.2.0**: Added project types, optional Python metadata, and extra context support
