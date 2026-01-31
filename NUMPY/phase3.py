import numpy as np
import matplotlib.pyplot as plt
sales_data=np.array ([[1,150000,180000,220000,250000],
                      [2,120000,140000,160000,190000],
                      [3,200000,230000,260000,300000],
                      [4,180000,210000,240000,270000],
                      [5,180000,210000,240000,270000],
                      [6,160000,185000,205000,230000]
                      ])

print("==== ZOMATO SALES ANALYSIS ====")
print("\n shaped of this data " , sales_data.shape)

print("\n sample data for first 3 resurantes :\n " , sales_data[:3])



#TOTAL SALES PER YEAR
print("\n")
print("total sales per year : ", np.sum(sales_data,axis=0))
year_total=np.sum(sales_data[: , 1:] ,axis=1)
print("year total : ", year_total)
total=np.sum(year_total[:])
print("TOTAL AMOUNT:  ", total)
print("\n")
print("\n")



#MINIMUN SALES PER RESUTURNAT 
min_sales=np.min(sales_data[:,1:],axis=1)
print("Min sales per reutrant is :  ",min_sales)
print("\n")

#MAXINMIN SALES PER RESUTRNAT 
max_sales=np.max(sales_data[:,1:],axis=1)
print("Max sales per resutnat is ::" , max_sales)
print("\n")


#MAXINMIN SALES PER year
max_sales=np.max(sales_data[:,1:],axis=0)
print("Max sales per year is ::" , max_sales)
print("\n")

#AVRAGE SALE SPER RESUTANT 
avg_sales=np.mean(sales_data[:,1:],axis=1)
print("avrage sales per resutrant is :: ", avg_sales)
print("\n")


#CUMMALATIVE SALES
cumsum=np.cumsum(sales_data[:,1:],axis=1)
print("Cummalative sales of is :: " ,cumsum)

plt.figure(figsize=(10,6)) 
plt.plot(np.mean(cumsum,axis=0))
plt.title("AVRAGE CUMLATIVE SLAES PER YEAR ACROSS ALL RESURANT ")
plt.xlabel("year")
plt.ylabel("sales")
plt.grid(True)
plt.show()

print("\n")