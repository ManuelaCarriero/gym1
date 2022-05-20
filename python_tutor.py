# -*- coding: utf-8 -*-
"""
Created on Thu May 19 18:34:42 2022

@author: asus
"""

events = [1,0,1,0]
state = [0,0]
states = []
for i in events:
    states.append(state)
    state = state[:]
    
    if i > 0:
        state[0] +=1
        state = state[:]
    else:
        state[0] -=1
        state = state[:]

# What you desire is the following results:

events = [1,0,1,0]
state = [0,0]
states = []
state = state[:]
states.append(state)
for i in events:

    
    if i > 0:
        state = state[:]
        state[0] +=1
        
    else:
        state = state[:]
        state[0] -=1
        
    
    states.append(state)
