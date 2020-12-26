import requests
from bs4 import BeautifulSoup
from pprint import pprint
import sys
import os

main_html = ""
header_html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link rel="stylesheet" href="../../assets/css/style.css" />
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

link = "https://ganjoor.net/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "*",
    "Connection": "keep-alive"
}

try:
    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    name = soup.findAll("div", {"class": "poet"})

    for res in name:
        poet_link = res.find('a')['href']
        page2 = requests.get(str(poet_link))
        soup2 = BeautifulSoup(page2.content, 'html.parser')
        names = soup2.find_all(
            "a", href=lambda href: href and str(poet_link) in href)[3:]
        poet_name = soup2.find("h2")
        poet_name_en = res.find('a')['href'][20:-1]

        for a in names:
            poemlink = a['href']
            name_of_poem = poemlink[20:-1]
            poem = requests.get(poemlink)
            poem_soup = BeautifulSoup(poem.content, 'html.parser')
            main_html = ""

            if poem_soup.find_all("div", {"class": "m1"}):
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
                save_path = os.path.join("poets", str(poet_name_en))

                if not os.path.exists(save_path):
                    os.makedirs(save_path)

                f = open("poets/%s.php" %
                         name_of_poem, 'w', encoding='utf-8')
                f.write(str(main_html))
                f.close()
                print("done ...")

            else:
                poem_header = a.string
                main_html += header_html
                main_html += "<h2>" + str(poet_name) + "</h2>"
                main_html += "<h1>" + str(poem_header) + "</h1>"
                main_html += after_header
                main_html += "<h3>" + str(poem_header) + "</h3>"
                main_html += "<ul>"

                all_sub_poems = poem_soup.find_all(
                    "a", href=lambda href: href and "%s/sh" % name_of_poem in href)
                for a in all_sub_poems:
                    main_html += "<li>" + \
                        '<a href="%s">' % a["href"] + \
                        str(a.string) + "</a></li>"
                main_html += "</ul>" + after_poems
                save_path = os.path.join("poets", str(poet_name_en))
                if not os.path.exists(save_path):
                    os.makedirs(save_path)

                f = open("poets/%s.php"
                         % name_of_poem, 'w', encoding='utf-8')
                f.write(str(main_html))
                f.close()
                print("done ...")
except requests.ConnectionError as e:
    print("  Failed to open url")
