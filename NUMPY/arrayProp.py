import numpy as np
#arr=np.array([[1,2,3] , [4,5,6]])

arr=np.arange(12)
print("original array: " ,arr)
print("\n")
print("SHAPE: " ,arr.shape)
print("Dimension : ", arr.ndim)
print("SIZE : ", arr.size)
print("DATATYPE  : ", arr.dtype)

print("\n")
reshaped=arr.reshape((3,4))
print("reshaped array: " ,reshaped)

print("\n")
flattened=reshaped.flatten()
print("flattend array: " ,flattened)

print("\n")
raveled=reshaped.ravel()
print("raveld array: " ,raveled) #return view insted of coply 

print("\n")
transpose=reshaped.T
print("traspose  array: " ,transpose)