# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 15:20:27 2023

@author: asus
"""

from hypothesis_testing import getitem
import pytest
import hypothesis
from hypothesis import given
import hypothesis.strategies as st


#%%Tests

#Informal tests

d = {'a':1,'b':2}
assert getitem(d,'a') == 1
assert getitem(d,'b') == 2

# Unit testing

def test_return_correct_value():
    d = {'a':1,'b':2}
    assert getitem(d,'a') == 1
    
# Property based testing

def test_invariance_by_case():
    data = {'a':1,'b':2}
    key = 'b'
    expected = 2
    assert getitem(data,key) == expected
    assert getitem(data,key.lower()) == expected
    assert getitem(data,key.upper()) == expected
    assert getitem(data,key.title()) == expected
    
def test_invariance_by_case_evoluted():
    expected = 2
    key = 'hEllo'
    
    transforms = [str.lower,str.upper,str.title]
    
    for transf_map in transforms:
        data = {transf_map(key): expected}
        for transf_key in transforms:
            assert getitem(data, transf_key(key)) == expected
"""
expected = 2
key = 'hEllo'

transforms = [str.lower,str.upper,str.title]

for transf_map in transforms:
    data = {transf_map(key): expected}
    for transf_key in transforms:
        assert getitem(data, transf_key(key))
"""
#gli passa tanti valori random grazie a strategies
@given(key=st.just("hEllo"), value=st.floats())
def test_invariance_by_case_property_based_testing(key,value):
    transforms = [ str.lower,str.upper,str.title]
    
    for transf_map in transforms:
        data = {transf_map(key): value}
        for transf_key in transforms:
            assert getitem(data, transf_key(key)) == value
#it runs for random values and it fails with nan
#so the function has to be adjusted for this case

@given(key=st.integers(), value=st.integers())
def test_string_and_int_mix(key,value):
    data = {key:value}
    assert getitem(data,key) == value
    
    with pytest.raises(KeyError):
        getitem(data,str(key))
        
    data = {str(key): value}
    with pytest.raises(KeyError):
        getitem(data,key)
           
