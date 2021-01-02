#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Copyright © 2021 - wwyqianqian <wwyqianqian@mails.ccnu.edu.com>


from bs4 import BeautifulSoup
import json
import requests
import re
import os




movieid = list()
title = list()
search_mov_url = list()
genres = list()

for line in open("movies.dat", encoding = "ISO-8859-1"):
    movieid.append(line.rstrip().split("::")[0])
    title.append(line.rstrip().split("::")[1])
    genres.append(line.rstrip().split("::")[2])


for i in title:
    line = str(i)
    search_name = line.replace(' ', '+')
    search_name = search_name.replace('(', '%28')
    search_name = search_name.replace(')', '%29')
    search_name = search_name.replace("'", '%27')
    search_name = search_name.replace('&', '%26')
    search_name = search_name.replace('!', '%21')
    search_name = search_name.replace(',', '%2C')
    search_name = search_name.replace(':', '%3A')
    search_name = search_name.replace('?', '%3F')
    search_name = search_name.replace('/', '%2F')

    # print(title[movie_count], search_name) // now the movie names are encoded
    # https://www.imdb.com/find?s=tt&q=
    encode_url = "https://www.imdb.com/find?s=tt&q=" + search_name
    search_mov_url.append(search_name)




# mov_search_url_list = list()

# def get_url_list(rootdir):
#     with open(rootdir, 'r') as file_to_read:
#         while True:
#             line = file_to_read.readline()
#             if not line:
#                 break
#             line = line.strip('\n')
#             mov_search_url_list.append(line)
#     return mov_search_url_list


def get_title_id(index, url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text)
        # print(soup)
    except Exception as e:
        print("Get Movie URL failed!")
        with open('err_log.txt', 'a', encoding='utf-8') as f:
            x = index + 1
            f.write(str(x) + ": "+ str(e) + '\n')

    try:
        web_table = soup.find("table", attrs={"class": "findList"})
        # print(web_table.a)
        # <a href="/title/tt0208874/"><img src="https://m.media-amazon.com/images/M/MV5BYTIzYTA5MDEtY2I0OS00OGJhLTlmMDctZWRlMGRjYzAxZDQzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX32_CR0,0,32,44_AL_.jpg"/></a>

        title_id_a_str = str(web_table.a)
        title_id = title_id_a_str.split('/')[2]
        print(index)
        print(title_id) # tt0208874

        with open('excess_log.txt', 'a+', encoding='utf-8') as f:
            f.write(movieid[index] + "::" + title[index] + "::" + genres[index] + "::" + search_mov_url[index] + "::" + "https://www.imdb.com/title/" + title_id + "/" +'\n')


    except Exception as e:
         print("Find title id failed!")
         with open('err_log.txt', 'a', encoding='utf-8') as f:
            x = index + 1
            f.write(str(x) + ": "+ str(e) + '\n')


def main():

    # get_url_list("searchMovUrlList_byLine.txt") #get a list with 3883 items
    for i in range(len(search_mov_url)):
        get_title_id(i, "https://www.imdb.com/find?s=tt&q=" + search_mov_url[i])


main()


# out put:
#     file:
#     - excess_log.txt (2::Jumanji (1995)::Adventure|Children's|Fantasy::Jumanji+%281995%29::https://www.imdb.com/title/tt0113497/)
#     - err_log.txt
#     log :
#         0
#         tt0114709
#         1
#         tt0113497
#         2
#         tt0113228
#         3
#         tt0114885
#         4
#         tt0113041