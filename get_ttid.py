#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Copyright © 2021 - wwyqianqian <wwyqianqian@mails.ccnu.edu.com>


from bs4 import BeautifulSoup
import json
import requests
import re


def get_title_id(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text)
        # print(soup)
    except Exception as e:
        print("Get Movie URL failed!")

    try:
        web_table = soup.find("table", attrs={"class": "findList"})
        # print(web_table.a)
        # <a href="/title/tt0208874/"><img src="https://m.media-amazon.com/images/M/MV5BYTIzYTA5MDEtY2I0OS00OGJhLTlmMDctZWRlMGRjYzAxZDQzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX32_CR0,0,32,44_AL_.jpg"/></a>

        title_id_a_str = str(web_table.a)
        title_id = title_id_a_str.split('/')[2]
        print(title_id) # tt0208874

    except Exception as e:
         print("Find title id failed!")


def main():
    get_title_id("https://www.imdb.com/find?s=tt&q=The+Contender+%282000%29")

main()