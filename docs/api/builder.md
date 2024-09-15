# collect_and_include_routers Function Documentation

## Overview

The `collect_and_include_routers` function is responsible for dynamically collecting and including routers in a FastAPI application.

## Function Signature

```python
def collect_and_include_routers(boot: FastAPI) -> set:
```

## Parameters

* `boot` (FastAPI): The FastAPI application instance to which routers will be added.

## Return Value

* `set`: A set of router names (without the '.py' extension) that were successfully processed.

## Functionality

The function performs the following operations:

1. Changes the current working directory to the directory of the script.
2. Retrieves the router path from the application configuration.
3. Scans the router directory for Python files (excluding `__init__.py`).
4. For each valid router file:
    * Adds the router name (without .py extension) to a set.
    * Attempts to import the router module.
    * If successful, includes the router in the FastAPI application.

## Side Effects

* Changes the current working directory.
* Modifies the provided FastAPI instance by including routers.
* Logs warnings and errors.

## Error Handling

* Exceptions raised during directory scanning or module importing are caught and logged.
* The function continues processing other routers even if an error occurs with one.

## Dependencies

* `FastAPI` from `fastapi`
* `import_module` from `importlib`
* `scandir`, `path`, `chdir` from `os`
* `error`, `warning` from `logging`
* `get_config` from `pyservice.config`

## Usage Example

```python
from fastapi import FastAPI
from pyservice.api.routes import collect_and_include_routers

app = FastAPI()
processed_routers = collect_and_include_routers(app)
print(f"Processed routers: {processed_routers}")
```

## Notes

* This function assumes a specific project structure where router modules are located in `pyservice.api.routes`.
* Router modules should follow a naming convention where the module name matches the file name.
* The function uses the application configuration to determine the router path.

## Potential Improvements

* Add error handling for cases where the router path doesn't exist.
* Implement a more robust method for identifying valid router modules.
* Consider adding options for custom router path or naming conventions.