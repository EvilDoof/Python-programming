#To claculate the sum of numbers from a json file

import json
import urllib.request, urllib.error, urllib.parse
import ssl

#Site name: http://py4e-data.dr-chuck.net/comments_482271.json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter the URL: ")
fhand = urllib.request.urlopen(url, context=ctx).read()
js = json.loads(fhand) #This is a disctionary
total = 0

for num in js["comments"]:
    total = total + int(num["count"])

print("Total: ", total)