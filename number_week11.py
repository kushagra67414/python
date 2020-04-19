# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 17:18:14 2020

@author: DELL
"""

m,n = input().split(',')
m = int(m)
n = int(n)

values = []
for i in range(m, n+1):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))