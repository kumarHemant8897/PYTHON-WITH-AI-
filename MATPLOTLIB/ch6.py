import numpy as np
import matplotlib.pyplot as plt
 

#BAR CHATS, PIE CHART , HISTOGRAMS

#plt.bar(x,height,coloe='',widt ='', label='')
product=['A','B','C','D','E']
price=[200,500,400,900,300]

plt.bar(product,price, color='orange',label='sales 2025')
plt.xlabel("product")
plt.ylabel("sales")
plt.title("PRODUCT SPRICE COMPARINSOON")
plt.legend()




plt.show()
