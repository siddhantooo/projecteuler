# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 19:06:17 2014

@author: Siddhant
"""
from time import time
from primesieve import soe
import math
start = time()
S = soe(math.ceil(math.sqrt(50000000)))
C = soe(math.ceil(math.pow(50000000,0.333333)))
Q = soe(math.ceil(math.pow(50000000,0.25)))

sq = {}
cu = {}
qu = {}
for i in S:
    sq[i] = i**2
for i in C:
    cu[i] = i**3
for i in Q:
    qu[i] = i**4
    
c = 0
memo = []
for i in sq:
    for j in cu:
        for k in qu:
            a = sq[i] + cu[j] + qu[k]
            if a <= 50000000:
                c += 1
                memo.append(a)

print(len(set(memo)))
print(time()-start,'seconds.')
