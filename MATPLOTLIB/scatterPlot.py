import matplotlib.pyplot as plt
import numpy as np

hours=[1,2,3,4,5,6,7,8]
score=[50,55,44,66,33,11,100,90]
plt.scatter(hours,score, color='green',marker='o',label='student data')
plt.xlabel("hours studeis")
plt.ylabel("exam score")
plt.title("RELATIOSHIP BW STDY TIME AND EXMA")
plt.legend()
plt.grid(True)

plt.show()