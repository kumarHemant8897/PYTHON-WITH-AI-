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

#.LOC-> updating set
#df.loc[row_index,"column_name"]=newValue
df.loc[0,"salary"]=4500000



print("UPDATING DATA IN EXISTING DATASET :  ")
print(df)

