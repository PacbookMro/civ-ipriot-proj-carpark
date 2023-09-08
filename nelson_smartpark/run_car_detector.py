from car_detector import CarDetector
from config import Config

# Create a Config instance from a TOML file
config = Config('config.toml', park_index=0)

car_detector = CarDetector(config)

# Run the car detector
car_detector.run()
