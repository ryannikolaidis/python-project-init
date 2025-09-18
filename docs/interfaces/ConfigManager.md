# ConfigManager

- **Stability:** stable
- **Owner:** @ryannikolaidis
- **Location:** project_init/config.py
- **Summary:** Manages user configuration and defaults from YAML files stored at ~/.project-init/config.yaml.

## Inputs/Outputs

**Inputs:**
- YAML configuration file at ~/.project-init/config.yaml (or custom path)
- Fallback to built-in defaults if config missing

**Outputs:**
- `UserDefaults` object with all configured values
- Created config file via `create_default_config()`

## Examples

```python
from project_init.config import ConfigManager

# Use default config location (~/.project-init/config.yaml)
config_manager = ConfigManager()
defaults = config_manager.get_defaults()

# Use custom config location
config_manager = ConfigManager(Path("/path/to/custom.yaml"))

# Create default config file
config_manager.create_default_config()
```

## Configuration Format

```yaml
defaults:
  author_name: Ryan Nikolaidis
  author_email: ryannikolaidis@gmail.com
  github_username: ryannikolaidis
  python_version: '3.12'
  entry_point_default: false
  project_type: python
  project_directory: /Users/ryannikolaidis/Development/
```

## Change Log

- **v0.1.0**: Initial implementation with user-configurable defaults
- **v0.2.0**: Added project type default handling and moved default path to ~/.project-init/config.yaml
