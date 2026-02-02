from sklearn.preprocessing import LabelEncoder
import pandas as pd

df=pd.read_csv("sample_data.csv")

df_label=df.copy()


le=LabelEncoder()
df_label['Gender_Encoded']=le.fit_transform(df_label['Gender'])
df_label['Passed_Encoded']=le.fit_transform(df_label['Passed'])

#print('\n Label encodede data')

#print(df_label[['Name','Gender','Gender_Encoded','Passed','Passed_Encoded']])

print("\n")
print("\n")
print("------USING HOT ENCODING METHOD------")


df_encoded=pd.get_dummies(df_label,columns=['City'])
print('\n  onr hot Encoded data(City ')

df_city_bool = pd.get_dummies(df, columns=['City'], dtype=int)
print(df_city_bool)








