# TemplateEngine

- **Stability:** stable
- **Owner:** @ryannikolaidis
- **Location:** project_init/template_engine.py
- **Summary:** Jinja2-based template processing engine that renders project files with variable substitution and custom filters.

## Inputs/Outputs

**Inputs:**
- Template directory path containing `.j2` files
- Template variables dictionary
- Template file paths for rendering

**Outputs:**
- Rendered file content as strings
- Processed filenames with variable substitution

## Examples

```python
from project_init.template_engine import TemplateEngine

engine = TemplateEngine(Path("./templates"))

# Render a template
content = engine.render_template("README.md.j2", {
    "project_name": "my-project",
    "description": "A cool project"
})

# Process filename with variables
filename = engine.process_filename("{{package_name}}.py.j2", {
    "package_name": "my_project"
})
# Result: "my_project.py"
```

## Custom Filters

- `snake_case`: Converts text to snake_case format

## Change Log

- **v0.1.0**: Initial implementation with Jinja2 integration and snake_case filter
