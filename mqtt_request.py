import paho.mqtt.client as mqtt
from time import sleep
from random import randint

CHANNEL_ID = "3092683"
CLIENT_ID = "CCccGScYFicOPC0lLRoVOgc"
USERNAME = "CCccGScYFicOPC0lLRoVOgc"
PASSWORD = "kOywyGwAJ7Usz5m7kQZjoVGD"
BROKER = "mqtt3.thingspeak.com"
PORT = 1883

client = mqtt.Client(client_id=CLIENT_ID, callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(USERNAME, PASSWORD)
client.connect(BROKER, PORT, 60)

def thingspeak_mqtt(data):
    topic = f"channels/{CHANNEL_ID}/publish"
    payload = f"field3={data}&status=MQTTPUBLISH"
    client.publish(topic, payload)
    print(f"[PUB] {topic}: {payload}")

while True:
    data_random = randint(0, 50)
    thingspeak_mqtt(data_random)
    sleep(20)
