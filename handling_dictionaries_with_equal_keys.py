# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 10:37:24 2022

@author: asus
"""

import matplotlib.pylab as plt 

dictionary = {'Dog': 4, 'Dog': 5, 'Elephant': 10}
dictionary.keys()

fig, ax = plt.subplots()

ax.bar(dictionary.keys(),dictionary.values())

plt.show()

#Dictionary gives problem when you use keys with the same name
##################################################################
# so in this case a would do:
class DictList(dict):
    def __setitem__(self, key, value):
        try:
            # Assumes there is a list on the key
            self[key].append(value)
        except KeyError: # If it fails, because there is no key
            super(DictList, self).__setitem__(key, value)
        except AttributeError: # If it fails because it is not a list
            super(DictList, self).__setitem__(key, [self[key], value])
            
my_dict = {1: 'a', 2: 'b', 3: 'b'}
my_dict = { 2: 'b', 3: 'b'}
my_dict = {'Dog': 4, 'Dog': 5, 'Elephant': 10}
rev = DictList()
for k, v in my_dict.items():
    rev[v] = k
rev # {'a': 1, 'b': [2, 3]}
rev.values()
#######################################################
fig, ax = plt.subplots()

ax.bar(rev.keys(),rev.values())

plt.show() #ValueError: setting an array element with a sequence.
#########################################################
dictionary_new = {}
for k,v in rev.items():
    if type(v) == list:
        dictionary_new[k] = sum(v)
    else:
        dictionary_new[k] = v
dictionary_new   

fig, ax = plt.subplots()

ax.bar(dictionary_new.values(), dictionary_new.keys())

plt.show()