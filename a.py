# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 17:38:17 2020

@author: DELL
"""

from PIL import Image
import random
im = Image.open("map.png")
rgb_i = im.convert('RGB')
count_pun = 0
count_in = 0
count = 0
while (count <= 100000):
    x= random.randint(0,279)
    y= random.randint(0,241)
    z= 0
    r,g,b = rgb_i.getpixel((x,y))
    if(r==60)   :
        count_in =count_in +1
        count = count+1
        
    else:
        if(r==80):
            count_pun = count_pun+ 1 
            count = count+1