# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 18:32:58 2022

@author: asus
"""

import numpy as np
import pylab as plt
import random as rn

import typing
from enum import Enum

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

#Using class is a nicer way to represent our event instead of tuples, lists etc...

class Transition(Enum):
    INCREASE = 'increase'
    DECREASE = 'removal'

class Observation(typing.NamedTuple):
    state: typing.Any
    time_of_observation: float
    time_of_residency: float
    transition: Transition
    
Observation(5, 1.0, 0.33, Transition.DECREASE)

transitions = [removal, increase]
transitions_names = [Transition.DECREASE, Transition.INCREASE]

#All together
observed_states = []
state = 5
total_time = 0.0
time_limit = 5.0

while total_time < time_limit:
    rates = [f(state) for f in transitions]
    total_rate = sum(rates)
    time = np.random.exponential(1/total_rate)
    event = rn.choices(transitions_names, weights=rates)[0]
    
    observation = Observation(state, total_time, time, event)
    print(observation)
    observed_states.append(observation)
    
    total_time += time
    
    if event == Transition.INCREASE:
        state += 1
    elif event == Transition.DECREASE:
        state -= 1
    else:
        raise ValueError("transition not recognized")
        
#Nicely chunking everything in a function
        
def simulation(starting_state, time_limit):
    observed_states = []
    state = starting_state
    total_time = 0.0

    while total_time < time_limit:
        rates = [f(state) for f in transitions]
        total_rate = sum(rates)
        time = np.random.exponential(1/total_rate)
        event = rn.choices(transitions_names, weights=rates)[0]

        observation = Observation(state, total_time, time, event)
        observed_states.append(observation)

        total_time += time

        if event == Transition.INCREASE:
            state += 1
        elif event == Transition.DECREASE:
            state -= 1
        else:
            raise ValueError("transition not recognized")
    return observed_states
        
time_limit = 100
result = simulation(starting_state=5, time_limit=time_limit)

len(result)

for res in result[-5:]:
    print(res)