# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 14:44:32 2022

@author: asus
"""
import re
import pandas as pd
import numpy as np
from itertools import islice


def read_file(file_name,columns):
    with open("proof.txt") as txt_file:
        records = []
        for line in txt_file:
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
    for line in txt_file:
        record=[]
        line.split(",")
        splits = re.findall(r"[\w']+", line)
        for i in np.arange(0,9):
            record.append(splits[i])
        records.append(record)
records
        
data = pd.DataFrame(records, columns= ['id','text','created_at','author.id','author.public_metrics.tweet_count','author.public_metrics.following_count','author.public_metrics.followers_count','public_metrics.like_count','public_metrics.retweet_count'])       
data

