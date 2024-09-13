import yaml
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)


def load_config():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    return config


_config = load_config()


def get_config():
    return _config
