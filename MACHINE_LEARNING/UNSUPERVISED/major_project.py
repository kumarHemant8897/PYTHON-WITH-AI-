import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


df=pd.read_csv("MajorStudent.csv")
print(df.head())

print("data shpe: ")
print(f" number of rows : " ,   {  df.shape[0]}  )
print(f" number of col : "  ,  {  df.shape[1]}  )

print("Dataset info:  ")
print(df.info())

print("summry of the data : ")
print(df.describe(include='all'))

print("misiing values:  ")
print(df.isnull().sum())