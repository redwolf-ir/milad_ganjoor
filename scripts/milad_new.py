import requests
from bs4 import BeautifulSoup
from pprint import pprint
import sys
import glob

main_html = ""
header_html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link rel="stylesheet" href="../css/style.css" />
  </head>
  <body>
    <div class="top-svg"></div>
    <nav class="top-nav">
      <div class="container top-nav-flex">
        <h1>گنجینه</h1>
        <ul>
          <li>صفحه نخست</li>
          <li>صفحه نخست</li>
          <li>صفحه نخست</li>
          <li>صفحه نخست</li>
        </ul>
        <form action="">
          <input placeholder="نام شاعر، شعر" type="text" />
          <button>جستجو</button>
        </form>
      </div>
    </nav>
    <div class="container">
      <section class="single-page-poet">
        <div class="poet-picture">
          <div class="poet-picture-part">
            <picture></picture>
"""
after_header = """

          </div>
          <div class="poet-picture-part">
            <audio controls>
              <source
                src="https://www.baharnaz.com/Divan-Voice/Hafez-Song004.mp3"
                type="audio/mp3"
              />
            </audio>
          </div>
          <ul class="like-part">
            <li>LIKE</li>
            <li>DISLIKE</li>
          </ul>
        </div>
        <div class="poet-info">
          <ul class="breadcast">
            <li>خیام</li>
            <li>ترانه‌های خیام (صادق هدایت)</li>
            <li>دم را دریابیم</li>
          </ul>
        <div class="poet-content">
"""
after_poems = """
            </div>
          </div>
        </div>
      </section>
    </div>
    <div class="bottom-svg"></div>
  </body>
</html>
"""


link = "https://ganjoor.net/razi/"
page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')
names = soup.find_all("a", href=lambda href: href and link in href)[4:]
poet_name = soup.find("h2")

for a in names:
    poemlink = a['href']
    name_of_poem = poemlink[25:-1]
    poem = requests.get(poemlink)
    poem_soup = BeautifulSoup(poem.content, 'html.parser')
    h3_numbers = poem_soup.find_all("h3")
    main_html = ""

    if len(h3_numbers) < 3:
        poem_header = a.string
        main_html += header_html
        main_html += "<h2>" + str(poet_name) + "</h2>"
        main_html += "<h1>" + str(poem_header) + "</h1>"
        main_html += after_header
        main_html += "<h3>" + str(poem_header) + "</h3>"
        main_html += '<div class="poem-content">'

        beyt_1 = poem_soup.findAll("div", {"class": "m1"})
        beyt_2 = poem_soup.findAll("div", {"class": "m2"})
        index = 0
        for a in beyt_1:
            main_html += "<p>" + str(a.text) + "</p>"
            main_html += "<p>" + str(beyt_2[index].text) + "</p>"
            index += 1
        main_html += after_poems
        f = open('razi/%s.php' % name_of_poem, 'w', encoding='utf-8')
        f.write(str(main_html))
        f.close()
