# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 14:44:56 2022

@author: asus
"""

MyStr2 = "I am poor"
MyList = MyStr2.split(" ") # a list object
MyList
myStr_new = ''
for word in MyList:
    if word == "poor":
        myStr_new += "Good"
    else:
        myStr_new +=word

print(myStr_new)

MyStr2 = "I am poor"
MyLis = MyStr2.split(" ")

for i in range(len(MyLis)):
    if MyLis[i] == "poor":
        MyLis[i] = "Good"



a = " ".join(MyLis)
print(a)

MyStr2 = "I am poor"
MyStr2_new = ' '.join("Good" if word == 'poor' else word for word in MyStr2.split(' '))

print(MyStr2_new)

#+Others