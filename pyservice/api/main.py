from fastapi import FastAPI
from logging import basicConfig, INFO
from pyservice.api.utils.builder import collect_and_include_routers
from pyservice.api.utils.service_bootstrapper import ServiceBootstrapper
from pyservice.api.utils.services import Services


# from pyservice.api.utils.services import bootstrap_database


def bootstrap_application() -> FastAPI:
    basicConfig(level=INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    boot = FastAPI(title="PyService Template", description="This is a internal template for fastapi microservices")

    # TODO: Implements Redis Enable/Disable mechanism and save the set from the builder in it.
    # TODO: Instead of the redi cache firs try to verify the possibility of lazy loading services
    # but write a enable/disable mechanism to enable when and where use the cache or the lazy loading or both.
    collect_and_include_routers(boot)

    return boot

services = Services()
bootstrapper = ServiceBootstrapper(services.services)

bootstrapper.register("postgres", Services.bootstrap_database)
# bootstrapper.register("redis", Services.bootstrap_redis)
# bootstrapper.register("rabbitmq", Services.bootstrap_rabbitmq)

bootstrapper.bootstrap_all()
app = bootstrap_application()
