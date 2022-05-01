# -*- coding: utf-8 -*-
"""
Created on Sun May  1 17:05:24 2022

@author: asus
"""
import pandas as pd
df = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
                              'Parrot', 'Parrot'],
                   'Max Speed': [380., 370., 24., 26.]})

df.groupby(['Animal']).max()