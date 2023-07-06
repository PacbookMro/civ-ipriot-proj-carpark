from car_detector import CarDetector
import toml

with open('config.toml', 'r') as f:
    config = toml.load(f)["CarParks"][0]

car_detector = CarDetector(config)
car_detector.run()
