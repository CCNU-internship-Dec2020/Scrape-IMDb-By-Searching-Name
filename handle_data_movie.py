import pandas as pd

id = list()
introduce = list()
title = list()
url = list()

for line in open("format_data.dat", "r"):
    line = line.strip().split("::")
    id.append(line[0].strip())
    introduce.append(line[6].strip())
    title.append(line[1].strip())
    url.append(line[5].strip())

dataframe = pd.DataFrame({'id':id, 'introduce':introduce, 'title':title, 'url':url})
dataframe.to_csv("movie_to_mysql.csv",index=False, sep=',')