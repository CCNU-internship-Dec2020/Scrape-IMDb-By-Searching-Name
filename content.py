from bs4 import BeautifulSoup
import json
import requests
import os

# input format
# 1::Toy Story (1995)::Animation|Children's|Comedy::Toy+Story+%281995%29::https://www.imdb.com/title/tt0114709/
movieid = list()
title = list()
genres = list()
search_mov_url = list()
detail_url = list()

for line in open("excess_log.txt", encoding = "ISO-8859-1"):
    movieid.append(line.rstrip().split("::")[0])
    title.append(line.rstrip().split("::")[1])
    genres.append(line.rstrip().split("::")[2])
    search_mov_url.append(line.rstrip().split("::")[3])
    detail_url.append(line.rstrip().split("::")[4])


def gethtmltext(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""

def get_img_content(index, url):
    try:
        html = gethtmltext(url)
        soup = BeautifulSoup(html, "html5lib")
        img = str(soup.find(name="div", attrs={"class" :"poster"}).contents[1])
        img = img.split('"')[5]
        content = soup.find(name="div", attrs={"class" :"summary_text"}).contents[0].strip()

        print(str(index + 1) + ": " + content)

        with open('Scrape_IMDb.txt', 'a+', encoding='utf-8') as f:
            f.write(movieid[index] + "::" + title[index] + "::" + genres[index] + "::" + search_mov_url[index] + "::" + detail_url[index] + "::" + img + "::" + content + '\n')

    except Exception as e:
        print(str(index + 1) + "Get image or content failed!")

        with open('scrape_err_log.txt', 'a', encoding='utf-8') as f:
            x = index + 1
            f.write(str(x) + ": "+ str(e) + '\n')


#print(get_img_content("https://www.imdb.com/title/tt0113845"))
#print(len(detail_url))

def main():
    for i in range(len(detail_url)):
        get_img_content(i, detail_url[i])

main()

# out put:
#     file:
#     - Scrape_IMDb.txt
#     - scrape_err_log.txt
#     screen log:
#     1: A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.
#     2: When two kids find and play a magical board game, they release a man trapped in it for decades - and a host of dangers that can only be stopped by finishing the game.