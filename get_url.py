#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Copyright © 2021 - wwyqianqian <wwyqianqian@mails.ccnu.edu.com>


uid = list()
title = list()
search_mov_url = list()

for line in open("movies.dat", encoding = "ISO-8859-1"):
    uid.append(line.rstrip().split("::")[0])
    title.append(line.rstrip().split("::")[1])

# print(uid[0], title[0]) // now title is a list full of the name of movies

for movie_count in range(0, len(title)):
    search_name = title[movie_count].replace(' ', '+')
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
    search_mov_url.append(encode_url)


# the list of search_mov_url contains the URL of movies searching
# 3883 URLs, 3952 movie_id
# print(search_mov_url)
print(len(search_mov_url))

file=open('searchMovUrlList.txt','a')
file.write(str(search_mov_url));
file.close()

