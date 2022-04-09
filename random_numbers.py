# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 18:34:48 2022

@author: asus
"""

import random 

random.random()

[random.random() for i in range(3)]
#senza parentesi quadre ti dà invalid syntax perchè you have to
#store the generated random numbers in a list

random.seed(42)
[random.random() for i in range(3)]
#[0.6394267984578837, 0.025010755222666936, 0.27502931836911926]
random.seed(42)
[random.random() for i in range(3)]
#[0.6394267984578837, 0.025010755222666936, 0.27502931836911926]
random.seed(43)
[random.random() for i in range(3)]
#[0.038551839337380045, 0.6962243226370528, 0.14393322139536102]