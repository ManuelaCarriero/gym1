# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 08:23:04 2022

@author: asus
"""

import numpy as np
from matplotlib import pyplot as plt 

t = np.arange(0., 1000, 0.2)
y=np.abs(-np.exp(-t/1068)+np.exp(-t/46))

plt.title("") #signal vs time 
plt.xlabel("x") #time
plt.ylabel("y") #signal
plt.plot(t,y) 
plt.grid()

# Finding the maximum x and y value of the y function
print(max(y))
x_max = t[np.argmax(y)] 


