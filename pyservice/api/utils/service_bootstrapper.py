from typing import Callable, Dict


class ServiceBootstrapper:
    def __init__(self, services: Dict[str, bool]):
        self.services = services
        self.bootstrap_functions: Dict[str, Callable] = {}

    def register(self, service_name: str, bootstrap_function: Callable):
            self.bootstrap_functions[service_name] = bootstrap_function

    def bootstrap_all(self):
        for service, enabled in self.services.items():
            if enabled and service in self.bootstrap_functions:
                self.bootstrap_functions[service]()
