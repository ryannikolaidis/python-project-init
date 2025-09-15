# ProjectInitCLI

- **Stability:** experimental
- **Owner:** @ryannikolaidis
- **Location:** python_project_init/cli.py
- **Summary:** Interactive command-line interface for initializing Python projects from templates with rich prompts and validation.

## Inputs/Outputs

**Inputs:**
- `project_name` (optional): Name of the project to create
- `--template-path`: Custom template directory path
- `--dry-run`: Preview mode without file creation
- `--force`: Overwrite existing directories

**Outputs:**
- Complete project directory structure
- Rich console feedback during generation
- Error messages for validation failures

## Examples

```bash
# Interactive mode
ppi init

# Direct project creation
ppi init my-awesome-project

# Custom template
ppi init --template-path ./custom-templates/

# Preview mode
ppi init --dry-run my-project
```

## Interactive Prompts

1. Project name validation (letters, numbers, hyphens, underscores)
2. Project description
3. Author name and email (with validation)
4. Python version selection (3.10, 3.11, 3.12)
5. Package name (auto-generated, editable)
6. CLI entry point option
7. GitHub username for URLs

## Change Log

- **v0.1.0**: Initial implementation with basic project generation