# -*- coding: utf-8 -*-
"""
Created on Mon May 16 15:12:58 2022

@author: asus
"""

import random 

random.seed(1)

[random.random() for i in range(3)]

random.seed(1)

[random.random() for i in range(3)]

lst = [1,2,3,4]
weights = [1,4,5,8]

event = random.choices(lst, weights = weights)[0]
event 

random.seed(1)
event = random.choices(lst, weights = weights)[0]
event

random.seed(1)
event = random.choices(lst, weights = weights)[0]
event

event = random.choices(lst, weights = weights)[0]
event

time = 0
while time < 10:
    time +=1
    random.seed(1)
    event = random.choices(lst, weights = weights)[0]
    print(event)

random.seed(1)  
time = 0
while time < 5:
    time +=1
    event = random.choices(lst, weights = weights)[0]
    print(event)

random.seed(1)  
time = 0
while time < 5:
    time +=1
    event = random.choices(lst, weights = weights)[0]
    print(event)
        