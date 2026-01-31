import matplotlib.pyplot as plt
import numpy as np


#saveFig('filename.extension',  dpi= value, bbox_inches='tight')


x=[1,2,3,4,5]
y=[10,20,15,25,44]

plt.plot(x,y,color='blue',marker='o')
plt.title("SIMPLE LINE PLOT ")
plt.xlabel(" x axis value ")
plt.ylabel("y axis label ")
plt.legend()

plt.savefig('LinePlot.png', dpi=300,bbox_inches='tight')








plt.show()