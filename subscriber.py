import json
import paho.mqtt.client as mqtt
from util import print_data

BROKER = "127.0.0.1"
PORT = 1883
TOPIC = "TEMPERATURE"


def handle_message(client, userdata, message):
    try:
        # Decode message
        decoded = message.payload.decode("utf-8")

        # Convert to dict
        data = json.loads(decoded)

        print_data(data)

    except Exception as e:
        print("Error processing message:", e)


client = mqtt.Client(client_id="Subscriber")

# Assign callback
client.on_message = handle_message

# Connect
client.connect(BROKER, PORT, 60)

# Subscribe
client.subscribe(TOPIC)

print("Subscribed and waiting for messages.")

# Listen forever
client.loop_forever()