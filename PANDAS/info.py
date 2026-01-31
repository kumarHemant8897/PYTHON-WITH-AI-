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



print("display thie info of sataset")
print(df.info())
