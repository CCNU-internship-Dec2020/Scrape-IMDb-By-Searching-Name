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
# print(lost_movieid)
# ['32', '96', '140', '142', '253', '264', '328', '390', '402', '405', '477', '506', '559', '655', '718', '727', '730', '735', '752', '769', '770', '780', '855', '888', '1065', '1107', '1130', '1142', '1144', '1157', '1181', '1202', '1251', '1261', '1294', '1319', '1335', '1340', '1421', '1423', '1430', '1433', '1434', '1454', '1547', '1555', '1559', '1706', '1738', '1792', '1815', '1969', '1976', '1978', '1988', '2014', '2148', '2215', '2227', '2360', '2422', '2503', '2510', '2576', '2586', '2593', '2678', '2783', '2994', '3022', '3145', '3192', '3193', '3279', '3309', '3320', '3399', '3421', '3448', '3487', '3569', '3623', '3664', '3687', '3703', '3819', '3847', '3890', '3892', '3930']

for lost_id_index in range(len(lost_movieid)):
    x = movieid.index(lost_movieid[lost_id_index])
    with open('lost_id_1.txt', 'a+', encoding='utf-8') as f:
        f.write(movieid[x] + "::" + title[x] + "::" + genres[x] + "::" + search_mov_url[x] + "::" + detail_url[x] + '\n')

# output format
# 140::Up Close and Personal (1996)::Drama|Romance::Up+Close+and+Personal+%281996%29::https://www.imdb.com/title/tt0497080/