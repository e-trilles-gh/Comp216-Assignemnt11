import json
import time
import threading
import paho.mqtt.client as mqtt
from util import create_data

BROKER = "127.0.0.1"
PORT = 1883
TOPIC = "TEMPERATURE"

def publish_loop():
    while True:
        # Create data
        data = create_data()

        # Convert to JSON string
        payload = json.dumps(data)

        # Create client
        client = mqtt.Client(client_id="Publisher")
        client.connect(BROKER, PORT, 60)

        # Publish
        client.publish(TOPIC, payload)
        print(f"Published: {payload}")

        # Disconnect
        client.disconnect()

        # Wait before next send
        time.sleep(3)


if __name__ == "__main__":
    threading.Thread(target=publish_loop).start()