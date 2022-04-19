# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 14:44:32 2022

@author: asus
"""
import re
import pandas as pd
import numpy as np
from itertools import islice
import matplotlib as plt


def read_file(file_name,columns):
    with open("proof.txt") as txt_file:
        records = []
        skipped = islice(txt_file, 1, None)
        for number, line in enumerate(skipped,2):
            record = []
            line.split(",")
            splits = re.findall(r"[\w']+", line)
            for i in np.arange(0,9):
                record.append(splits[i])
            records.append(record)
    return pd.DataFrame(records, columns=columns)

data = read_file("proof.txt", columns=['id','text','created_at','author.id','author.public_metrics.tweet_count','author.public_metrics.following_count','author.public_metrics.followers_count','public_metrics.like_count','public_metrics.retweet_count'])
data






with open("proof.txt") as txt_file:
    records=[]
    skipped = islice(txt_file, 0, None)
    for number, line in enumerate(skipped,1):
        record=[]
        line.split(",")
        splits = re.findall(r"[\w']+", line)
        for i in np.arange(0,9):
            record.append(splits[i])
        records.append(record)
records
        
data = pd.DataFrame(records, columns= ['id','text','created_at','author.id','author.public_metrics.tweet_count','author.public_metrics.following_count','author.public_metrics.followers_count','public_metrics.like_count','public_metrics.retweet_count'])       
data

df = pd.read_csv('tweets_data.txt')
df['created_at']
df
df.text[0]

# convert text column to date time and keep only the date part  
df['created_at'] = pd.to_datetime(df['created_at'])
df['created_at']
df['created_at'] = df['created_at'].dt.date
df['created_at']

# group by date taking the sum of public_metrics.like_count
df1 = df.groupby(['created_at'])['public_metrics.like_count'].sum().reset_index()
df1 = df1.set_index('created_at')

# plot and show
df1.plot()
plt.show()
