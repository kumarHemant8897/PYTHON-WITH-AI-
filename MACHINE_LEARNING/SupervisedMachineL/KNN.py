from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np

#1->pass
#0->fail



X=[
    [108,7],
    [200,7.5],
    [250,8],
    [300,8.5],
    [330,9],
    [360,9.5]
]
#0->allple
#``1->orange
y=[0,0,0,1,1,1]
model=KNeighborsClassifier(n_neighbors=3)

model.fit(X,y)
weight=float(input("enter the weight in grass:  "))
size=float(input("enter the size in cm:  "))

predication=model.predict([[weight,size]])[0]
if predication==0:
    print("this is a APPLE")
else:
    print("this is a orange ")





