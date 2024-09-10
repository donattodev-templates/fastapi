from fastapi import FastAPI
from pyservice.api.routes.score_router import router
from pyservice.infrastructure.mapping.score_table import create_score_table

# TODO: Create a loop and cache for both bootstrap classes and routers

def bootstrap_database():
    """Creates database tables schematics if they don't exist at application startup."""
    create_score_table()

def bootstrap_application() -> FastAPI:
    boot = FastAPI(title="PyService Template", description="This is a internal template for fastapi microservices")
    boot.include_router(router)
    return boot

app = bootstrap_application()
bootstrap_database()
