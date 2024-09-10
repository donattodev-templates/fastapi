from fastapi import FastAPI
from pyservice.api.routes.submit_scores import router
from pyservice.infrastructure.adapters.postgres_adapter import engine, Base

def bootstrap_database():
    """Creates database tables schematics if they don't exist at application startup."""
    Base.metadata.create_all(bind=engine)

def bootstrap_application() -> FastAPI:
    boot = FastAPI(title="PyService Template", description="This is a internal template for fastapi microservices")
    boot.include_router(router)
    return boot

app = bootstrap_application()
bootstrap_database()
