import requests
from bs4 import BeautifulSoup
from pprint import pprint
import sys


link = "https://ganjoor.net/razi/saghiname/"
page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')
# beyt_1 = soup.findAll("div", {"class": "m1"})
# beyt_2 = soup.findAll("div", {"class": "m2"})
# main_html = ""

# index = 0
# for a in beyt_1:
#     main_html += "<p>" + str(a.text) + "</p>"
#     main_html += "<p>" + str(beyt_2[index].text) + "</p>"
#     index += 1

print(soup)
