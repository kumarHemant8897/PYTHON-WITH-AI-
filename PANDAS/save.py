import pandas as pd

data= {
    "Name":['ram','rahul','rohan'],
    "age":[10,20,30],
    "city":["bangalore","aligarh","goa"]
}

df=pd.DataFrame(data)
print(df)


df.to_csv("output.csv",index=False)