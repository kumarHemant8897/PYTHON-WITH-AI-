import numpy as np
import matplotlib.pyplot as plt
 

region=['North','South','East','Wesr']
revenue=[3000,5000,4000,9000]

plt.pie(revenue,labels=region,autopct='%1.1f%%',colors=['gold','skyblue','coral','lightgreen'])
plt.title("REVENCUE CONTIBUTION BY REGION ")


plt.show()
