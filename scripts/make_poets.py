import requests
from bs4 import BeautifulSoup
from pprint import pprint
import sys

html_1 = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
"""

html_2 = """
    <link rel="stylesheet" href="../assets/css/style.css" />
    <meta
      name="description"
      content="صفحه اصلی گرفتن فال حافظ با تعبیر دقیق و خواندن شعر به صورت ناطق"
    />
    <meta
      name="keywords"
      content="تعبیر فال حافظ , تفال بر حضرت حافظ, فال حافظ دقیق , فال حافظ شیرازی , فال حافظ شب یلدا , فال حافظ صوتی , فال حافظ عشقی , فال حافظ موبایل , فال حافظ ناطق , معنی فال حافظ"
    />
  </head>
  <body>
  <?php include '../includes/header.html';?>
      <div class="container">
      <section class="single-page-poet">
        <div class="poet-picture">
          <div class="poet-picture-part">
            <picture>
"""

html_3 = """
          </div>
          <ul class="like-part">
            <li>LIKE</li>
            <li>DISLIKE</li>
          </ul>
        </div>
        <div class="poet-info">
          <ul class="breadcast">
"""

html_4 = """
          </ul>
          <div class="poet-content">
            <h3>گذری بر زندگی‌نامه ایشان</h3>
            <p>
"""

html_5 = """
            </p>
          </div>
          <div class="poet-content">
"""

html_6 = """
            </ul>
          </div>
        </div>
      </section>
    </div>
    <?php include '../includes/footer.html';?>
  </body>
</html>
"""


link = "https://ganjoor.net/"
page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')
name = soup.findAll("div", {"class": "poet"})
main_html = ""

for res in name:
    poet_link = res.find('a')['href']
    poet_name_en = res.find('a')['href'][20:-1]
    poet_name_fa = res.text
    main_html += html_1 + "\n"
    main_html += '<title>' + "گنجور" + " > " + \
        str(poet_name_fa) + '</title>\n'
    main_html += html_2 + "\n"
    main_html += '<img src = "./assets/img/poets/' + \
        str(res.find('a')['href'][20:-1]) + \
        '.png" alt = "' + str(res.text) + '"></picture>'
    main_html += '<h1>' + str(poet_name_fa) + '</h1>'
    main_html += html_3
    main_html += '<li><a href="/poets/' + \
        str(poet_name_en) + '/">' + str(poet_name_fa) + '</a></li>'
    main_html += html_4

    page = requests.get(str(poet_link))
    soup2 = BeautifulSoup(page.content, 'html.parser')
    biography = soup2.find("p")
    main_html += str(biography)
    main_html += html_5
    main_html += '<h3>آثار ' + str(poet_name_fa) + ' در این مجموعه</h3><ul>'
    data = soup2.findAll('div', attrs={'class': 'poem'})
    for div in data:
        links = div.find_all(
            "a", href=lambda href: href and str(poet_link) in href)[3:]
        for a in links:
            main_html += "<li>" + str(a.text) + "</li>"
    main_html += html_6

    if str(poet_name_en) == "hatef/divan-hatef/gar":
        continue

    f = open('poets/' + str(poet_name_en) + '.php', 'w', encoding='utf-8')
    f.write(str(main_html))
    f.close()
    main_html = ""

print("its Done ...")
