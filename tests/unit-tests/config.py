from unittest.mock import mock_open, patch
from pyservice.config import load_config


def test_load_config():
    mock_config_data = """
    application:
        key1: value1
        key2: value2
    """
    with patch('builtins.open', mock_open(read_data=mock_config_data)):
        config = load_config()

    assert config == {'application': {'key1': 'value1', 'key2': 'value2'}}
