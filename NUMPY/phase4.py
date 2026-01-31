import numpy as np
import matplotlib.pyplot as plt

arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.random.rand(3,3)
arr3=np.zeros((4,4))

np.save('arr1.npy',arr1)
np.save('arr2.npy',arr2)
np.save('arr3.npy',arr3)


loaded_arr1=np.load('arr1.npy')
print(loaded_arr1)
print("\n")
loaded_arr2=np.load('arr2.npy')
print(loaded_arr2)
print("\n")
loaded_arr3=np.load('arr3.npy')
print(loaded_arr3)




print("\n")