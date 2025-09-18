# ProjectGenerator

- **Stability:** stable
- **Owner:** @ryannikolaidis
- **Location:** project_init/template_engine.py
- **Summary:** Main orchestrator for project generation that processes template directories and creates complete project structures.

## Inputs/Outputs

**Inputs:**
- `ProjectConfig` instance with project metadata
- `TemplateEngine` instance for file processing

**Outputs:**
- Complete project directory structure
- All template files rendered and organized
- Package directories with correct naming

## Examples

```python
from pathlib import Path

from project_init.template_engine import TemplateEngine, ProjectGenerator
from project_init.models import ProjectConfig

config = ProjectConfig(
    project_name="my-project",
    project_type="python",
    description="A sample Python project",
    author_name="Jane Doe",
    author_email="jane@example.com",
    github_username="janedoe",
    target_directory=Path("./my-project"),
    python_version="3.12",
    package_name="my_project",
    entry_point=True,
)

engine = TemplateEngine(template_path)
generator = ProjectGenerator(engine)
generator.generate_project(config)
```

## Processing Logic

1. Creates target directory structure
2. Recursively processes template directories
3. Handles special directory names (`package_template` → package name)
4. Renders `.j2` files with variables
5. Copies non-template files as-is
6. Processes filenames with variable substitution

## Change Log

- **v0.1.0**: Initial implementation with recursive directory processing
- **v0.2.0**: Supports multi-template project types (Python, Bash)
