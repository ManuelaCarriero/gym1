# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 18:32:58 2022

@author: asus
"""

import numpy as np
import pylab as plt
import random as rn

def removal(state):
    return state*0.1

def increase(state):
    return 1

transitions = [removal, increase]
transitions_names = ['removal', 'increase']

state = 5

rates = [f(state) for f in transitions]
rates

total_rate = sum(rates)
total_rate

time = np.random.exponential(1/total_rate)
time

rn.choices(transitions_names, weights=rates)

event = rn.choices(transitions_names, weights=rates)[0]
print(event)

if event == 'increase':
    state += 1
elif event == 'removal':
    state -= 1
else:
    raise ValueError("transition not recognized")