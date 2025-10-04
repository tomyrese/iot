from urllib import request, parse
from time import sleep
import json

def thingspeak_get():
    api_key_read = "VSOKXS2QDTNC3Z30"
    channel_ID = "794872"
    req = request.Request('#')

    r = request.urlopen(req)
    respone_data = r.read().decode()
    respone_data = json.loads(respone_data)
    value = respone_data['field1']
    return value
value = thingspeak_get()