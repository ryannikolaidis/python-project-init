"""Data models for project initialization.

# @interface ProjectConfig | stability:stable | owner:@ryannikolaidis
# inputs: user-provided project metadata | outputs: template variables dict
# purpose: Configuration data structure for project generation
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class ProjectConfig:
    """Configuration for a new project."""

    project_name: str
    description: str
    author_name: str
    author_email: str
    python_version: str
    package_name: str
    entry_point: bool
    create_api: bool
    github_username: str
    target_directory: Path

    def to_template_vars(self) -> dict[str, Any]:
        """Convert to template variables dictionary."""
        from datetime import datetime

        return {
            "project_name": self.project_name,
            "description": self.description,
            "author_name": self.author_name,
            "author_email": self.author_email,
            "python_version": self.python_version,
            "package_name": self.package_name,
            "entry_point": self.entry_point,
            "create_api": self.create_api,
            "github_username": self.github_username,
            "current_year": datetime.now().year,
        }
