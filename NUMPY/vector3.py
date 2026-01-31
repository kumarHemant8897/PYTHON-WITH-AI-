import numpy as np 

vector1=np.array([1,2,3,4,5])
vector2=np.array([6,7,8,9,10])
print("vector addition : ", vector1+vector2)

print("\nMULTIPLICATION OF VECTOR IS ::: ", vector1*vector2)

print("\n DOT product :", np.dot(vector1,vector2))

print("\n")

#VECTOREISZED 
rest_types=(['biryani','cafe','pizza','burger','cafe'])
vectorized_upper=np.vectorize(str.upper)
print("Vectorzied upper : ", vectorized_upper(rest_types))












print("\n")