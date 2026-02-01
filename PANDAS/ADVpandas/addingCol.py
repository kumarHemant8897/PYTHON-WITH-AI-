import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#modifuication of data in this lecture


#df=pd.read_csv("NetflixData.csv")

data= {
    "Name":['ram','rahul','rohan','abhiraj','hemant','mahi','sonam','raj'],
    "age":[10,20,30,25,26,28,29,30],
    "salary":[50000,120000,60000,40000,90000,70000,60000,45000],
    "Performance_score":[96,91,92,93,85,84,86,88]
}    

df=pd.DataFrame(data)
#adding a new column called bonus
df["bonus"]= df['salary']* 0.1

print("\n")

#using insert method
df.insert(0,"employe_id",[10,45,65,75,48,52,55,26])




print("sample data frame")
print(df)

