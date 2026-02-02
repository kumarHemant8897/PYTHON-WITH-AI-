import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.model_selection import train_test_split

data={
    "studyHours":[2,3,4,5,6],
    "marksScore":[30,40,60,80,90]
    
}


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


print("\n")








# Select only numeric columns for scaling
df_numeric=df_city_bool.select_dtypes(include=['number'])

#STANDARD SCALLER
standard_scler=StandardScaler()
standard_scled=standard_scler.fit_transform(df_numeric)
print("standdard scler output:  ")
print(pd.DataFrame(standard_scled,columns=df_numeric.columns))
print("\n")

#minmaxSCaler 
minmax_scalar=MinMaxScaler()
minmax_scaled=minmax_scalar.fit_transform(df_numeric)
print("MIN MAX SCLAER OUTPUT ")
print(pd.DataFrame(minmax_scaled,columns=df_numeric.columns))


#WORINKING ON TRAIN_TEST_SPLIT
# Use numeric columns for train_test_split
x_train,x_test=train_test_split(df_numeric,test_size=0.2,random_state=42)
print("Training data")
print(x_train)
print()

print("test data")
print(x_test)