# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 16:32:22 2014

@author: Siddhant
"""
maxpower = 50
l = []
for power in range(1,maxpower + 1):
    for i in range(1,10):
        if len(str(i**power)) == power:
            l.append(i**power)

print(len(l),len(str(l[-1])))