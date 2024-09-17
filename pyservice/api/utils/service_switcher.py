from pyservice.config import get_config


class ServiceSwitcher:
    def __init__(self):
        self.config = get_config()

    @staticmethod
    def get_services():
        redis: bool = get_config()['application']['api']['service_switcher']['redis']
        postgres: bool = get_config()['application']['api']['service_switcher']['postgres']

        services = {
            "redis": redis,
            "postgres": postgres
        }

        return services
