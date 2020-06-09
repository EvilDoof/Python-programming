#A spider used to crawl twitter an retrive the friends of the user name

import requests
from requests_oauthlib import OAuth1
import sqlite3
import json
import hidden

SERVICE_URL = "https://api.twitter.com/1.1/friends/list.json"

comm = sqlite3.connect("twfriends.sqlite")
cur = comm.cursor()

keys = hidden.oauth()

auth = OAuth1(keys["consumer_key"], keys["consumer_secret"], keys["token_key"], keys["token_secret"])

cur.execute("CREATE TABLE IF NOT EXISTS Twitter (name TEXT, retrieve INTEGER, friends INTEGER)")

while True:
    acc = input("Enter the account name: ")
    if (acc == "quit"): break
    if (len(acc) < 1):
        cur.execute("SELECT name FROM Twitter WHERE retrieve = 0 LIMIT = 1")
        try:
            acc = cur.fetchone()[0] #Returns a single row as a list, hence we take one first element: name
        except:
            print("No accounts found")
            continue

    url = requests.get(SERVICE_URL, auth = auth, params={"screen_name": acc, "count": "5"})

    print("Retrieving url:", url)

    headers = url.headers
    print("Remaining:", headers["x-rate-limit-remaining"])

    js = json.loads(url.text)

    countnew = 0
    countold = 0
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1',
                    (friend, ))
        try:
            count = cur.fetchone()[0]
            cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?',
                        (count+1, friend))
            countold = countold + 1
        except:
            cur.execute('''INSERT INTO Twitter (name, retrieve, friends)
                        VALUES (?, 0, 1)''', (friend, ))
            countnew = countnew + 1
    print('New accounts=', countnew, ' revisited=', countold)
    comm.commit()
    url.close()

cur.close()


