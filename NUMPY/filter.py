import numpy as np
numbers=np.array([1,2,3,4,5,6,7,8,9,10])
even_numbers=numbers[numbers % 2 ==0]
print("EVEN NUMBERS :", even_numbers)
print("\n")

mask=numbers>5
print("NUmber greate then 5 are : " , numbers[mask])

print("\n")

indices=[0,2,4]
print("this indices are::  " ,numbers[indices])

where_result=np.where(numbers> 5)
print("NP where : ", numbers[where_result])
print("\n")


#CCONDIATIOn ARRAY

condition_array=np.where(numbers>5,numbers*4,numbers)
print("condition array:: ", condition_array)

print("\n")

condition_array=np.where(numbers>5,"true","false")
print("condition array:: ", condition_array)




print("\n")

##adding data or removing data

arr1=np.array([4,5,6])
arr2=np.array([7,8,9])

combined=np.concatenate((arr1,arr2))
print("conbined noth array :: " , combined)
print("\n")


#array COMPATIBLITY

a=np.array([1,2,3])
b=np.array([4,5,6,8])
c=np.array([7,8,9])

print("comaptiblity dhapes :: ", a.shape == b.shape)
print("\n")

original=np.array([[1,2],[3,4]])
new_row=([[8,9]])

with_new_row=np.vstack((original,new_row))
print(original)
print("\n")
print(with_new_row)
print("\n")


new_Col=np.array([[2],[4]])
with_new_col=np.hstack((original,new_Col))
print(original)
print("\n")
print(with_new_col)


#DELET OPRATION
arr=np.array([1,2,3,4,5,6])
deledted=np.delete(arr,1)
print("deledted:  ", deledted)






print("\n")