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

#dropna()->remove whole column or a row
#dropna(axis=0,inplace=True)
#df.dropna(inplace=True)


#there is a method fill some in value in place of missing data called
#fillna(value, inplace=True)

#df.fillna(0,inplace=True)

#filling a caluplated value

df['age'].fillna(df['age'].mean(), inplace=True)
df['salary'].fillna(df['salary'].mean(), inplace=True)












print("------------MODIFICATION OF DATA UISNG OPERATIONS ------ :  ")
print(df)

print(df.isnull().sum())