# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 16:58:51 2020

@author: DELL
"""

import scipy.misc
from PIL import Image
import numpy as np
import random
img= scipy.misc.imread("map.png")
count_pun = 0
count_in = 0
count = 0
while (count <= 100000):
    x= random.randint(0,279)
    y= random.randint(0,241)
    z= 0
    if(img[x][y][z]==222)   :
        count_in =count_in +1
        count = count+1
        
    else:
        if(img[x][y][z]==205):
            count_pun = count_pun+ 1 
            count = count+1
            
            
area_pun = (count_pun/count_in)*3287263
print(area_pun)