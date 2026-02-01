import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data= {
    "Name":['ram','shayam','rohan','abhiraj','hemant','mahi','sonam','raj'],
    "age":[10,None,30,25,26,28,29,30],
    "salary":[50000,None,60000,40000,90000,70000,60000,45000],
    "Performance_score":[96,None,92,93,85,84,86,88]
}    

df=pd.DataFrame(data)
#fil estimated data on the place of missing values by looking at the other values in the same colums
#this method is called interpolation
#-> prreseve data intergrity
#->prevent smooth trends
#->avoid data loss
#->linear,polynomial,time,quardtic
#->axis=0 -> row and axis=1->column
#

# ensure proper dtypes before interpolating to avoid FutureWarning
df.infer_objects(copy=False)

df.interpolate(method='linear',axis=0,inplace=True)








print("UPDATING DATA IN EXISTING DATASET :  ")
print(df)

