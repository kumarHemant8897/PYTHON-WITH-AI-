import matplotlib as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,root_mean_squared_error
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from sklearn.preprocessing import LabelEncoder


df=pd.read_csv("Student_simple.csv")

print("summary of the data : ")
print(df.describe(include='all'))

print("")

print("print top 5 ")
print(df.head())
print("\n")

print("check the msiiong values:  ")
print(df.isnull().sum())
print("\n")

print("information of the data:; ")
print(df.info())



df_fname_bool = pd.get_dummies(df, columns=['First_Name'], dtype=int)
print(df_fname_bool)


df_lname_bool = pd.get_dummies(df, columns=['Last_Name'], dtype=int)
print(df_lname_bool)


df_gender_bool = pd.get_dummies(df, columns=['Gender'], dtype=int)
print(df_gender_bool)


df_department_bool = pd.get_dummies(df, columns=['Department'], dtype=int)
print(df_department_bool)


df_mail_bool = pd.get_dummies(df, columns=['Email'], dtype=int)
print(df_mail_bool)

print("\n")

print("after encoding ")
print(df.head())

print("dattyoes ")
print(df.dtypes)

print("\n")
print(df.info)




