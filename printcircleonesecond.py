# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 10:38:39 2023

@author: asus
"""

import matplotlib.pyplot as plt
#from itertools import cycle
import time
#import numpy as np
import argparse
import configparser
"""
config = configparser.ConfigParser()



parser = argparse.ArgumentParser()



parser.add_argument("-run", help="Circles that increase and decrease to modulate your diaphragmatic breathing.", action = "store_true")

args = parser.parse_args()

if args.run:
"""
# initialization
count = 1

# exit limit
n = 2

# count is always in this limit so the user stops the program when he wants.
while count in range(0,10):
    #Inspirazione 
    startTime = time.time()
    
    def circle1():
        
        fig, ax = plt.subplots()
        
        circle1 = plt.Circle((0.5, 0.5), 0.1, facecolor='None', edgecolor='green')
            
        ax.add_patch(circle1)
        
        ax.set_facecolor('lightgreen')
        
        fig.patch.set_facecolor('lightgreen')
        
        plt.axis('off')
        
        plt.show()
    
    circle1()
    
    time.sleep(1.1)
    
    def circle2():
        
        fig, ax = plt.subplots()
        
        circle2 = plt.Circle((0.5, 0.5), 0.2, facecolor='None', edgecolor='green')
            
        ax.add_patch(circle2)
    
        ax.set_facecolor('lightgreen')
        
        fig.patch.set_facecolor('lightgreen')
        
        plt.axis('off')
        
        plt.show()
    
    circle2()
    
    time.sleep(1.1)
    
    def circle3():
        
        fig, ax = plt.subplots()
        
        circle3 = plt.Circle((0.5, 0.5), 0.3, facecolor='None', edgecolor='green')
        
        ax.set_facecolor('lightgreen')
            
        ax.add_patch(circle3)
        
        fig.patch.set_facecolor('lightgreen')
        
        plt.axis('off')
        
        plt.show()
    
    circle3()
    
    time.sleep(1.1)
    
    
    
    
    def circle4():
        
        fig, ax = plt.subplots()
        
        circle4 = plt.Circle((0.5, 0.5), 0.4, facecolor='None', edgecolor='green')
        
        ax.set_facecolor('lightgreen')
            
        ax.add_patch(circle4)
        
        fig.patch.set_facecolor('lightgreen')
        
        plt.axis('off')
        
        plt.show()
    
    circle4()
    
    # metti le linee di comando così puoi visualizzare il cerchio che si apre e si chiude più grande
    # 4 secondi inspirazione
    # trattieni per circa un paio di secondi l'aria
    # 6 secondi di espirazione
    
    
    
    
    endTime = time.time()
    elapsedTime = endTime - startTime
    print("Elapsed Time Inspiration = %s" % elapsedTime)
    
       
    
    startTime = time.time()
    
    time.sleep(2.1)
    
    endTime = time.time()
    elapsedTime = endTime - startTime
    print("Elapsed Time holding your breath = %s" % elapsedTime)
    
    #Espirazione
    
    startTime = time.time()
    
    
    
    def circle6():
        
        fig, ax = plt.subplots()
        
        circle = plt.Circle((0.5, 0.5), 0.4, facecolor='None', edgecolor='green')
        
        ax.set_facecolor('lightgreen')
            
        ax.add_patch(circle)
        
        fig.patch.set_facecolor('lightgreen')
        
        plt.axis('off')
        
        plt.show()
    
    circle6()
    
    time.sleep(1.1)
    
    def circle5():
        
        fig, ax = plt.subplots()
        
        circle = plt.Circle((0.5, 0.5), 0.3, facecolor='None', edgecolor='green')
        
        ax.set_facecolor('lightgreen')
            
        ax.add_patch(circle)
        
        fig.patch.set_facecolor('lightgreen')
        
        plt.axis('off')
        
        plt.show()
    
    circle5()
    
    time.sleep(1.1)
    
    def circle4():
        
        fig, ax = plt.subplots()
        
        circle = plt.Circle((0.5, 0.5), 0.2, facecolor='None', edgecolor='green')
        
        ax.set_facecolor('lightgreen')
            
        ax.add_patch(circle)
        
        fig.patch.set_facecolor('lightgreen')
        
        plt.axis('off')
        
        plt.show()
    
    circle4()
    
    time.sleep(1.1)
    
    def circle3():
        
        fig, ax = plt.subplots()
        
        circle = plt.Circle((0.5, 0.5), 0.1, facecolor='None', edgecolor='green')
        
        ax.set_facecolor('lightgreen')
            
        ax.add_patch(circle)
        
        fig.patch.set_facecolor('lightgreen')
        
        plt.axis('off')
        
        plt.show()
    
    circle3()
    
    time.sleep(1.1)
    
    def circle2():
        
        fig, ax = plt.subplots()
        
        circle = plt.Circle((0.5, 0.5), 0.05, facecolor='None', edgecolor='green')
        
        ax.set_facecolor('lightgreen')
            
        ax.add_patch(circle)
        
        fig.patch.set_facecolor('lightgreen')
        
        plt.axis('off')
        
        plt.show()
    
    circle2()
    
    time.sleep(1.1)
    
    def circle1():
        
        fig, ax = plt.subplots()
        
        circle = plt.Circle((0.5, 0.5), 0.025, facecolor='None', edgecolor='green')
        
        ax.set_facecolor('lightgreen')
            
        ax.add_patch(circle)
        
        fig.patch.set_facecolor('lightgreen')
        
        plt.axis('off')
        
        plt.show()
    
    circle1()
    
    time.sleep(2.1)
    
    endTime = time.time()
    elapsedTime = endTime - startTime
    print("Elapsed Time Exhale = %s" % elapsedTime)


#%%############################################        
import numpy as np    
        
theta = np.linspace(0, 10*np.pi, 50)
r= 1
x = r*np.cos(theta)
y = r*np.sin(theta)
plt.figure(figsize=(10,10))
plt.plot(x,y, color='green')
plt.xlim(-10,10)

time.sleep(1.1)

theta = np.linspace(0, 10*np.pi, 50)
r= 2
x = r*np.cos(theta)
y = r*np.sin(theta)
plt.figure(figsize=(10,10))
plt.plot(x,y, color='green')
plt.xlim(-10,10)

time.sleep(1.1)

theta = np.linspace(0, 10*np.pi, 50)
r= 3
x = r*np.cos(theta)
y = r*np.sin(theta)
plt.figure(figsize=(10,10))
plt.plot(x,y, color='green')
plt.xlim(-10,10)

time.sleep(1.1)

theta = np.linspace(0, 10*np.pi, 50)
r= 4
x = r*np.cos(theta)
y = r*np.sin(theta)
plt.figure(figsize=(10,10))
plt.plot(x,y, color='green')
plt.xlim(-10,10)

time.sleep(1.1)

