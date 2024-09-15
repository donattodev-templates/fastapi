from fastapi import FastAPI
from logging import basicConfig, INFO
from pyservice.api.builder import collect_and_include_routers
from pyservice.infrastructure.mapping.score_table import create_score_table


def bootstrap_database() -> None:
    """Creates database tables schematics if they don't exist at application startup."""
    create_score_table()


def bootstrap_application() -> FastAPI:
    basicConfig(level=INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    boot = FastAPI(title="PyService Template", description="This is a internal template for fastapi microservices")
    # TODO: Implements Redis Enable/Disable mechanism and save the set from the builder in it.
    collect_and_include_routers(boot)

    return boot


app = bootstrap_application()
bootstrap_database()
