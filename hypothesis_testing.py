# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 14:59:00 2023

@author: asus
"""
#Lesson Professor Exercise

def _convert(k):
    if isinstance(k, str):
        return k.lower()
    else:
        return k

def getitem(mapping,key,transform=_convert):
    key = transform(key)
    for map_key in mapping.keys():
        transformed_key = transform(map_key)
        if key == transformed_key:
            return mapping[map_key]
    raise KeyError("key {} not in mapping".format(key))
    
#def getitem(mapping,key):
#    return mapping[key]

#%%Tests

#Informal tests

d = {'a':1,'b':2}
assert getitem(d,'a') == 1
assert getitem(d,'b') == 2

# Unit testing

def test_return_correct_value():
    d = {'a':1,'b':2}
    assert getitem(d,'a') == 1
    
#