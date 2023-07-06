import tkinter as tk
import paho.mqtt.client as mqtt

class CarDetector:
    def __init__(self, config):
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
        self.mqtt_client.connect(self.config["broker"], self.config["port"])
        self.mqtt_client.loop_start()

        self.root.mainloop()

    def publish_detection(self, car_type):
        payload = f"{self.config['name']}_{car_type}"
        self.mqtt_client.publish("car_detection", payload)

    def incoming_car(self):
        if self.available_bays < self.config["total-spaces"]:
            self.available_bays += 1
            print(f"Available bays: {self.available_bays}")
            self.publish_detection("incoming")
        else:
            print("All bays are occupied")

    def outgoing_car(self):
        if self.available_bays > 0:
            self.available_bays -= 1
            print(f"Available bays: {self.available_bays}")
            self.publish_detection("outgoing")
        else:
            print("No cars to remove")

if __name__ == '__main__':
    import toml

    # Load the config from the TOML file
    with open('config.toml', 'r') as f:
        config = toml.load(f)["CarParks"][0]

    car_detector = CarDetector(config)
