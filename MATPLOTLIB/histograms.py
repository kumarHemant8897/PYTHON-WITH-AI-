import matplotlib.pyplot as plt
import numpy as np

#plt.hist(data,bins='number of bins' , colors='color name, edge color='black)
score=[45,65,84,97,20,45,45,75,48,41,45,64,52,30,12,88,77,99,45,11,20]
plt.hist(score,bins=150,color='purple',edgecolor='black')
plt.xlabel(" score range")
plt.ylabel(" number of student")
plt.title("SCORE DISTRIBUTION OF SCORE ")




plt.show()