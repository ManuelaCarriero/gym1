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

namespace_0 = Empty()
namespace_0.a = 1
namespace_0.a
