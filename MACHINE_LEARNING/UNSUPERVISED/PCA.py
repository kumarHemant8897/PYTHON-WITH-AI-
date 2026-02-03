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

