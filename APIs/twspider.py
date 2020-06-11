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

cur.execute("CREATE TABLE IF NOT EXISTS Friends (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE, retrieve INTEGER)")

#Table to keep track of friends
cur.execute("CREATE TABLE IF NOT EXISTS Links (friend1 INTEGER, friend2 INTEGER, PRIMARY KEY (friend1, friend2))")

while True:
    acc = input("Enter the account name or enter to quit: ")
    if (len(acc) < 1): break
    if (len(acc) < 1):
        cur.execute("SELECT name, id FROM Friends WHERE retrieve = 0 LIMIT = 1")
        try:
            val = cur.fetchone()
            acc = val[0] #Returns a single row as a list, hence we take one first element: name
            friend1_id = val[1]
        except:
            print("No accounts found")
            continue
    else:
        cur.execute("SELECT retrieve, id FROM Friends WHERE name = ?", (acc,))
        try:
            val = cur.fetchone()
            retrieve = val[0]
            friend1_id = val[1]
            if (retrieve != 0):
                print("Account has already been retrieved")
                continue
            else:
                cur.execute("UPDATE Friends SET retrieve = retrieve + 1 WHERE name = ?", (acc, ))
        except:
            cur.execute("INSERT OR IGNORE INTO Friends (name, retrieve) VALUES ( ?, 1 )", (acc, ))
            friend1_id = cur.lastrowid

    try:
        url = requests.get(SERVICE_URL, auth = auth, params={"screen_name": acc, "count": "100"})
    except Exception as err:
        print("Error retrieving: ", err)
        break

    js = json.loads(url.text)

    countnew = 0
    countold = 0
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        cur.execute('SELECT name FROM Friends WHERE name = ? LIMIT 1',
                    (friend, ))
        try:
            count = cur.fetchone()[0]
            countold = countold + 1
        except:
            cur.execute('''INSERT INTO Friends (name, retrieve)
                        VALUES (?, 0)''', (friend, ))
            countnew = countnew + 1
        friend2_id = cur.lastrowid

        cur.execute("INSERT OR IGNORE INTO Links (friend1, friend2) VALUES ( ?, ? )", (friend1_id, friend2_id))
    print('New accounts=', countnew, ' revisited=', countold)
    comm.commit()

    headers = url.headers
    print("Remaining:", headers["x-rate-limit-remaining"])
    url.close()

cur.close()