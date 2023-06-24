import json

class ConfigManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = {}
        self.load_config()

    def load_config(self):
        try:
            with open(self.file_path, 'r') as file:
                self.config = json.load(file)
        except OSError as e:
            if e.args[0] == 2:  # errno.ENOENT, file not found
                self.save_config({})  # Write empty values if file doesn't exist

    def save_config(self, config=None):
        if config is None:
            config = self.config

        with open(self.file_path, 'w') as file:
            json.dump(config, file)

    def update_config(self, new_config):
        self.config = new_config
        self.save_config()
        print("Config updated:", self.config)

    def get(self, key):
        return self.config.get(key, "")
