# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 15:18:48 2022

@author: asus
"""

#Exercise 1: Print First 10 natural numbers using while loop        
i=0 
"""
you have to set the starting value, 
otherwise when running it again it will start 
from the last value of the iteration
"""
# condition: Run loop till count is less than 10
while i < 10:
    print(i+1)
    i = i + 1

#Now let us store into a function

def numbers_printer(n):
    """This function prints the first n numbers"""
    i=0
    while i < n:
        print(i+1)
        i=i+1

numbers_printer(10)
