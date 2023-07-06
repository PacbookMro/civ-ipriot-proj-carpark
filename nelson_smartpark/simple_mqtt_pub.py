import paho.mqtt.publish as publish

if __name__ == '__main__':
    # Publish a test message
    publish.single("carpark/test", "Hello from Python", hostname="localhost")

# Comment out the above code uncomment this back in to test if mosquitto broker is working
#
# import paho.mqtt.client as mqtt
#
# BROKER, PORT = "localhost", 1883
#
# def on_connect(client, userdata, flags, rc):
#     """
#     Callback function triggered when the client successfully connects to the MQTT broker.
#
#     Args:
#         client (mqtt.Client): The MQTT client instance.
#         userdata: User-defined data associated with the client.
#         flags: Response flags sent by the broker.
#         rc (int): The connection result code.
#     """
#     if rc == 0:
#         print("Connected to MQTT broker")
#     else:
#         print(f"Failed to connect, return code: {rc}")
#
# def on_publish(client, userdata, mid):
#     """
#     Callback function triggered when a message is successfully published.
#
#     Args:
#         client (mqtt.Client): The MQTT client instance.
#         userdata: User-defined data associated with the client.
#         mid (int): The message ID.
#     """
#     print("Message published successfully")
#     with open("published_message.txt", "w") as f:
#         f.write("Hello from Python")
#
# client = mqtt.Client()
# client.on_connect = on_connect
# client.on_publish = on_publish
#
# client.connect(BROKER, PORT)
# client.loop_start()
#
# client.publish("lot/sensor", "Hello from Python")
#
# client.loop_stop()
# client.disconnect()
#
