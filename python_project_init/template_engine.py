"""Template engine for generating project files.

# @interface TemplateEngine | stability:stable | owner:@ryannikolaidis
# inputs: template directory path, variables dict | outputs: rendered file content
# purpose: Jinja2-based template processing for project generation

# @interface ProjectGenerator | stability:stable | owner:@ryannikolaidis
# inputs: ProjectConfig, template directory | outputs: complete project structure
# purpose: Main project generation orchestrator
"""

import shutil
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, select_autoescape

from .models import ProjectConfig


class TemplateEngine:
    """Engine for processing Jinja2 templates."""

    def __init__(self, template_path: Path) -> None:
        """Initialize template engine.

        Args:
            template_path: Path to the template directory
        """
        self.template_path = template_path
        self.env = Environment(
            loader=FileSystemLoader(str(template_path)),
            autoescape=select_autoescape(["html", "xml"]),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        # Add custom filters
        self.env.filters["snake_case"] = self._snake_case

    def _snake_case(self, text: str) -> str:
        """Convert text to snake_case."""
        import re

        # Replace hyphens and spaces with underscores
        text = re.sub(r"[-\s]+", "_", text)
        # Insert underscores before capital letters
        text = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", text)
        return text.lower()

    def render_template(self, template_file: str, variables: dict[str, Any]) -> str:
        """Render a template file with variables.

        Args:
            template_file: Path to template file relative to template directory
            variables: Template variables

        Returns:
            Rendered content
        """
        template = self.env.get_template(template_file)
        return template.render(**variables)

    def process_filename(self, filename: str, variables: dict[str, Any]) -> str:
        """Process filename template variables.

        Args:
            filename: Filename that may contain template variables
            variables: Template variables

        Returns:
            Processed filename
        """
        # Remove .j2 extension if present
        if filename.endswith(".j2"):
            filename = filename[:-3]

        # Render template variables in filename
        template = self.env.from_string(filename)
        return template.render(**variables)


class ProjectGenerator:
    """Generates project from templates."""

    def __init__(self, template_engine: TemplateEngine) -> None:
        """Initialize project generator.

        Args:
            template_engine: Template engine instance
        """
        self.template_engine = template_engine

    def generate_project(self, config: ProjectConfig) -> None:
        """Generate a new project from templates.

        Args:
            config: Project configuration
        """
        variables = config.to_template_vars()

        # Create target directory
        config.target_directory.mkdir(parents=True, exist_ok=True)

        # Process all template files
        self._process_directory(
            self.template_engine.template_path,
            config.target_directory,
            variables,
        )

    def _process_directory(
        self, source_dir: Path, target_dir: Path, variables: dict[str, Any], relative_path: str = ""
    ) -> None:
        """Recursively process directory templates.

        Args:
            source_dir: Source template directory
            target_dir: Target output directory
            variables: Template variables
            relative_path: Relative path from template root
        """
        for item in source_dir.iterdir():
            if item.name.startswith(".") and item.name not in {
                ".github",
                ".gitignore.j2",
                ".pre-commit-config.yaml.j2",
            }:
                continue

            # Skip Docker files unless creating API project
            if not variables.get("create_api", False) and item.name in {
                "Dockerfile.j2",
                "docker-compose.yml.j2",
            }:
                continue

            item_relative = f"{relative_path}/{item.name}" if relative_path else item.name

            # Process filename
            processed_name = self.template_engine.process_filename(item.name, variables)
            target_path = target_dir / processed_name

            if item.is_dir():
                # Handle special directory names that need processing
                if item.name == "package_template":
                    processed_name = variables["package_name"]
                    target_path = target_dir / processed_name

                # Create directory and process contents
                target_path.mkdir(parents=True, exist_ok=True)
                self._process_directory(item, target_path, variables, item_relative)

            elif item.suffix == ".j2":
                # Process template file
                content = self.template_engine.render_template(item_relative, variables)
                # Ensure content ends with newline
                if content and not content.endswith("\n"):
                    content += "\n"
                target_path.write_text(content, encoding="utf-8")

            else:
                # Copy non-template file as-is
                shutil.copy2(item, target_path)
