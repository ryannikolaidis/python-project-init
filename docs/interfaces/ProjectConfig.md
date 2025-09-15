# ProjectConfig

- **Stability:** stable
- **Owner:** @ryannikolaidis
- **Location:** python_project_init/models.py
- **Summary:** Data structure that holds all project configuration and metadata, with conversion to template variables.

## Inputs/Outputs

**Inputs:**
- Project metadata from user input or programmatic creation

**Outputs:**
- Structured configuration data
- Template variables dictionary via `to_template_vars()`

## Examples

```python
from python_project_init.models import ProjectConfig
from pathlib import Path

config = ProjectConfig(
    project_name="my-awesome-project",
    description="A Python project",
    author_name="John Doe",
    author_email="john@example.com",
    python_version="3.12",
    package_name="my_awesome_project",
    entry_point=True,
    github_username="johndoe",
    target_directory=Path("./my-awesome-project"),
)

# Get template variables
variables = config.to_template_vars()
# Returns: {'project_name': 'my-awesome-project', ...}
```

## Fields

- `project_name`: Display name for the project
- `description`: Brief project description
- `author_name`, `author_email`: Author metadata
- `python_version`: Target Python version
- `package_name`: Python module/package name
- `entry_point`: Boolean for CLI entry point creation
- `github_username`: GitHub username for URLs
- `target_directory`: Output directory path

## Change Log

- **v0.1.0**: Initial implementation with all core project fields