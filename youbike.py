import requests
import json

# youbikeURL = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
# r = requests.get(youbikeURL)
# print(r.status_code)
# for station in json.loads(r.text):
#     print(type(station))
#     print(station["sna"])


str1 = '{"a": null, ' \
        ' "b": true, ' \
        ' "c": 123.4}'
json1 = json.loads(str1)
print(json1)
print(json1["c"])
print(json.dumps(json1))
