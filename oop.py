# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 09:45:40 2022

@author: asus
"""
import pdir as dir

class Empty():
    """ This is an empty class. 
    It does nothing."""
    
#Let us define our instance

empty_instance = Empty()

help(empty_instance)

dir(empty_instance).public

isinstance(empty_instance,Empty)

#Attributes
namespace_0 = Empty()
namespace_0.a = 1
namespace_0.a

#Methods

class Something():
    a=2
    def multiply(self,b=3):
        return self.a*b

#Something.multiply(self, b=3) NameError: name 'self' is not defined

instance_of_Something = Something()

instance_of_Something.multiply(b=3) #bound

Something.multiply(instance_of_Something,b=3) #unbound

#__init__ method

class Something:
    def __init__(self,a):
        self.a = a

instance_mary = Something(a=3)
instance_mary.a

"""
OOP Exercise 1: Create a Class with instance attributes
Write a Python program to create a Vehicle class with max_speed 
and mileage instance attributes.
"""
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        
# This is an instance of Vehicle !
ModelX = Vehicle(max_speed = 200, mileage = 10) 

Vehicle.max_speed 
#AttributeError: type object 'Vehicle' has no attribute 'max_speed'

ModelX.max_speed 
#Se non metti il self ti dà lo stesso AttributeError precedente

"""Thus __init__ sets the attributes of the instances 
and not of the classes"""

