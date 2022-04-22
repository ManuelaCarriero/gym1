# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 14:44:32 2022

@author: asus
"""
import re
import pandas as pd
import numpy as np
from itertools import islice
import matplotlib.pylab as plt
import matplotlib.dates as mdates

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

##########################################################
df = pd.read_csv('tweets_data.txt')
df['created_at']
df
df.columns

df['created_at'] = pd.to_datetime(df['created_at'])
df['created_at']
df['created_at'] = df['created_at'].dt.date
df['created_at']

histogram_data = pd.concat([df[['created_at']],df[['public_metrics.like_count']]],axis=1)
January_values = histogram_data[histogram_data['created_at'].astype(str).str.contains('2018-01')]
January_values

histogram_data
df[['public_metrics.like_count']]
histogram_data.columns
histogram_data.created_at
histogram_data

dictionary = {}

for date, n_likes in histogram_data.itertuples(index=False):
    dictionary[date] = n_likes

print(dictionary)

fig, ax = plt.subplots()
ax.tick_params(axis='x', which='major', labelsize=8, width=2)
ax.bar(dictionary.keys(),dictionary.values()) # Horrible
plt.setp( ax.xaxis.get_majorticklabels(), rotation=-45, ha="left" )


###############Dirty#################################
df = pd.read_csv('tweets_data.txt')

#df['created_at'] = pd.to_datetime(df['created_at'].str.split('T', n=1).str[0])
#df
#df['created_at'] = pd.to_datetime(df['created_at'])

#df['created_at'] = df['created_at'].dt.date
df['created_at'] = df['created_at'].str.replace(".000Z", "")
df.created_at
histogram_data = pd.concat([df[['created_at']],df[['public_metrics.like_count']]],axis=1)
January_values = histogram_data[histogram_data['created_at'].astype(str).str.contains('2018-01')] #histogram_data['created_at'].astype(str)
January_values
type(January_values)
January_values.shape


dictionary = {}

for date, n_likes in January_values.itertuples(index=False):
    dictionary[date] = n_likes

print(dictionary)
len(dictionary)

fig, ax = plt.subplots()
ax.tick_params(axis='x', which='major', labelsize=4, width=2)
ax.bar(dictionary.keys(),dictionary.values())
ax.set_ylabel("Counts")
ax.set_title("Tweets likes counts in January 2018")
ax.xaxis.set_tick_params(labelsize=4, rotation = 90)

plt.setp( ax.xaxis.get_majorticklabels(), rotation=-45, ha="left", weight="bold")







# Create figure and plot space
fig, ax = plt.subplots(figsize=(12, 12))

# Add x-axis and y-axis
ax.bar(dictionary.keys(),
       dictionary.values(),
       color='purple')

# Set title and labels for axes
ax.set_xlabel('Date', fontsize = 20)
ax.set_ylabel('Counts', fontsize = 20)
ax.set_title('Tweets likes counts in January 2018', fontsize = 15, weight = "bold")


#Define the date format


# Ensure a major tick for each week using (interval=1) 
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.tick_params(axis='x', which='major', labelsize=15, width=2)
plt.setp( ax.xaxis.get_majorticklabels(), rotation=-45, ha="left", weight="bold")

plt.show()



######################My nicer version happy########################
df = pd.read_csv('tweets_data.txt')
df['created_at'] = df['created_at'].str.replace(".000Z", "")
df.created_at

histogram_data = pd.concat([df[['created_at']],df[['public_metrics.like_count']]],axis=1)
January_values = histogram_data[histogram_data['created_at'].astype(str).str.contains('2018-01')] #histogram_data['created_at'].astype(str)
January_values
January_values.shape


dictionary = {}
for date, n_likes in January_values.itertuples(index=False):
    dictionary[date] = n_likes
print(dictionary)


# Create figure and plot space
fig, ax = plt.subplots(figsize=(12, 12))

# Add x-axis and y-axis
ax.bar(dictionary.keys(),
       dictionary.values(),
       color='purple')

# Set title and labels for axes
ax.set_xlabel('Date', fontsize = 20)
ax.set_ylabel('Counts', fontsize = 20)
ax.set_title('Tweets likes counts in January 2018', fontsize = 15, weight = "bold")

# Ensure a major tick for each week using (interval=1) 
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.tick_params(axis='x', which='major', labelsize=15, width=2)
plt.setp( ax.xaxis.get_majorticklabels(), rotation=-45, ha="left", weight="bold")

plt.show()








# How to remove a substring from a string


a_string = "programming"
new_string = a_string. replace("ing", "")
print(new_string)



# SE User Solution

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
