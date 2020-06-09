#This is used to generate sign the request URL with the tokens to provide access

import requests
from requests_oauthlib import OAuth1
import hidden
import json

SERVICE_URL = "https://api.twitter.com/1.1/search/tweets.json"

fhand = open("tweets.txt","w+")

keys = hidden.oauth()

auth = OAuth1(keys["consumer_key"], keys["consumer_secret"], keys["token_key"], keys["token_secret"])

url = requests.get(SERVICE_URL, auth = auth, params={"q":"@realDonaldTrump", "count": "5"})

headers = dict(url.headers)
print("Remaining:", headers["x-rate-limit-remaining"])

js = json.loads(url.text)
for u in js["statuses"]:
    fhand.write(u["text"] + "\n")

fhand.close()