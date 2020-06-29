# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:08:44 2020

@author: DELL
"""

n = input()
i = 0
j = 0
x=''
for k in n:
    if(k.isupper()==True):
        i=i+1
        x=x+k.lower()
    elif (k.islower()==True):
        j = j + 1
        x=x+k.upper()
        
print(i,j)
