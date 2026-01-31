import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv("NetflixData.csv")

print("Rows and columns of data:")
print(df.shape)
print()

print("Names of the columns of the data:")
print(df.columns.tolist())
print("\n")


filtered = df[
    (df['release_year'] > 2010) &
    (df['duration'].str.contains('min')) &
    (df['duration'].str.extract('(\d+)').astype(int) > 60)
]

print("Movies released after 2010 with duration above 60 minutes:")
print(filtered)

