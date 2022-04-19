# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 13:37:04 2022

@author: asus
"""
#Import pandas module
import pandas as pd

#Lists of data 
list_A = [1,2,3,4,5]
list_B = [2,4,3,3,2]

#Define a dictionary containing lists of data
dictionary = {'A':  list_A,
        'B': list_B}

#Convert the dictionary into DataFrame
data = pd.DataFrame(dictionary)
data

#New list
data_diff = data.A - data.B 

new_list=[]
for i in data_diff:
    if i > 0:
        new_list.append(i*5)
    else:
        new_list.append(0)

#New dataframe
new_dictionary = {'A':  [1,2,3,4,5],
        'B': [2,4,3,3,2],
        'C': new_list}

new_data=pd.DataFrame(new_dictionary)
new_data

#SEUser1
numbers = {'A': [1,2,3,4,5], "B":[2,4,3,3,2]}
df = pd.DataFrame(numbers)
df

c = []

for lab, row in df.iterrows():
    curr = 0
    if row['A'] > row['B']:
        curr = row['B'] * 5

    c.append(curr)

df['C'] = c #you can create a new coloumn just like in this way
df

#SEUser2
df["C"] = df.A - df.B

# First turns negative values into 0s
df["C"].mask(df["C"] <= 0, 0, inplace=True)

# Then divides everything by 2. The 0s will still remain 0.
df["C"] = df["C"] * 0.5

df

#SEUser3
import numpy as np
df["C"] = np.where(df["A"] > df["B"], df["B"]*5, 0)
df

# New exercise
data={'column1': [1,3],'column2': [1,4]}

dataframe = pd.DataFrame(data)
dataframe

# Fill a new column with values equal to the maximum value in column 1 
new_column = []
for i in dataframe.column1:
    new_column.append(max(dataframe.column1))


dataframe['column3'] = new_column

dataframe

#How to build a dataframe by inserting lists or numpy arrays
low_value_cluster_20_h = np.array([[10.000000,0.240619]])
low_value_cluster_20_h
low_value_cluster_20_h = [[10.000000,0.240619]]
#low_value_cluster_20_h = [10.000000,0.240619] If you put it, you obtain:
#ValueError: Shape of passed values is (2, 1), indices imply (2, 2)
low_value_cluster_20_h = pd.DataFrame(low_value_cluster_20_h, columns = ['N dias Treino', 'RMSE'])
low_value_cluster_20_h

######################################################################

Dat = pd.DataFrame({'product_name': ['laptop', 'printer', 'printer',], 'price': [1200, 150, 1200],  'price1': [1200, 150, 1200]})
Dat1 = pd.DataFrame({'product_name': ['laptop', 'printer', 'laptop', 'printer'], 'price2': [200, 150, 200, 999]})
pd.merge(Dat, Dat1, on = 'product_name')

#Apply merge method on pandas dataframes using chain rule
Dat.merge(Dat1, on = 'product_name')
