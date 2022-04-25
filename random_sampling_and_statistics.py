# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 17:34:48 2022

@author: asus
"""

import numpy as np
import pylab as plt
import scipy.stats as st
import seaborn as sns
import pandas as pd

import matplotlib.pylab as plt

data_1 = np.array([1.35, 1.01, 0.25, 0.39, -1.57])
st.ttest_1samp(data_1, 0)

mean_1 = np.mean(data_1)
std_1 = np.std(data_1, ddof=1)
print(mean_1, std_1, mean_1/(std_1/np.sqrt(len(data_1))))

np.mean(data_1)/st.sem(data_1)

def t_stat(data):
    return np.mean(data)/st.sem(data)

n_data = len(data_1)
data_fake_1 = plt.randn(n_data)
t_stat(data_fake_1)

distribution = [t_stat(plt.randn(n_data)) for i in range(100_000)]

fig, ax = plt.subplots()
# Distribution of statistics of random numbers normally distributed
ax.hist(distribution, bins=50, alpha=0.5, color='teal')
# Statistics of data_1 
ax.axvline(t_stat(data_1), color='coral')
ax.set_xlim(-5, 5)

# All this is done to answer to the question:
# Does this value really belong to a normal distribution ?
# p-value helps us to answer

# We can calculate the p-value by hand 
greater = np.abs(np.array(distribution))>abs(t_stat(data_1))

greater # binary array
sum(greater)
sum(np.array([False,True,True,True])) # It returns the number of true values

p_value = sum(greater)/len(greater)
print(p_value)

# We can calculate the p-value with the scipy stats already built function
st.ttest_1samp(data_1, 0)

# Correcting for "real" process
def gen_fake(n):
    fake_data = plt.randn(n)
    return fake_data.round(2)
gen_fake(5)

distribution = [t_stat(gen_fake(n_data)) for i in range(100_000)]

greater = np.abs(np.array(distribution))>abs(t_stat(data_1))
p_value = sum(greater)/len(greater)
print(p_value)

p_values = []
for i in range(8):
    distribution = [t_stat(gen_fake(n_data)) for i in range(1_000)]
    greater = np.abs(np.array(distribution))>abs(t_stat(data_1))
    p_value = sum(greater)/len(greater)
    print(p_value)
    p_values.append(p_value)

# You can plot to visualize better the uniform distribution (as in statistics)

df = pd.DataFrame({"X": np.arange(1,len(p_values)+1) , "Y": p_values})

len(np.arange(1,len(p_values)+1))
len(p_values)

f, (ax_hist, ax_bar) = plt.subplots(2)
sns.histplot(data=df, x="X", ax=ax_hist, stat="density", alpha=0.4, kde=True, kde_kws={"cut": 3})
ax_hist.set_title("new histplot")

ax_bar.bar(df["X"], df["Y"])
ax_bar.set_title("bar plot")
plt.show()



