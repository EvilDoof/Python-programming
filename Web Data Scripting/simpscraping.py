#Using the requests library

import requests
from bs4 import BeautifulSoup
page = requests.get("https://myanimelist.net/")
fhand = open("htmlfile.html", "w+")
soup = BeautifulSoup(page.content, "html.parser")
fhand.write(soup.prettify())