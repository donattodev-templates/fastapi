# Configuration Loading Module Documentation

## Overview

This module provides functionality to load configuration from a YAML file and make it accessible throughout the application.

## Functions

### load_config Function

#### Function Signature

```python
def load_config() -> dict:
```

#### Functionality

The `load_config` function performs the following operations:

1. Opens the "config.yaml" file in read mode.
2. Loads the YAML content into a Python dictionary.
3. Returns the loaded configuration.

#### Return Value

* `dict`: A dictionary containing the configuration loaded from the YAML file.

### get_config Function

#### Function Signature

```python
def get_config() -> dict:
```

#### Functionality

The `get_config` function returns the previously loaded configuration.

#### Return Value

* `dict`: A dictionary containing the loaded configuration.

## Global Variables

* `script_dir` (str): The absolute path to the directory containing the script.
* `_config` (dict): The loaded configuration, initialized by calling `load_config()`.

## Side Effects

* Changes the current working directory to the script's directory.
* Reads from the filesystem to load the configuration file.

## Dependencies

* `yaml`: For parsing YAML files.
* `os`: For file and directory operations.

## Usage Example

```python
from config_module import get_config

config = get_config()
database_url = config['database']['url']
print(f"Database URL: {database_url}")
```

## Notes

* The configuration is loaded only once when the module is imported.
* The `config.yaml` file is expected to be in the same directory as the script.

## Potential Improvements

* Add error handling for cases where the config file doesn't exist or is invalid.
* Implement environment-specific configuration loading.
* Add a mechanism to reload the configuration without restarting the application.
* Consider using environment variables for sensitive information instead of storing in the YAML file.