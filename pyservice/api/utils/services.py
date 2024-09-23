import logging

from pyservice.infrastructure.mapping.score_table import create_score_table
from pyservice.config import get_config


class Services:
    def __init__(self):
        self.config = get_config()
        self.services = self._get_services()
        logging.info(f"Initialized services: {self.services}")

    @staticmethod
    def _get_services():
        # redis: bool = get_config()['application']['api']['service_switcher']['redis']
        postgres: bool = get_config()['application']['api']['service_switcher']['postgres'].get('postgres', False)

        services = {
            # "redis": redis,
            "postgres": postgres
        }

        return services

    @staticmethod
    def bootstrap_database() -> None:
        """Creates database tables schematics if they don't exist at application startup."""
        logging.info("Bootstrapping database...")
        create_score_table()
