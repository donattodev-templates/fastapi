from fastapi import FastAPI
from pyservice.api.routes.submit_scores import router

def bootstrap() -> FastAPI:
    boot = FastAPI(title="PyService Template", description="This is a internal template for fastapi microservices")
    boot.include_router(router)
    return boot

app = bootstrap()
