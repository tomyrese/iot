from urllib import request
import json

def thingspeak_get():
    api_key_read = "HCDIIZM6GTHADAER"
    channel_ID = "3092683"
    url = f"https://api.thingspeak.com/channels/{channel_ID}/fields/3.json?api_key={api_key_read}&results=1"
    
    req = request.Request(url, method='GET')
    r = request.urlopen(req)
    response_data = r.read().decode()
    response_data = json.loads(response_data)

    # Lấy phần tử đầu tiên trong feeds
    if "feeds" in response_data and len(response_data["feeds"]) > 0:
        value = response_data["feeds"][0]["field3"]
        return value
    else:
        return None

value = thingspeak_get()
print("Last value in field3:", value)
