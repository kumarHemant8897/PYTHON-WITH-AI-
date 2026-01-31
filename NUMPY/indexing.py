import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
print("bassic Slicing : ", arr[2:7])
print(" with step slicing : " , arr[1:8:2])
print("Negative indesxing : ", arr[-3])

print("\n")
print("\n")


#2D ARRAY
arr_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])

print("specific elemt:  " , arr_2d[1,2])
print("entrire  row:  " , arr_2d[1])
print("entrire  col:  " , arr_2d[:,1])
print("\n")
print("\n")



#SORTING


unsorted=np.array([4,5,8,7,9,3,1,4])
print("SOrted array::  " , np.sort(unsorted))

arr_2dunsorted=np.array([[1,5,9],[1,5,3],[5,5,6]])
print("2d Sorted array is ::" , np.sort(arr_2dunsorted,axis=0))