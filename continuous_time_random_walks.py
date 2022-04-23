# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 18:32:58 2022

@author: asus
"""

import numpy as np
import pylab as plt
import random as rn
import pandas as pd

import typing
from enum import Enum

import scipy.stats as st

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
result
observation.state
for observation in result:
    print(observation.state)

len(result)

for res in result[-5:]:
    print(res)

##########################TRYING TO UNDERSTAND THE FOLLOWING PIECE OF CODE#######
data = pd.read_csv("fruits.txt", sep = " ")
data

from collections import Counter

counts = Counter(data.ID)
counts #It works

counts = Counter()
counts[data.ID] #It does not work
for ID in data.ID:
    counts[data.ID] += Counter(data.ID) #TypeError: unhashable type: 'Series'
print(counts)

lst = ['Mary', 'Mary', 'Mary', 'Mary','Dog']
counts = Counter(lst)
counts

counts = Counter()
for item in lst:
    counts[lst] += Counter(lst)#TypeError: unhashable type: 'list'

for item in lst:
    counts[lst] += Counter(lst).values()
print(counts)

counts[lst] #it does not work

counts = Counter()
for observation in result:
   counts[observation.state]

print(counts) #printa tutti 0
    
#CONCLUSION: IT IS SOMETHING THAT WORKS WIH NAMEDTUPLES CLASS

distribution = Counter()
for observation in result:
    state = observation.state
    residency_time = observation.time_of_residency
    distribution[state] += 1
print(distribution)
#############################

distribution = Counter()
for observation in result:
    state = observation.state
    residency_time = observation.time_of_residency
    distribution[state] += residency_time/time_limit
print(distribution)

fig, ax = plt.subplots()
ax.bar(distribution.keys(), distribution.values())
#xlim = [5,12.5]

values = np.arange(20)
pmf = st.poisson(10).pmf(values)
ax.bar(values, pmf, alpha=0.5)

def generate_distribution(observation_sequence):
    distribution = Counter()
    for observation in observation_sequence:
        state = observation.state
        residency_time = observation.time_of_residency
        distribution[state] += residency_time
        
    total_time_observed = sum(distribution.values())
    for state in distribution:
        distribution[state] /= total_time_observed
    return distribution

time_limit = 1_000
result = simulation(starting_state=5, time_limit=time_limit)
distribution = generate_distribution(result)

fig, ax = plt.subplots()
ax.bar(distribution.keys(), distribution.values())

values = np.arange(20)
pmf = st.poisson(10).pmf(values)
ax.bar(values, pmf, alpha=0.5)

#Add the following steps of the slides, in particular plot
#the probability distribution in case of absorbing states 
#and fixed time events
#moreover do the final exercise.