import json
import toml


class Config:
    def __init__(self, filepath, park_index=0):
        """
        Initializes the Config class.

        Args:
            filepath (str): Path to the configuration file (TOML or JSON).
            park_index (int, optional): Index of the parking lot configuration to use. Defaults to 0.
        """
        self.filepath = filepath
        self.park_index = park_index
        self.load_config()

    def load_config(self):
        """
        Loads the configuration from the TOML or JSON file.
        """
        if self.filepath.endswith('.toml'):
            with open(self.filepath, 'r') as f:
                self.config_data = toml.load(f)
        elif self.filepath.endswith('.json'):
            with open(self.filepath, 'r') as f:
                self.config_data = json.load(f)
        else:
            raise ValueError("Unsupported config file format")

    def get(self, key):
        """
        Gets the value of a configuration attribute.

        Args:
            key (str): The attribute name.

        Returns:
            Any: The value of the attribute.
        """
        park_config = self.config_data['CarParks'][self.park_index]
        return park_config.get(key)
