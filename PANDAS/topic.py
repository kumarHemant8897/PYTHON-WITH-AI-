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


#chosse a specific coloumn
#fliter row
#combined multiple conditions

#selecting a single column 
print("names single columns only :  ")
title=df['title']
print(title)
print("\n")



#selecting multiplie column
print("names title and country   MUltiple column columns only :  ")
subset=df[['title','country']]
print(subset)
print("\n")


#foletring rows 
new_moveis=df[df['release_year'] > 2010]
print("moveis relaese after  in 2000 are : ")
print(new_moveis)

#fitering row with more then one conditions
# Filtering rows with more than one condition

filtered = df[
    (df['release_year'] > 2010) &
    (df['duration'].str.contains('min')) &
    (df['duration'].str.extract('(\d+)').astype(int) > 60)
]

print("Movies released after 2010 with duration above 60 minutes:")
print(filtered)

