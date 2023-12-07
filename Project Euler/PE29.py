# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 05:04:01 2014

@author: Siddhant
"""
l = []
for a in range(2,101):
    for b in range(2,101):
        s = a**b
        l.append(s)
l=list(set(l))
print(len(l))