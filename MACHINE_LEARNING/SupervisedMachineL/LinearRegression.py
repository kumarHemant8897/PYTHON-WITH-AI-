from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

X=[[1],[2],[3],[4],[5]]
y=[30,36,48,60,80]








model=LinearRegression()
model.fit(X,y)


hours=float(input("enter how many hours you studied:  "))
predicted_marks=model.predict([[hours]])
print(f"The expected marks you will got will be:  ",predicted_marks)