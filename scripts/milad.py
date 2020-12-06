import requests
from bs4 import BeautifulSoup
from pprint import pprint
import sys


link = "https://ganjoor.net/razi/"
page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')
h3_numbers = soup.find_all("h3")
names = soup.find_all("a", href=lambda href: href and link in href)[4:]
for a in names:
    poemlink = a['href']
    print(poemlink)


# if len(h3_numbers) < 3:
    # for a in name:
    #     poemlink = a.string
    #     poemlink = "<li>" + str(poemlink) + "</li>"
    #     main_html += poemlink
    # poem = requests.get(poemlink)
    # poem_soup = BeautifulSoup(poem.content, 'html.parser')

    # top_header = """
    # <!DOCTYPE html>
    # <html lang="en">
    #   <head>
    #     <meta charset="UTF-8" />
    #     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    #     <title>Document</title>
    #     <link rel="stylesheet" href="./css/style.css" />
    #   </head>
    #   <body>
    # <?php include 'header.html';?>
    # <div class="container">
    #       <section class="single-page-poet">
    #         <div class="poet-picture">
    #           <div class="poet-picture-part">
    #             <picture></picture>
    # """
    # after_header_title = """
    #           </div>
    #           <ul class="like-part">
    #             <li>LIKE</li>
    #             <i>DISLIKE</li>
    #           </ul>
    #         </div>
    #         <div class="poet-info">
    #           <ul class="breadcast">
    #             <li>خیام</li>
    #             <li>ترانه‌های خیام (صادق هدایت)</li>
    #             <li>دم را دریابیم</li>
    #           </ul>
    #           <div class="poet-content">
    #             <h3>گذری بر زندگی‌نامه ایشان</h3>
    #             <p>
    # """
    # main_html = ""
    # after_bio = """
    #             </p>
    #           </div>
    #           <div class="poet-content">
    #             <h3>آثار خیام در این مجموعه:</h3>
    #             <ul>
    # """
    # after_poem_link = """
    #             </ul>
    #           </div>
    #         </div>
    #       </section>
    #     </div>
    #     <?php include 'footer.html';?>
    # """
    # main_html += top_header

    # # link = "http://ganjoor.net/"
    # # page = requests.get(link)
    # # soup = BeautifulSoup(page.content, 'html.parser')
    # # name = soup.findAll("div", {"class": "poet"})
    # # fullHtml = ""
    # # myHtml_p1 = "<li><picture></picture><p>"
    # # myHtml_p2 = "</p></li>"

    # # for res in name:
    # #     print(myHtml_p1 + res.text + myHtml_p2)

    # link = "ganjoor.net/razi/"
    # add_html_to_the_first = "https://" + link
    # page = requests.get(add_html_to_the_first)
    # soup = BeautifulSoup(page.content, 'html.parser')
    # poet_name = soup.find("h2")
    # poet_name = "<h1>" + str(poet_name.text) + "</h1>"
    # main_html += poet_name
    # main_html += after_header_title
    # biography = soup.find("p")
    # main_html += str(biography.text)
    # main_html += after_bio
    # name = soup.find_all("a", href=lambda href: href and link in href)[4:]
    # # name = soup.find("p")
    # # print(name)

    # for a in name:
    #     poemlink = aa['href']
    #     poemlink = "<li>" + str(poemlink) + "</li>"
    #     main_html += poemlink
    #     # poem = requests.get(poemlink)
    #     # poem_soup = BeautifulSoup(poem.content, 'html.parser')

    # main_html += after_poem_link
    # # print(main_html)

    # f = open('nezami.php', 'w', encoding='utf-8')
    # f.write(str(main_html))
    # f.close()
# else:
#     print("kiro")
