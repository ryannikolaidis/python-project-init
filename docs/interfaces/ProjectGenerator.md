# ProjectGenerator

- **Stability:** stable
- **Owner:** @ryannikolaidis
- **Location:** python_project_init/template_engine.py
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
from python_project_init.template_engine import TemplateEngine, ProjectGenerator
from python_project_init.models import ProjectConfig

config = ProjectConfig(
    project_name="my-project",
    package_name="my_project",
    # ... other fields
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