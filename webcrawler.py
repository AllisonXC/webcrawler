import requests

req = requests.get('https://en.wikipedia.org/wiki/Data_science')
webpage = req.text

from bs4 import BeautifulSoup

soup = BeautifulSoup(webpage, 'html.parser')
print(soup.prettify())

paragraph = soup.find('p', attrs={"class":False})

paragraph.find_all('a', attrs={"title":True})

data = {"title":[], "href":[]}
for link in paragraph.find_all('a', attrs={"title":True}):
    data["title"].append(link["title"])
    data["href"].append(link["href"])

import pandas as pd
df = pd.DataFrame(data)

webpages = []
head = "https://en.wikipedia.org"
for href in data["href"]:
    link = head + href
    req = requests.get(link)
    webpage = req.text
    webpages.append(webpage)

print(webpages)
