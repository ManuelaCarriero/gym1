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
len(data.columns)
np.arange(1,len(data.columns))

data.iloc[:,[0]]
data["ID"]

#It gives you a dataframe with only the selected rows.
data_ID101 = data[data["ID"].isin([101])]
data_ID101

unique_classes = data.ID.unique()
unique_classes

#You can iterate over isin.
for i in unique_classes:
    print(data[data["ID"].isin([i])])
    
#Iterate over dataframe.
for index, row in data_ID101.iterrows():
    #print(row['field1'])
    print(row[0])

for index, row in data_ID101.iterrows():
    print(row[1], row[2], row[3])
    