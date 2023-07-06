import unittest
import tomli

from nelson_smartpark.car_detector import CarDetector


class TestCarDetector(unittest.TestCase):
    def test_outgoing_car_does_not_exceed_total_spaces(self):
        config_string = '''
        [[CarParks]]
        name = "raf-park-international"
        total-spaces = 130
        total-cars = 0
        location = "moondalup"
        broker = "localhost"
        port = 1883

          [[CarParks.Sensors]]
          name = "sensor1"
          type = "entry"

          [[CarParks.Sensors]]
          name = "sensor2"
          type = "exit"

          [[CarParks.Displays]]
          name = "display1"
        '''
        config = tomli.loads(config_string)
        car_detector = CarDetector(config["CarParks"][0])

        # Simulate outgoing car multiple times
        for _ in range(10):
            car_detector.outgoing_car()

            # Check if available bays are less than or equal to total spaces
            self.assertLessEqual(car_detector.available_bays, config["CarParks"][0]["total-spaces"])

    def test_incoming_car_does_not_go_negative(self):
        config_string = '''
        [[CarParks]]
        name = "raf-park-international"
        total-spaces = 130
        total-cars = 0
        location = "moondalup"
        broker = "localhost"
        port = 1883

          [[CarParks.Sensors]]
          name = "sensor1"
          type = "entry"

          [[CarParks.Sensors]]
          name = "sensor2"
          type = "exit"

          [[CarParks.Displays]]
          name = "display1"
        '''
        config = tomli.loads(config_string)
        car_detector = CarDetector(config["CarParks"][0])

        # Simulate incoming car multiple times
        for _ in range(10):
            car_detector.incoming_car()

            # Check if available bays are greater than 0
            self.assertGreater(car_detector.available_bays, 0)


if __name__ == '__main__':
    unittest.main()
