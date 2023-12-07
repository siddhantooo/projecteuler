# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 19:58:30 2014

@author: Siddhant
"""
import numpy as np
def isPal(n):
    n = str(n)
    k = int(len(n)/2)
    for i in range(0,k+1):
        if n[i] != n[-(i+1)]:
            return False
    return True
pals = []    
for i in range(1,1000001):
    if isPal(i) and isPal(np.binary_repr(i)):    
        pals.append(i)
print(len(pals),pals,sum(pals))