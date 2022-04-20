# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 10:58:09 2022

@author: asus
"""

import pandas as pd
import numpy as np

data = pd.read_csv("fruits.txt",sep=" ")
data
data.columns

data.iloc[:,[0]]
data["ID"]



