"""Configuration management for python-project-init.

# @interface ConfigManager | stability:stable | owner:@ryannikolaidis
# inputs: YAML config files | outputs: default values for CLI prompts
# purpose: Manage user configuration and defaults from YAML files
"""

from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass
class UserDefaults:
    """User default values for project initialization."""

    author_name: str = "Your Name"
    author_email: str = "your.email@example.com"
    github_username: str = "yourusername"
    python_version: str = "3.12"
    entry_point_default: bool = False
    project_directory: str | None = None


class ConfigManager:
    """Manages configuration from YAML files."""

    def __init__(self, config_path: Path | None = None) -> None:
        """Initialize config manager.

        Args:
            config_path: Path to config file, defaults to ~/.ppi/config.yaml
        """
        if config_path is None:
            config_path = Path.home() / ".ppi" / "config.yaml"

        self.config_path = config_path
        self._defaults = None

    def get_defaults(self) -> UserDefaults:
        """Get user defaults, loading from config file if available."""
        if self._defaults is None:
            self._defaults = self._load_defaults()
        return self._defaults

    def _load_defaults(self) -> UserDefaults:
        """Load defaults from config file or return system defaults."""
        if not self.config_path.exists():
            return UserDefaults()

        try:
            with open(self.config_path, encoding="utf-8") as f:
                config_data = yaml.safe_load(f)

            if not config_data:
                return UserDefaults()

            # Extract defaults section
            defaults_data = config_data.get("defaults", {})

            return UserDefaults(
                author_name=defaults_data.get("author_name", "Your Name"),
                author_email=defaults_data.get("author_email", "your.email@example.com"),
                github_username=defaults_data.get("github_username", "yourusername"),
                python_version=defaults_data.get("python_version", "3.12"),
                entry_point_default=defaults_data.get("entry_point_default", False),
                project_directory=defaults_data.get("project_directory"),
            )

        except (yaml.YAMLError, OSError, KeyError) as e:
            # If config is invalid, fall back to system defaults
            print(f"Warning: Could not load config from {self.config_path}: {e}")
            return UserDefaults()

    def create_default_config(self) -> None:
        """Create a default configuration file."""
        self.config_path.parent.mkdir(parents=True, exist_ok=True)

        default_config = {
            "defaults": {
                "author_name": "Ryan Nikolaidis",
                "author_email": "ryannikolaidis@gmail.com",
                "github_username": "ryannikolaidis",
                "python_version": "3.12",
                "entry_point_default": False,
                "project_directory": "/Users/ryannikolaidis/Development/",
            }
        }

        with open(self.config_path, "w", encoding="utf-8") as f:
            yaml.safe_dump(default_config, f, default_flow_style=False, sort_keys=False)

        print(f"Created default config at {self.config_path}")
