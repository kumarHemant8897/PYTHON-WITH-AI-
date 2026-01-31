import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df=pd.read_csv("NetflixData.csv")

print("display first 10 rows")
print(df.head(5))


print("display last 10 rows")
print(df.tail())
