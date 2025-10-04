from urllib import request
import json

def thingspeak_get():
    api_key_read = "VX2U30805CIFDI30"
    channel_ID = "3099700"
    url = f"https://api.thingspeak.com/channels/{channel_ID}/fields/1.json?api_key={api_key_read}&results=1"

    req = request.Request(url, method="GET")
    r = request.urlopen(req)
    respone_data = r.read().decode()
    respone_data = json.loads(respone_data)

    # Lấy giá trị field1 từ phần feeds
    feeds = respone_data.get('feeds', [])
    if feeds and 'field1' in feeds[0]:
        value = feeds[0]['field1']
    else:
        value = None

    return value

value = thingspeak_get()
print("Latest field1 value:", value)
