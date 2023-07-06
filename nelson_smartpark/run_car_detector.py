from car_detector import CarDetector
import toml

# Load the config from the TOML file
with open('config.toml', 'r') as f:
    config = toml.load(f)["CarParks"][0]

# Create an instance of CarDetector
car_detector = CarDetector(config)

# Run the car detector
car_detector.run()
