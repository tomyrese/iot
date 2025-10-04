# Channel ID: 794872
# Author: iotlabivuh
# username = JiQ0BAc1DSU5EzgtJishCBQ
# clientId = JiQ0BAc1DSU5EzgtJishCBQ
# password = cVQTrLjDgySCFMpETyQERX3

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code {}".format(rc))
    channel_ID = "3099763"

    # subscribes to updates to a channel field from a private channel
    client.subscribe("channels/%s/subscribe/fields/field1" % (channel_ID))

def on_disconnect(client, userdata, rc):
    print("Disconnected From Broker")

def on_message(client, userdata, message):
    print(message.payload.decode())
    # print(message.topic)

client_id = "EC0FOBEWKjU1OQwkHhg1Nx0"
client = mqtt.Client(client_id, callback_api_version=mqtt.CallbackAPIVersion.VERSION2)

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.username_pw_set(
    username="EC0FOBEWKjU1OQwkHhg1Nx0",
    password="yH6AmGkv+BrU7ZltoUCDdY4+"
)

client.connect("mqtt3.thingspeak.com", 1883, 60)
client.loop_forever()