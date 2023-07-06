import paho.mqtt.subscribe as subscribe

if __name__ == '__main__':
    # Subscribe to the test topic and print received messages
    msg = subscribe.simple("carpark/test", hostname="localhost")
    print(msg.payload.decode())
