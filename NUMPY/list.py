import numpy as np
import time

py_list=[1,2,3]
print("python list multiplication", py_list*2)

np_array=np.array([1,2,3])
print("python array multipplication ", np_array*2)


start=time.time()
py_list=[i*2 for i in range(100000)]
print("\n list multiplcation time is : ", time.time()-start)


start=time.time()
np_array=np.arange(100000) * 2 
print("\n array multiplication time is :" , time.time()-start )