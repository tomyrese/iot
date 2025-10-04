from gpiozero import LED
from urllib import request, parse
from time import sleep
import json

# Channel ID và API Key
CHANNEL_ID = 794872
API_KEY_WRITE = "VNYLZB86X7YL4NJ3"
API_KEY_READ  = "VSOKSZ9DTNC3Z30"

red = LED(5)   # LED nối vào GPIO5 (chân số 29 trên Raspberry Pi)

def thingspeak_get():
    api_key_read = "VSOKSZ9DTNC3Z30"
    url = "https://api.thingspeak.com/channels/%s/fields/1/last.json?api_key=%s" % (CHANNEL_ID, api_key_read)
    req = request.Request(url, method="GET")
    response_data = request.urlopen(req).read().decode()
    response_data = json.loads(response_data)
    value = response_data['field1']
    return value

while True:
    value = thingspeak_get()
    print("Giá trị đọc từ ThingSpeak:", value)

    if value == "1":
        red.on()
    else:
        red.off()
    
    sleep(1)