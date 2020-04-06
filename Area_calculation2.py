# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 14:37:12 2020

@author: DELL
"""

from PIL import Image
img = Image.open('AREA_img2.png')
rgb_i = img.convert('RGB')
r,g,b= rgb_i.getpixel((1,99))
print(r,g,b)
r,g,b= rgb_i.getpixel((100,99))
print(r,g,b)