# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 10:38:39 2023

@author: asus
"""

import matplotlib.pyplot as plt


def circle1():
    
    circle1 = plt.Circle((0.5, 0.5), 0.1, color='green')
    
    fig, ax1 = plt.subplots()
    
    ax1.add_patch(circle1)

circle1()

from itertools import cycle

import time

def progress(iterator):
    cycling = cycle("\|/")
    for element in iterator:
        print(next(cycling), end="\r")
        yield element
    print(" \r", end='')



for idx in progress(range(10)):
    time.sleep(0.5)

circle2 = plt.Circle((0.5, 0.5), 0.2, color='green')

fig, ax = plt.subplots()

ax.add_patch(circle2)



def progress(iterator):
    cycling = cycle("\|/")
    for element in iterator:
        print(next(cycling), end="\r")
        yield element
    print(" \r", end='')



for idx in progress(range(10)):
    time.sleep(0.5)


circle3 = plt.Circle((0.5, 0.5), 0.3, color='green')

fig, ax = plt.subplots()

ax.add_patch(circle3)

circle4 = plt.Circle((0.5, 0.5), 0.4, color='green')

fig, ax = plt.subplots()

ax.add_patch(circle4)