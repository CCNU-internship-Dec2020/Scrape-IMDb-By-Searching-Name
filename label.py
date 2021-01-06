import pandas as pd

movie_id = list()
label_id = list()
id = list()
id_c = 1
label_dict = {'Film-Noir': 1,
 'Crime': 2,
 'Romance': 3,
 'Fantasy': 4,
 'Horror': 5,
 "Children's": 6,
 'Action': 7,
 'War': 8,
 'Thrill3er': 9,
 'Sci-Fi': 10,
 'Drama': 11,
 'Western': 12,
 'Musical': 13,
 'Documentary': 14,
 'Animation': 15,
 'Comedy': 16,
 'Mystery': 17,
 'Thriller': 18,
 'Adventure': 19}

for line in open("format_data.dat", "r"):
    line = line.strip().split("::")
    labels = line[2].strip().split("|")
    for i in labels:
        movie_id.append(line[0].strip())
        label_id.append(label_dict[i])
        id.append(id_c)
        id_c += 1

dataframe = pd.DataFrame({'id':id, 'label_id':label_id, 'movie_id':movie_id})
dataframe.to_csv("movie_label_to_mysql.csv",index=False, sep=',')