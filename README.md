# python-project-init

A CLI tool to initialize Python projects from templates with modern tooling and best practices.

## Features

- **Three Project Types**: Library, CLI applications, and FastAPI web applications
- **Interactive CLI** with rich prompts and YAML configuration support
- **Modern Python tooling**: uv, ruff, black, mypy, pytest, pre-commit hooks
- **FastAPI Support**: Production-ready web applications with Docker
- **Hot-reload development**: `make run-dev` for rapid development
- **Complete project structure**: tests, docs, CI/CD, Docker support
- **Template engine** using Jinja2 for flexible customization
- **GitHub workflows** for automated testing and building
- **Docker optimization**: Multi-stage builds with retry logic and security

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
- **Entry point**: Whether to create a CLI command (Typer-based)
- **FastAPI web app**: Whether to create a web application
- **GitHub username**: For repository URLs

### Configuration File

Save defaults in `~/.ppi/config.yaml`:

```yaml
author_name: "Your Name"
author_email: "your.email@example.com"
github_username: "yourusername"
project_directory: "/path/to/your/projects"
python_version: "3.12"
```

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

## Project Types

### 1. Library Projects
- Simple Python libraries with reusable functions
- Clean API design with comprehensive tests
- Import and use in other projects

### 2. CLI Applications
- **Typer-based** command-line interfaces with rich output
- **Multiple commands** with help, configuration, and interactive prompts
- **Global installation** via pipx for system-wide access

### 3. FastAPI Web Applications
- **Production-ready** FastAPI applications with Docker
- **Hot-reload development** with `make run-dev`
- **Complete stack**: PostgreSQL, Redis, pgAdmin via docker-compose
- **Interactive docs**: Swagger UI and ReDoc automatically generated
- **Health checks**, logging, and security best practices

## Templates

Templates use Jinja2 with these variables:

- `{{ project_name }}`: Project name (e.g., "my-project")
- `{{ package_name }}`: Python package name (e.g., "my_project")
- `{{ description }}`: Project description
- `{{ author_name }}`, `{{ author_email }}`: Author information
- `{{ python_version }}`: Target Python version
- `{{ github_username }}`: GitHub username
- `{{ entry_point }}`: Boolean for CLI entry point
- `{{ create_api }}`: Boolean for FastAPI web application
- `{{ current_year }}`: Current year for copyright

## Architecture

- **CLI**: Built with Typer and Rich for excellent UX
- **Templates**: Jinja2 engine with variable substitution
- **Models**: Type-safe configuration with dataclasses
- **Generator**: Orchestrates template processing and file creation

See [docs/interfaces/](docs/interfaces/) for detailed interface documentation.

## Recent Improvements

### Docker & FastAPI Enhancements
- **Robust Docker builds** with retry logic for package repository issues
- **Security hardened** containers with non-root users and proper permissions
- **Multi-stage optimization** with dependency caching
- **Health checks** for production readiness

### Development Experience
- **`make run-dev`** target for instant FastAPI development servers
- **Hot-reload** automatically restarts on code changes
- **Fixed Makefile generation** with proper Jinja2 template handling
- **Comprehensive testing** for all project types (library, CLI, API)

### Template System
- **Conditional Docker files** (only generated for API projects)
- **Project-specific dependencies** based on selected features
- **Proper CLI command naming** (preserves original project names)
- **Enhanced README generation** with project-specific documentation

## License

MIT License - see [LICENSE](LICENSE) file for details.