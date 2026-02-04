import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,confusion_matrix


#
#
df=pd.read_csv("MajorStudent.csv")

# normalize column names (remove stray leading/trailing spaces)
df.columns = df.columns.str.strip()

le=LabelEncoder()
df['Internet']=le.fit_transform(df["Internet"])
df['Passed']=le.fit_transform(df["Passed"])




# features: exclude the target column and fixed whitespace issues
feature=['StudyHours','Attendance','PastScore','SleepHours']
scaler=StandardScaler()
df_scaled=df.copy()
df_scaled[feature]=scaler.fit_transform(df[feature])






X=df_scaled[feature]  # feature
y=df_scaled['Passed'] # target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=LogisticRegression()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)






print("CLASSIFICATION REPORT:  ")
print(classification_report(y_test,y_pred))

conf_metrics=confusion_matrix(y_test,y_pred)
plt.figure(figsize=(6,4))
sns.heatmap(conf_metrics,annot=True,fmt="d",cmap="Blues",xticklabels=["Fail","Pass"],yticklabels=["Fail","Pass"])
plt.xlabel("predicated")
plt.ylabel("actual")
plt.title("confucion metrices ")
plt.tight_layout()
plt.show()





print("\n")
print("------predicted your result--------- ")
try:
    study_hours=float(input("enter the study hours :  "))
    attendence=float(input("enter the attendence :  "))
    past_score=float(input("enter the past score of yours  :  "))
    sleep_hours=float(input("enter the sleep hous in a day  :  "))

    user_input_df=pd.DataFrame([{
        'StudyHours':study_hours,
        'Attendance':attendence,
        'PastScore':past_score,
        'SleepHours':sleep_hours
    }])

    user_input_scled=scaler.transform(user_input_df)

    predication=model.predict(user_input_scled)[0]
    result="Pass" if predication == 1 else "Fail"
    print(f"predication based on input : {result}")

except Exception as e:
    print(" An error occured !!")


