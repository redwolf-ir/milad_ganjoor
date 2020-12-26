import requests
from bs4 import BeautifulSoup
from pprint import pprint
import sys
import os


poet_link = "https://ganjoor.net/abusaeed/"
page = requests.get(str(poet_link))
soup = BeautifulSoup(page.content, 'html.parser')

names = soup.find_all(
    "a", href=lambda href: href and str(poet_link) in href)[3:]
for a in names:
    poemlink = a['href']
    name_of_poem = poemlink[20:-1]
    print(name_of_poem)
