from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np

#1->pass
#0->fail


X=[[1],[2],[3],[4],[5]]
y=[0,0,1,1,1]








model=LogisticRegression()
model.fit(X,y)


hours=float(input("enter how many hours you studied:  "))
predicted_result=model.predict([[hours]])

if predicted_result==1:
    print(f"based on on your studeud hours {hours},you likedly to pass !!")
else:
    print(f"based on on your studeud hours {hours},you likedly to fail !!")




