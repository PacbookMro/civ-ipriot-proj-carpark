import random
import tkinter as tk
import paho.mqtt.client as mqtt

from config import Config


class CarDetector:
    def __init__(self, config):
        """
        Initializes the CarDetector class.

        Args:
            config (Config): Configuration parameters for the car detector.
        """
        self.config = config
        self.available_bays = 0

        self.root = tk.Tk()
        self.root.title("Car Detector ULTRA")

        self.btn_incoming_car = tk.Button(
            self.root, text='🚘 Incoming Car', font=('Arial', 50), cursor='right_side', command=self.incoming_car)
        self.btn_incoming_car.pack(padx=10, pady=5)
        self.btn_outgoing_car = tk.Button(
            self.root, text='Outgoing Car 🚘', font=('Arial', 50), cursor='bottom_left_corner', command=self.outgoing_car)
        self.btn_outgoing_car.pack(padx=10, pady=5)

        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.connect(self.config.get("broker"), self.config.get("port"))
        self.mqtt_client.loop_start()

        self.root.mainloop()

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

    def publish_detection(self, car_type):
        """
        Publishes the car detection event and random temperature to the MQTT broker.

        Args:
            car_type (str): Type of car event (incoming or outgoing).
        """
        temperature = random.randint(0, 45)
        payload = f"{self.config.get('name')}_{car_type}_Temperature:{temperature}℃"
        self.mqtt_client.publish("car_detection", payload)

    def incoming_car(self):
        """
        Handles the incoming car event.

        Increments the available bays if there are vacant spots and publishes the detection event.
        Prints the current available bays count.
        """
        if self.available_bays < self.config.get("total-spaces"):
            self.available_bays += 1
            parking_bays_available = self.config.get("total-spaces") - self.available_bays
            print(f"Parking bays remaining: {parking_bays_available}")
            self.publish_detection("incoming")
        else:
            print("Parking lot has all bays occupied.")

    def outgoing_car(self):
        """
        Handles the outgoing car event.

        Decrements the available bays if there are cars to remove and publishes the detection event.
        Prints the current available bays count.
        """
        if self.available_bays > 0:
            self.available_bays -= 1
            parking_bays_available = self.config.get("total-spaces") - self.available_bays
            print(f"Parking bays remaining: {parking_bays_available}")
            self.publish_detection("outgoing")
        else:
            print("Parking lot has no cars to remove.")

if __name__ == '__main__':
    # Create a Config instance from a TOML file
    config = Config('config.toml', park_index=0)

    car_detector = CarDetector(config)
