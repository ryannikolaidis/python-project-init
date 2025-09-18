"""Data models for project initialization.

# @interface ProjectConfig | stability:stable | owner:@ryannikolaidis
# inputs: user-provided project metadata | outputs: template variables dict
# purpose: Configuration data structure for project generation
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class ProjectConfig:
    """Configuration for a new project."""

    project_name: str
    project_type: str
    description: str
    author_name: str
    author_email: str
    github_username: str
    target_directory: Path
    python_version: str | None = None
    package_name: str | None = None
    entry_point: bool = False
    create_api: bool = False
    extra_context: dict[str, Any] = field(default_factory=dict)

    def to_template_vars(self) -> dict[str, Any]:
        """Convert to template variables dictionary."""
        from datetime import datetime

        variables: dict[str, Any] = {
            "project_name": self.project_name,
            "project_type": self.project_type,
            "description": self.description,
            "author_name": self.author_name,
            "author_email": self.author_email,
            "entry_point": self.entry_point,
            "create_api": self.create_api,
            "github_username": self.github_username,
            "current_year": datetime.now().year,
        }

        if self.python_version is not None:
            variables["python_version"] = self.python_version

        if self.package_name is not None:
            variables["package_name"] = self.package_name

        variables.update(self.extra_context)

        return variables
