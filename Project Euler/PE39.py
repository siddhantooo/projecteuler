# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 02:46:51 2014

@author: Siddhant
"""
from time import time
from math import *
start = time()

pytha = []
sq = {}
for i in range(1,500):
    sq[i] = (i**2)
sums={}
for i in range(10,1001):
    sums[i] = 0
for a in range(2,498):
    for b in range(a,499):
        c = sqrt(sq[a] + sq[b])
        if a + b + c <= 1000:
            if ceil(c-0.00000001) != ceil(c+0.00000001):    
                if c < a + b:
    #                print(a,b,c,a+b+c,sq[a],sq[b])
                    pytha.append([a,b,c])
                    
                    sums[a+b+c] += 1

k = max(sums.values())
for i in sums:
    if sums[i] == k:
        print(i)
print(time()-start,'seconds.')
