import os
from magical_chords.configs import docker_config, local_config


def configure_app(app):
    env = os.environ.get("CHORDS_ENV", "local")

    print(f"Using environment = {env}")

    current_configs = {
        "docker": docker_config,
        "local": local_config
    }[env].config_dict

    for key, value in current_configs.items():
        app.config[key] = value
