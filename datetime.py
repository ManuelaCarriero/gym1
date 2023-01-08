# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 08:50:52 2022

@author: asus
"""

import datetime

start = datetime.datetime.now()

list1 = [4, 2, 3, 1, 5]
list1.sort()

end = datetime.datetime.now()
print(end-start)

now = datetime.datetime.now()

now = "%0.2d:%0.2d:%0.2d" % (now.hour, now.minute, now.second)
#
start = datetime.datetime.now()

start = "%0.2d:%0.2d:%0.2d" % (now.hour, now.minute, now.second)

list1 = [4, 2, 3, 1, 5]
list1.sort()

end = datetime.datetime.now()

end = "%0.2d:%0.2d:%0.2d" % (now.hour, now.minute, now.second)

print(start-end)

#
#import ast
now=datetime.datetime.now()
string_i_want=('%02d:%02d.%d'%(now.minute,now.second,now.microsecond))[-4]#'02:53.34'
string_i_want=('%02d:%02d.%d'%(now.minute,now.second,now.microsecond))#'02:53.343892'
string_i_want=('%02d:%02d:%0.2d'% (now.hour, now.minute, now.second))
string_i_want
time = datetime.datetime.strptime(string_i_want, '%H:%M:%S').time()
print(time)

list1 = [4, 2, 3, 1, 5]
list1.sort()

string_i_want_now=('%02d:%02d:%0.2d'% (now.hour, now.minute, now.second))
time_now = datetime.datetime.strptime(string_i_want, '%H:%M:%S').time()
print(time-time_now)

#
import datetime
import time

# get the start datetime
st = datetime.datetime.now()

# main program
# find sum to first 1 million numbers
sum_x = 0
for i in range(1000000):
    sum_x += i

# wait for 3 seconds
time.sleep(3)
print('Sum of first 1 million numbers is:', sum_x)

# get the end datetime
et = datetime.datetime.now()

# get execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')