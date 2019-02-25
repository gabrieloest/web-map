import yaml

CONFIG_PATH = "./config/config.yml"

class ConfigResolver:

    def __init__(self, logger):
        self.log = logger

    def log_configurations(self, configurations):
        for key, value in configurations.items():
            self.log.info('{}: {}'.format(key, value))

    def load_config(self):
        self.log.info('Loading configurations....')
        with open(CONFIG_PATH, 'r') as ymlfile:
            config = yaml.load(ymlfile)

        config = config['google-api']
        self.log_configurations(config)

        return config
