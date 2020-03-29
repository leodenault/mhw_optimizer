import json

from config.config import Config
from config.config import DecorationConfig
from config.config import SkillConfig
from config.config import SkillData


class ConfigImporter:
    def __init__(self, file_location):
        self.file_location = file_location

    def load(self):
        with open(self.file_location) as config_file:
            raw_config = json.load(config_file)

            raw_decoration_config = raw_config["decorations"]
            decoration_config = DecorationConfig(
                _validate_and_return_value(raw_decoration_config, "deco_1"),
                _validate_and_return_value(raw_decoration_config, "deco_2"),
                _validate_and_return_value(raw_decoration_config, "deco_3"),
                _validate_and_return_value(raw_decoration_config, "deco_4"),
                _validate_and_return_value(raw_decoration_config, "num_decos")
            )

            skill_config = SkillConfig(
                _generate_skill_data(raw_config["skills"])
            )

            return Config(
                decoration_config,
                skill_config,
                _validate_and_return_value(raw_config, "defence"),
                int(_validate_and_return_value(raw_config, "limit")),
            )


def _validate_and_return_value(config, parameter_name):
    if parameter_name in config:
        return config[parameter_name]
    else:
        print(
            "Missing parameter '{0}' in config. Assuming a value of 1.0.".format(
                parameter_name
            )
        )
        return 1.0


def _generate_skill_data(config):
    return {
        skill: SkillData(
            _validate_and_return_value(raw_data, "max"),
            _validate_and_return_value(raw_data, "weight"),
            _validate_and_return_value(raw_data, "penalty")
        ) for skill, raw_data in config.items()
    }
