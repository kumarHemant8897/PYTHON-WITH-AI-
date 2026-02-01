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
print("---SAMPLE DATA-----")
print(df)
print("\n")

avg_salary=df['age'].mean()
print("avgrage age if data is :   ",avg_salary)
print()


sumAGE=df['age'].mean()
print("TOATL SUM OF AGES IS  if data is :   ",sumAGE)
print()


min_age=df['age'].min()
print("min age from the  data is :   ",min_age)
print()


max_age=df['age'].max()
print("max age of the data is :   ",max_age)
print()
