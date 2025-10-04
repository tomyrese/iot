import paho.mqtt.client as mqtt
from time import sleep
from random import randint

CHANNEL_ID = "3099763"
CLIENT_ID = "EC0FOBEWKjU1OQwkHhg1Nx0"
USERNAME = "EC0FOBEWKjU1OQwkHhg1Nx0"
PASSWORD = "yH6AmGkv+BrU7ZltoUCDdY4+"
BROKER = "mqtt3.thingspeak.com"
PORT = 1883

client = mqtt.Client(client_id=CLIENT_ID, callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(USERNAME, PASSWORD)
client.connect(BROKER, PORT, 60)

def thingspeak_mqtt(data):
    topic = f"channels/{CHANNEL_ID}/publish"
    payload = f"field2={data}&status=MQTTPUBLISH"
    client.publish(topic, payload)
    print(data)

while True:
    data_random = randint(0, 50)
    thingspeak_mqtt(data_random)
    sleep(2)
