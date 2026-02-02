from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np





X=[
    [7,8],
    [8,3],
    [9,8],
    [10,9]
]
#0->allple
#``1->orange
y=[0,0,1,1]
model=DecisionTreeClassifier()

model.fit(X,y)
size=float(input("enter the size in cm:  "))
shade=float(input("enter the color shade :  "))

predication=model.predict([[size,shade]])[0]
if predication==0:
    print("this is a APPLE")
else:
    print("this is a orange ")





