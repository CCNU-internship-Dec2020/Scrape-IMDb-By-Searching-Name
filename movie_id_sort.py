#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Copyright © 2021 - wwyqianqian <wwyqianqian@mails.ccnu.edu.com>


result = []

with open('Scrape_IMDb_pic_clarity.txt','r') as f:
    for line in f:
        result.append(list(line.strip('\n').split('::')))

# print(result)
# [[aa, xx], [bb, xx], [cc, xx]]
# ['3336',
# 'It Happened Here (1961)',
# 'Drama',
# 'It+Happened+Here+%281961%29',
# 'https://www.imdb.com/title/tt0055024/',
# 'https://m.media-amazon.com/images/M/MV5BZjdmMmE5OTctMjdmOC00ODc5LThlMjItNTczZDI4ZmI5YzdmXkEyXkFqcGdeQXVyNjE5NjI4NzI@.jpg',
# 'In 1940, the Nazis invade Britain and transform it into a fascist state where some Britons collaborate and others resist. In 1944, an apolitical Irish nurse becomes a reluctant player in the fight between the two sides.'],


for i in range(len(result)):
    result[i][0] = int(result[i][0])
new = sorted(result, key = (lambda x:x[0]))

print(new)