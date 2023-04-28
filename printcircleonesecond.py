# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 10:38:39 2023

@author: asus
"""

import matplotlib.pyplot as plt
from itertools import cycle
import time

startTime = time.time()

def circle1():
    
    fig, ax = plt.subplots()
    
    circle1 = plt.Circle((0.5, 0.5), 0.1, facecolor='None', edgecolor='green')
        
    ax.add_patch(circle1)
    
    plt.show()

circle1()

time.sleep(1)

def circle2():
    
    fig, ax = plt.subplots()
    
    circle2 = plt.Circle((0.5, 0.5), 0.2, facecolor='None', edgecolor='green')
        
    ax.add_patch(circle2)
    
    plt.show()

circle2()

time.sleep(1)

def circle3():
    
    fig, ax = plt.subplots()
    
    circle3 = plt.Circle((0.5, 0.5), 0.3, facecolor='None', edgecolor='green')
        
    ax.add_patch(circle3)
    
    plt.show()

circle3()

time.sleep(1)




def circle4():
    
    fig, ax = plt.subplots()
    
    circle4 = plt.Circle((0.5, 0.5), 0.4, facecolor='None', edgecolor='green')
        
    ax.add_patch(circle4)
    
    plt.show()

circle4()




endTime = time.time()
elapsedTime = endTime - startTime
print("Elapsed Time = %s" % elapsedTime)
"""
print("Before the sleep statement")
time.sleep(5)
print("After the sleep statement")
"""