# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 00:42:13 2014

@author: Siddhant
"""
from palindrome import *

Lychrel = [x for x in range(1,10001)]

maxIter = 50
for x in range(1,10001):
    c = 0
    s = x
    while c <= maxIter:
        s += int(reverse(s))
        if isPal(s):
            Lychrel.remove(x)
            break
        c += 1
        
print(len(Lychrel),Lychrel)
        