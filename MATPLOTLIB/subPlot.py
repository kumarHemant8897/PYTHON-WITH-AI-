import matplotlib.pyplot as plt
import numpy as np


#1->to compare multipli chats
# 2 -> quickly analyze sama data toghther
#plt.subpplot(nrows,ncol,index)

x=[1,2,3,4]
y=[10,25,15,25]

plt.subplot(1,2,1) # 1 row, 2 col, 1 index
plt.plot(x,y)
plt.title("line chart")


plt.subplot(1,2,2)
plt.bar(x,y)
plt.title("bar chart")

plt.tight_layout()





plt.show()