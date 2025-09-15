# python-project-init

A CLI tool to initialize Python projects from templates with modern tooling and best practices.

## Features

- **Interactive CLI** with rich prompts for project configuration
- **Modern Python tooling**: uv, ruff, pytest, pre-commit hooks
- **Complete project structure**: tests, docs, CI/CD, Docker support
- **Template engine** using Jinja2 for flexible customization
- **GitHub workflows** for automated testing and building
- **Sphinx documentation** setup ready to go

## Quick Start

```bash
# Install the tool
git clone https://github.com/ryannikolaidis/python-project-init.git
cd python-project-init
make install-dev

# Initialize a new project
ppi init my-awesome-project

# Or run interactively
ppi init
```

## Generated Project Structure

```
my-awesome-project/
├── my_awesome_project/          # Main package
│   ├── __init__.py
│   └── main.py                  # Entry point (optional)
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── docs/                        # Sphinx documentation
├── .github/workflows/ci.yml     # GitHub Actions CI
├── pyproject.toml               # Modern Python packaging
├── Makefile                     # Development commands
├── Dockerfile                   # Container support
├── docker-compose.yml
├── .pre-commit-config.yaml      # Code quality hooks
├── .gitignore
├── LICENSE                      # MIT License
└── README.md
```

## CLI Usage

```bash
# Basic usage
ppi init [PROJECT_NAME]

# With custom template
ppi init --template-path ./my-templates/

# Preview without creating files
ppi init --dry-run

# Force overwrite existing directory
ppi init --force

# Show help
ppi --help
```

## Configuration Options

The CLI prompts for:

- **Project name**: Used for directories and repository
- **Description**: Brief project description
- **Author details**: Name and email for metadata
- **Python version**: 3.10, 3.11, or 3.12
- **Package name**: Python module name (auto-generated)
- **Entry point**: Whether to create a CLI command
- **GitHub username**: For repository URLs

## Development

### Setup

```bash
make install-dev          # Install with dev dependencies
uv run pre-commit install # Install pre-commit hooks
```

### Commands

```bash
make test                 # Run tests
make test-cov            # Run tests with coverage
make lint                # Run linting
make tidy                # Fix formatting
make check               # Run all checks
```

## Templates

Templates use Jinja2 with these variables:

- `{{ project_name }}`: Project name (e.g., "my-project")
- `{{ package_name }}`: Python package name (e.g., "my_project")
- `{{ description }}`: Project description
- `{{ author_name }}`, `{{ author_email }}`: Author information
- `{{ python_version }}`: Target Python version
- `{{ github_username }}`: GitHub username
- `{{ entry_point }}`: Boolean for CLI entry point

## Architecture

- **CLI**: Built with Typer and Rich for excellent UX
- **Templates**: Jinja2 engine with variable substitution
- **Models**: Type-safe configuration with dataclasses
- **Generator**: Orchestrates template processing and file creation

See [docs/interfaces/](docs/interfaces/) for detailed interface documentation.

## License

MIT License - see [LICENSE](LICENSE) file for details.