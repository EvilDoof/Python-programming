#Using the google API to get a geoJSON. We are using Dr. Chuck's subset of the API which has unlimited attempts

import urllib.request, urllib.parse, urllib.error
import json
import ssl

#Ignore ssl errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

SERVICE_URL = "http://py4e-data.dr-chuck.net/json?"
api_key = 42

while True:
    address = input("Enter the address: ")
    if len(address) < 1: break

    parms = dict()
    parms["address"] = address
    parms["key"] = 42
    url = SERVICE_URL + urllib.parse.urlencode(parms)
    data = urllib.request.urlopen(url, context=ctx).read()

    try:
        js = json.loads(data)
    except:
        js = None

    if js is None or "status" not in js or js["status"] != "OK":
        print("=====Failure=====")
        print(data)
        continue
#Dumping the retrieved JSON
    print(json.dumps(js, indent=4))

    print("Place id: ", js["results"][0]["place_id"])