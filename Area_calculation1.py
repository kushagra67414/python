# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 13:50:15 2020

@author: DELL
"""
import numpy as np
from PIL import Image
w = 5
h = 5
array= np.zeros([w,h,3] , dtype = np.uint8)
img = Image.fromarray(array)
img.save('AREA_img1.png')
array1= np.zeros([100,200,3] , dtype = np.uint8)
array1[: ,:100 ] =  [255,128,0]  #orange
array1[: ,100: ] = [0,0,255]    #blue
img = Image.fromarray(array1)
img.save('AREA_img2.png')