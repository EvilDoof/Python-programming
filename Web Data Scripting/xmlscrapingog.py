#PAsing the XML tree

import xml.etree.ElementTree as ET 
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter the URL: ")
fhand = urllib.request.urlopen(url, context=ctx).read()

tree = ET.fromstring(fhand)
count = tree.findall("comments/comment")
total = 0
for item in count:
    total = total + int(item.find("count").text)

print(total)
