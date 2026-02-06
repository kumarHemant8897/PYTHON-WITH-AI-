import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder

#step 2 converting string data inot a number for machine learning 
#if you have more words in a columns other then yes/no use getdummies()
df=pd.read_csv("MajorStudent.csv")


print("missing vlaues in each column:  ")
print(df.isnull().sum())

le=LabelEncoder()
df['Internet']=le.fit_transform(df["Internet"])
df['Passed']=le.fit_transform(df["Passed"])

print("after encoding ")
print(df.head())

print("dattyoes ")
print(df.dtypes)