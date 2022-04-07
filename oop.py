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
