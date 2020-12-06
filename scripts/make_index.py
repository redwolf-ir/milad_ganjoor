import requests
from bs4 import BeautifulSoup
from pprint import pprint
import sys


top = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link rel="stylesheet" href="./assets /css/style.css" />
  </head>
  <body>
<?php include 'includes/header.html';?>
    <div class="container">
      <section class="poets">
        <h3>شاعران پارسی زبان</h3>
        <ul class="poets-part">
"""


bottom = """
        </ul>
      </section>
    </div>
<?php include 'includes/footer.html';?>
"""

main = ""


link = "https://ganjoor.net/"
page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')
name = soup.findAll("div", {"class": "poet"})
main += top
for res in name:
    main = main + '<li><a href="poets/' + str(res.find('a')['href'][20:-1]) + '.php"></a><picture><img src="./assets/img/poets/' + \
        str(res.find('a')['href'][20:-1]) + \
        '.png" alt="' + str(res.text) + '"></picture><p>' + \
        str(res.text) + '</p></li> \n'
main += bottom

f = open('index.php', 'w', encoding='utf-8')
f.write(str(main))
f.close()
