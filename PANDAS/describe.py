import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#df=pd.read_csv("NetflixData.csv")

data= {
    "Name":['ram','rahul','rohan'],
    "age":[10,20,30],
    "city":["bangalore","aligarh","goa"]
}

df=pd.DataFrame(data)
print("sample data frame")
print(df)

print("descritive statics of the data")
print(df.describe())