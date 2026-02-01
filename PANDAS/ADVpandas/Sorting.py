import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data= {
    "Name":['ram','shayam','rohan','abhiraj','hemant','mahi','sonam','raj'],
    "age":[10,45,30,25,26,28,29,30],
    "salary":[50000,60000,60000,40000,90000,70000,60000,45000],
    "Performance_score":[96,90,92,93,85,84,86,88]
}    

df=pd.DataFrame(data)

df.sort_values(by=['age','salary'],ascending=[True,False],inplace=True)
print("sorted ages by descending :")



print("UPDATING DATA IN EXISTING DATASET :  ")
print(df)

