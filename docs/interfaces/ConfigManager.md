# ConfigManager

- **Stability:** stable
- **Owner:** @ryannikolaidis
- **Location:** python_project_init/config.py
- **Summary:** Manages user configuration and defaults from YAML files stored at ~/.ppi/config.yaml.

## Inputs/Outputs

**Inputs:**
- YAML configuration file at ~/.ppi/config.yaml (or custom path)
- Fallback to built-in defaults if config missing

**Outputs:**
- `UserDefaults` object with all configured values
- Created config file via `create_default_config()`

## Examples

```python
from python_project_init.config import ConfigManager

# Use default config location (~/.ppi/config.yaml)
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
  project_directory: /Users/ryannikolaidis/Development/
```

## Change Log

- **v0.1.0**: Initial implementation with ~/.ppi/config.yaml location