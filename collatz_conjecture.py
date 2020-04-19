# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 16:43:28 2020

@author: DELL
"""
def check_sum(num):
    i=1
    while(num!=1):
        if num%2==0:
            num = num/2
            i= i+1
        else:
            num= (num*3)+1
            i = i +1
            
            
    print(num,i)
n = int(input())
check_sum(n)
    