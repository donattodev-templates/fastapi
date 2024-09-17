
import pytest
from fastapi import FastAPI


@pytest.fixture
def mock_fastapi_app():
    return FastAPI()


@pytest.fixture
def mock_config():
    return {
        'application': {
            'api': {
                'routers_path': '/mock/path/to/routers'
            }
        }
    }
