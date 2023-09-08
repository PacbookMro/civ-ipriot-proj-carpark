from carpark_display import CarParkDisplay
from config import Config

# Create a Config instance from a TOML file
config = Config('config.toml', park_index=0)

# Create an instance of CarParkDisplay with the config
car_park_display = CarParkDisplay(config)
