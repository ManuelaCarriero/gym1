# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 12:19:42 2022

@author: asus
"""

#Exercise convert strings into numbers in a numpy array

import numpy as np

"""First version simply converts into numbers without assigning 
a precise number to a string"""

letters_list = ['A','B','C']
letters_array = np.array(letters_list)
letters_array
print(letters_array)
counter = len(letters_array)

#linspace takes the initial value, final value and the number of steps
numbers_array = np.linspace(1,counter,counter)
numbers_array
numbers_array.dtype # Now it is dtype('float64')

numbers_array=numbers_array.astype(np.int32) # It converts to dtype=int32 
numbers_array  

"""Second version converts strings into numbers by assigning 
a precise number to a string"""

letters_list = ['A','B','C','A']
letters_array = np.array(letters_list)

numbers_list = []
for i in letters_array:
    if i == 'A':
        numbers_list.append(1)
    elif i == 'B':
        numbers_list.append(2)
    else:
        numbers_list.append(3)

numbers_array = np.array(numbers_list, dtype=np.int32)
numbers_array
numbers_array.dtype

def array_type_converter(letters_array):
    """function that converts a numpy array of strings A B C 
    into a numpy array of corresponding numbers""" 
    numbers_list = []
    for i in letters_array:
        if i == 'A':
            numbers_list.append(1)
        elif i == 'B':
            numbers_list.append(2)
        else:
            numbers_list.append(3)

    numbers_array = np.array(numbers_list, dtype=np.int32)
    return numbers_array

# Testing the function 
letters_list = ["A","B","C","A"]
example = np.array(letters_list)
example
array_type_converter(example)
array_type_converter(np.array(["A","B","C","A"]))

"""Fourth version with all the letters of alphabet"""

import string
letters_list = list(string.ascii_uppercase)
array_of_letters = np.array(letters_list)

length_array = len(array_of_letters)
length_array 
numbers = np.linspace(1, length_array, length_array)
indices = np.linspace(0, length_array, length_array) #sistema !
indices

numbers_list = []
for i, j in zip(array_of_letters,numbers):
    for k in indices:
        if i == letters_list[k]:
            numbers_list.append(j)
    i = i+1
            
            
