#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Copyright © 2021 - wwyqianqian <wwyqianqian@mails.ccnu.edu.com>


movieid = list()
title = list()
genres = list()
search_mov_url = list()
detail_url = list()

got_movieid = list()
got_title = list()
got_genres = list()
got_search_mov_url = list()
got_detail_url = list()
got_img = list()
got_content = list()

lost_movieid = list()


# input format
# 1::Toy Story (1995)::Animation|Children's|Comedy::Toy+Story+%281995%29::https://www.imdb.com/title/tt0114709/
for line in open("excess_log.txt", encoding = "ISO-8859-1"):
    movieid.append(line.rstrip().split("::")[0])
    title.append(line.rstrip().split("::")[1])
    genres.append(line.rstrip().split("::")[2])
    search_mov_url.append(line.rstrip().split("::")[3])
    detail_url.append(line.rstrip().split("::")[4])

# input format
# 1::Toy Story (1995)::Animation|Children's|Comedy::Toy+Story+%281995%29::https://www.imdb.com/title/tt0114709/::https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg::A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.
for got_line in open("Scrape_IMDb.txt", encoding = "ISO-8859-1"):
    got_movieid.append(got_line.rstrip().split("::")[0])
    got_title.append(got_line.rstrip().split("::")[1])
    got_genres.append(got_line.rstrip().split("::")[2])
    got_search_mov_url.append(got_line.rstrip().split("::")[3])
    got_detail_url.append(got_line.rstrip().split("::")[4])
    got_img.append(got_line.rstrip().split("::")[5])
    got_content.append(got_line.rstrip().split("::")[6])


for original_id_index in range(len(movieid)):
    if movieid[original_id_index] not in got_movieid:
        lost_movieid.append(movieid[original_id_index])


# if 90, then correct
print(len(lost_movieid))


