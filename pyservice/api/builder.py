from fastapi import FastAPI
from logging import error, warning
from os import scandir, path, chdir
from importlib import import_module
from pyservice.config import get_config


def collect_and_include_routers(boot: FastAPI) -> set:
    """

    Collect router names, format them, and dynamically include routers in the FastAPI application.

    This function performs the following operations:
    1. Changes the current working directory to the directory of this script.
    2. Retrieves the router path from the application configuration.
    3. Scans the router directory for Python files (excluding __init__.py).
    4. For each valid router file:
       a. Adds the router name (without .py extension) to a set.
       b. Attempts to import the router module.
       c. If successful, includes the router in the FastAPI application.

    Args:
    boot (FastAPI): The FastAPI application instance to which routers will be added.

    Returns:
    set: A set of router names (without the '.py' extension) that were successfully
         processed. Note that this includes routers that were found but may not have
         been successfully imported or included.

    Raises:
    Any exceptions raised during directory scanning or module importing are caught
    and logged, allowing the function to continue processing other routers.

    Side Effects:
    - Changes the current working directory.
    - Modifies the provided FastAPI instance by including routers.
    - Logs warnings and errors.

    Note:
    This function assumes a specific project structure where router modules are
    located in 'pyservice.api.routes' and follow a naming convention where the
    module name matches the file name.
    """

    chdir(path.dirname(path.abspath(__file__)))
    routers_path = get_config()['application']['api']['routers_path']
    routers = set()

    with scandir(routers_path) as entries:
        for entry in entries:
            if entry.is_file() and entry.name.endswith('.py') and entry.name != '__init__.py':
                router_name = entry.name[:-3]
                routers.add(router_name)

                try:
                    module = import_module(f"pyservice.api.routes.{router_name}")
                    router = getattr(module, 'router', None)
                    if router:
                        boot.include_router(router)
                    else:
                        warning(f"Warning: No router found in {router_name}")
                except ImportError as e:
                    error(f"Error importing {router_name}: {e}")

    return routers
