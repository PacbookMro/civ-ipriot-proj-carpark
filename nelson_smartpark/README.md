# Smart Car Park System

This project implements a smart car park system that tracks the number of available parking bays and displays the status in real-time.
It utilizes MQTT messaging for communication between the car detector and the car park display.

## Prerequisites

Before running the project, make sure you have the following prerequisites installed:

- Python 3.x
- Paho MQTT library (`paho-mqtt`)
- Tkinter library (included with Python)
- Toml library (`toml`)
- Tomli library (`tomli`)
- Mosquitto 

You can install the required libraries by running the following command:

```shell
pip install paho-mqtt toml tomli
```

## Setup

Follow the steps below to set up and run the project:

1. Clone the repository to your local machine.
2. Navigate to the project directory.

### Car Park Display

1. Open the `config.toml` file in the root directory.
2. Configure the car park details by modifying the values under the `[CarParks]` section.
3. Save the `config.toml` file.

### Car Detector

1. Open the `config.toml` file in the root directory.
2. Configure the car park details by modifying the values under the `[CarParks]` section.
3. Save the `config.toml` file.

## Running the Application

To run the application, follow these steps:
1. If not already running as a background service, open up a terminal and run the MQTT broker (e.g., Mosquitto) to enable communication between components.
2. Open a terminal and navigate to the project directory subdirectory nelson_smartpark.
3. Repeat 2. for steps 4 - 7.
4. (Optional) Run the mqtt subscriber to test broker is setup to receive MQTT messages:

   ```shell
   python simple_mqtt_sub.py
   ```
5. (Optional) Run the mqtt publisher to publish a test message:

   ```shell
   python simple_mqtt_pub.py
   ```

6. Run the car park display GUI:

   ```shell
   python run_carpark_display.py
   ```

7. Run the car detector GUI:

   ```shell
   python run_car_detector.py
   ```

8. The car park display GUI should open, showing the available bays, temperature, and timestamp.
9. Press the "Incoming Car" or "Outgoing Car" buttons in the car detector GUI to simulate cars entering or leaving the car park.
10. The car park display will update in real-time based on the car detector's actions.
11. The above steps were all performed in the PyCharm IDE using the venv Python 3.x interpreter and associated packages. Make sure to setup and install any missing packages if attempting to run using alternative methods.

## Running Unit Tests

To run the unit tests for the project, follow these steps:

1. Open a terminal and navigate to the project directory.
2. Run the following command:

   ```shell
   python -m unittest discover -s nelson_smartpark_tests
   ```

3. The unit tests will run and display the results in the terminal.
4. Alternatively, you can run the following:

   ```shell
   python -m nelson_smartpark_tests.test_car_detector
   ```

5. The car detector GUI will pop up for each test.
6. Click the `x` each time to close the window.
7. Any test results will be output to the terminal.