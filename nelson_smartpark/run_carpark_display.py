import toml
from carpark_display import CarParkDisplay

# Load the config from the toml file
with open('config.toml', 'r') as f:
    config = toml.load(f)["CarParks"][0]

# Create an instance of CarParkDisplay with the config
car_park_display = CarParkDisplay(config)
