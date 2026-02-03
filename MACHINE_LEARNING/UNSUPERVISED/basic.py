import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error
from sklearn.cluster import KMeans




#somaple data
data={
    'cutomer':['riya','aman','fiazan','neha','imran','senha'],
    'age':[20,30,40,42,38,25],
    'spending':[100,200,300,110,290,130]
}

df=pd.DataFrame(data)

X=df[['age','spending']]

model=KMeans(n_clusters=2,random_state=42,n_init=10)

df['group']=model.fit_predict(X)

plt.figure(figsize=(6,5))
for group in df['group'].unique():
    group_data=df[df['group']==group]  #this called masking
    plt.scatter(group_data['age'],group_data['spending'],label=f'group{group}')


plt.xlabel("age")
plt.ylabel("spdending score")
plt.title("customer segmentaion (kmenas)")
plt.legend()
plt.grid(True)
plt.show()

print(df)