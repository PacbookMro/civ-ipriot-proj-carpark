import random
import threading
import time
import paho.mqtt.client as mqtt

from config import Config
from windowed_display import WindowedDisplay

class CarParkDisplay:
    fields = ['Available bays', 'Temperature', 'At']

    def __init__(self, config):
        """
        Initializes the CarParkDisplay class.

        Args:
            config (Config): Configuration parameters for the car park display.
        """
        self.config = config
        self.window = WindowedDisplay(self.config.get("name"), CarParkDisplay.fields)
        self.available_bays = self.config.get("total-spaces")
        self.temperature = None    # Initialise temperature
        updater = threading.Thread(target=self.check_updates)
        updater.daemon = True
        updater.start()

        # MQTT client setup
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.connect(self.config.get("broker"), self.config.get("port"))
        self.mqtt_client.subscribe("car_detection")
        self.mqtt_client.loop_start()

        self.window.show()

    def on_connect(self, client, userdata, flags, rc):
        """
            Callback function executed when the MQTT client successfully connects to the broker.

            Args:
                client (mqtt.Client): The MQTT client instance.
                userdata: Custom user data.
                flags: Response flags sent by the broker.
                rc (int): The return code indicating the connection status.
                          0 indicates a successful connection, while other values indicate errors.
        """
        if rc == 0:
            print("Connected to MQTT broker")
        else:
            print(f"Failed to connect, return code: {rc}")

    def on_message(self, client, userdata, message):
        """
        Callback function to handle MQTT message events.

        Updates the available bays count and temperature based on the car detection events received via MQTT.

        Args:
            client (mqtt.Client): The MQTT client instance.
            userdata: Custom user data.
            message (mqtt.MQTTMessage): The received MQTT message.
    """
        payload = message.payload.decode()
        if "_incoming" in payload:
            self.available_bays -= 1
        elif "_outgoing" in payload:
            self.available_bays += 1

        # Extract temperature from payload
        parts = payload.split('_')
        if len(parts) == 3 and parts[2].startswith("Temperature"):
            temperature_part = parts[2].split(":")
            if len(temperature_part) == 2:
                self.temperature = temperature_part[1]

    def check_updates(self):
        """
        Periodically checks for updates and updates the display.

        Retrieves field values (available bays, temperature, and current time) and updates the display
        at random intervals between 1 and 10 seconds.
        """
        while True:
            # Check if temperature is not None before updating field_values
            if self.temperature is not None:
                # Format temperature correctly
                temperature = f'{self.temperature}'

                field_values = {
                    'Available bays': f'{self.available_bays}',
                    'Temperature': temperature,  # Display temperature
                    'At': time.strftime("%H:%M:%S")
                }
                time.sleep(random.randint(1, 10))
                self.window.update(field_values)


if __name__ == '__main__':
    # Create a Config instance from a TOML file
    config = Config('config.toml', park_index=0)

    car_park_display = CarParkDisplay(config)
