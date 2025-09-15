"""CLI interface for python-project-init.

# @interface ProjectInitCLI | stability:experimental | owner:@ryannikolaidis
# inputs: project_name, template_path, flags | outputs: generated project files
# purpose: Interactive CLI for initializing Python projects from templates
"""

import re
from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, Prompt
from rich.text import Text

from .config import ConfigManager
from .models import ProjectConfig
from .template_engine import ProjectGenerator, TemplateEngine

app = typer.Typer(
    name="python-project-init",
    help="Initialize Python projects from templates",
    add_completion=False,
)
console = Console()


def validate_project_name(name: str) -> bool:
    """Validate project name format."""
    # Allow letters, numbers, hyphens, and underscores
    pattern = r"^[a-zA-Z][a-zA-Z0-9_-]*$"
    return bool(re.match(pattern, name))


def validate_email(email: str) -> bool:
    """Basic email validation."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def snake_case(text: str) -> str:
    """Convert text to snake_case."""
    # Replace hyphens and spaces with underscores
    text = re.sub(r"[-\s]+", "_", text)
    # Insert underscores before capital letters
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", text)
    return text.lower()


@app.command()
def init(
    project_name: str | None = typer.Argument(None, help="Name of the project to create"),
    template_path: Path | None = typer.Option(
        None, "--template-path", "-t", help="Path to custom template directory"
    ),
    config_path: Path | None = typer.Option(
        None, "--config", "-c", help="Path to configuration file"
    ),
    dry_run: bool = typer.Option(
        False, "--dry-run", help="Show what would be created without actually creating files"
    ),
    force: bool = typer.Option(
        False, "--force", "-f", help="Overwrite existing directory if it exists"
    ),
) -> None:
    """Initialize a new Python project from a template."""

    # Display welcome message
    console.print()
    console.print(
        Panel.fit(
            Text("🐍 Python Project Initializer", style="bold blue"),
            style="blue",
        )
    )
    console.print()

    # Get template path
    if template_path is None:
        # Use built-in generic template
        template_path = Path(__file__).parent / "templates" / "generic"

    if not template_path.exists():
        console.print(f"[red]Error: Template path does not exist: {template_path}[/red]")
        raise typer.Exit(1)

    # Initialize configuration manager
    config_manager = ConfigManager(config_path)

    # Collect project information interactively
    config = collect_project_info(project_name, force, config_manager)

    if dry_run:
        console.print(
            f"\n[yellow]Dry run mode - would create project at: {config.target_directory}[/yellow]"
        )
        console.print("Template variables:")
        for key, value in config.to_template_vars().items():
            console.print(f"  {key}: {value}")
        return

    # Generate project
    try:
        template_engine = TemplateEngine(template_path)
        generator = ProjectGenerator(template_engine)
        generator.generate_project(config)

        console.print(f"\n✅ [green]Project '{config.project_name}' created successfully![/green]")
        console.print(f"📁 Location: {config.target_directory}")
        console.print("\n🚀 Next steps:")
        console.print(f"   cd {config.project_name}")
        console.print("   make install-dev")
        console.print("   uv run pre-commit install")

    except Exception as e:
        console.print(f"\n[red]Error creating project: {e}[/red]")
        raise typer.Exit(1)


def collect_project_info(project_name: str | None, force: bool, config_manager: ConfigManager) -> ProjectConfig:
    """Collect project information interactively."""

    # Get user defaults from config
    defaults = config_manager.get_defaults()

    # Project name
    while not project_name or (project_name and not validate_project_name(project_name)):
        project_name = Prompt.ask(
            "Project name", default="my-awesome-project" if not project_name else None
        )
        if project_name and not validate_project_name(project_name):
            console.print(
                "[red]Invalid project name. Use letters, numbers, hyphens, and underscores only.[/red]"
            )
            project_name = None

    # Check if directory exists
    assert project_name is not None  # mypy: project_name is guaranteed to be str here

    # Use configured project directory or current working directory
    if defaults.project_directory:
        base_directory = Path(defaults.project_directory).expanduser()
    else:
        base_directory = Path.cwd()

    target_directory = base_directory / project_name

    # Show user where project will be created
    if defaults.project_directory:
        console.print(f"📁 Project will be created in: {target_directory}")

    if target_directory.exists() and not force:
        if not Confirm.ask(f"Directory '{project_name}' already exists. Continue anyway?"):
            console.print("[yellow]Cancelled.[/yellow]")
            raise typer.Exit(0)

    # Description
    description = Prompt.ask(
        "Project description", default=f"A Python project called {project_name}"
    )

    # Author information
    author_name = Prompt.ask("Author name", default=defaults.author_name)

    author_email = None
    while not author_email or not validate_email(author_email):
        author_email = Prompt.ask("Author email", default=defaults.author_email)
        if not validate_email(author_email):
            console.print("[red]Invalid email format.[/red]")
            author_email = None

    # Python version
    python_version = Prompt.ask("Python version", choices=["3.12", "3.11", "3.10"], default=defaults.python_version)

    # Package name (auto-generate from project name)
    suggested_package_name = snake_case(project_name)
    package_name = Prompt.ask("Package name (Python module name)", default=suggested_package_name)

    # Entry point
    entry_point = Confirm.ask("Create CLI entry point?", default=defaults.entry_point_default)

    # API option
    create_api = Confirm.ask("Create FastAPI web application?", default=False)

    # GitHub username
    github_username = Prompt.ask("GitHub username/organization", default=defaults.github_username)

    return ProjectConfig(
        project_name=project_name,
        description=description,
        author_name=author_name,
        author_email=author_email,
        python_version=python_version,
        package_name=package_name,
        entry_point=entry_point,
        create_api=create_api,
        github_username=github_username,
        target_directory=target_directory,
    )


@app.command()
def config() -> None:
    """Create default configuration file."""
    config_manager = ConfigManager()
    config_manager.create_default_config()


@app.command()
def version() -> None:
    """Show version information."""
    from . import __version__

    console.print(f"python-project-init {__version__}")


if __name__ == "__main__":
    app()
