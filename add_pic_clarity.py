#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Copyright © 2021 - wwyqianqian <wwyqianqian@mails.ccnu.edu.com>


movieid = list()
title = list()
genres = list()
search_mov_url = list()
detail_url = list()
img = list()
content = list()

new_img = list()


# input format
# 1::Toy Story (1995)::Animation|Children's|Comedy::Toy+Story+%281995%29::https://www.imdb.com/title/tt0114709/::https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg::A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.
for line in open("Scrape_IMDb.txt", encoding = "ISO-8859-1"):
    movieid.append(line.rstrip().split("::")[0])
    title.append(line.rstrip().split("::")[1])
    genres.append(line.rstrip().split("::")[2])
    search_mov_url.append(line.rstrip().split("::")[3])
    detail_url.append(line.rstrip().split("::")[4])
    img.append(line.rstrip().split("::")[5])
    content.append(line.rstrip().split("::")[6])


# ['@xx','@xx','@xx','@xx'] 3694 items in img list
for pic_index in range(len(img)):
    new_img.append(img[pic_index].rstrip().split("._")[0])

# print(len(new_img))

    with open('Scrape_IMDb_pic_clarity.txt', 'a+', encoding='utf-8') as f:
        f.write(movieid[pic_index] + "::" + title[pic_index] + "::" + genres[pic_index] + "::" + search_mov_url[pic_index] + "::" + detail_url[pic_index] + "::" + new_img[pic_index] + ".jpg::" + content[pic_index] + '\n')

# output format
# 1::Toy Story (1995)::Animation|Children's|Comedy::Toy+Story+%281995%29::https://www.imdb.com/title/tt0114709/::https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@.jpg::A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.