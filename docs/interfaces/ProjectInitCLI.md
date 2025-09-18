# ProjectInitCLI

- **Stability:** experimental
- **Owner:** @ryannikolaidis
- **Location:** project_init/cli.py
- **Summary:** Interactive command-line interface for initializing projects (Python/Bash) from curated templates with rich prompts and validation.

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
project-init init

# Direct project creation
project-init init my-awesome-project

# Custom template
project-init init --template-path ./custom-templates/

# Preview mode
project-init init --dry-run my-project
pji init my-project
```

## Interactive Prompts

1. Project name validation (letters, numbers, hyphens, underscores)
2. Project type selection (Python default, Bash optional)
3. Project description auto-personalized by type
4. Author name and email (with validation)
5. Python-specific settings (version, package, CLI/API toggles)
6. Bash-specific settings (script filename and description)
7. GitHub username for README/metadata

## Change Log

- **v0.1.0**: Initial implementation with basic project generation
- **v0.2.0**: Added multi-project support (Python/Bash) and customizable templates
