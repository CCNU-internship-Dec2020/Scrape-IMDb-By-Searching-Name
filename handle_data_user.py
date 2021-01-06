import pandas as pd

id = list()
age = list()
gender = list()
occ = list()
password = list()
role = list()

for line in open("users.dat", "r"):
    line = line.strip().split("::")
    id.append(line[0].strip())
    gender.append(0 if line[1].strip() == "F" else 1)
    # gender.append(line[1].strip())
    age.append(line[2].strip())
    occ.append(line[3].strip())
    password.append("pbkdf2:sha256:150000$V8aMwj86$7a62b8c5c2e7b975e711524e6f1232074f70083d022b376f0d07e7f38c2a497c")
    role.append(0)

dataframe = pd.DataFrame({'id':id, 'username':id, 'age':age, 'gender':gender, 'occupation':occ, 'password_hash':password, 'role':role})
dataframe.to_csv("user_to_mysql.csv",index=False, sep=',')