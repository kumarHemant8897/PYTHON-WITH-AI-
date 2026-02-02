from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
import pandas as pd
import matplotlib as plt
import numpy as np

#true answer 
y_true=[1,0,1,1,0,1,0]

#model prdication what it guesed
y_pred=[1,0,1,0,0,1,1]


#EVAlution
print("accuracy : ", accuracy_score(y_true,y_pred))
print("precision : ", precision_score(y_true,y_pred))
print("recall : ", recall_score(y_true,y_pred))
print("f1 score  : ", f1_score(y_true,y_pred))