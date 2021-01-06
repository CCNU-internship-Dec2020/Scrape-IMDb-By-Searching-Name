import pandas as pd

id = list()
user_id = list()
movie_id = list()
rating = list()

id_c = 1

for line in open("ratings.dat", "r"):
    line = line.strip().split("::")
    id.append(id_c)
    id_c += 1
    user_id.append(line[0].strip())
    movie_id.append(line[1].strip())
    rating.append(line[2].strip())

dataframe = pd.DataFrame({'id':id, 'user_id':user_id, 'movie_id':movie_id, 'rating':rating})
dataframe.to_csv("rating_to_mysql.csv",index=False, sep=',')