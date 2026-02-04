import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA




#somaple data
data={
    
    'age':[25,30,35,40,45,50],
    'spending':[70,60,50,40,30,20],
    'income':[30000,40000,50000,60000,70000,80000],
    'saving':[1000,5000,10000,15000,20000,6000]
}

df=pd.DataFrame(data)

scaler=StandardScaler()
scaled_data=scaler.fit_transform(df)

pca=PCA(n_components=2)
pca_result=pca.fit_transform(scaled_data)

pca_df=pd.DataFrame(pca_result,columns=['PCA1','PCA2'])

expalin_varience=pca.explained_variance_ratio_
print("varience captured by each compent is :   ")
print(np.round(expalin_varience*100,2))



plt.figure(figsize=(8,6))
plt.scatter(pca_df['PCA1'] ,pca_df['PCA2'],color='black',s=2)
plt.title("PCA projection in (2d view)")
plt.xlabel("PCA1 main patter ")
plt.ylabel("PCA2 minor Pattern")
plt.grid(True)

plt.show()

print("varinece captured by each compenent is : ")
print(pca_df)
