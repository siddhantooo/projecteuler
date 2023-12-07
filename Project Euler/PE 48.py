# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 17:47:56 2014

@author: Siddhant
"""

#import numpy as np

s = 0
for i in range(1,1001):
    s += i**i
s = str(s)
print(s[-10:])