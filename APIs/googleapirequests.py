#Using the google API to get a geoJSON. We are using Dr. Chuck's subset of the API which has unlimited attempts

import requests
import json
import ssl

SERVICE_URL = "http://py4e-data.dr-chuck.net/json"
api_key = 42

while True:
    address = input("Enter the address: ")
    if len(address) < 1: break

    url = requests.get(SERVICE_URL, params={"address": address, "key": 42})

    try:
        js = json.loads(url.content)
    except:
        js = None

    if js is None or "status" not in js or js["status"] != "OK":
        print("=====Failure=====")
        print(url.content)
        continue
#Dumping the retrieved JSON
    print(json.dumps(js, indent=4))

    print("Place id: ", js["results"][0]["place_id"])