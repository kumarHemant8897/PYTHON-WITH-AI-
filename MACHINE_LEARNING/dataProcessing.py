import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data= {
    "Name":['ram',None,'rohan','abhiraj','hemant','mahi','sonam','raj'],
    "age":[10,None,30,25,26,28,29,30],
    "salary":[50000,None,60000,40000,90000,70000,60000,45000],
    "Performance_score":[96,None,92,93,85,84,86,88]
}    

df=pd.DataFrame(data)
print("original Dataframe ")
print(df)
print("\n")
print(df.isnull().sum())
df_drop=df.dropna()
print(df_drop)
