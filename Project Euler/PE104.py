# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 17:21:41 2014

@author: Siddhant
"""
import numpy as np
import time
import math

def f(n):
    n = str(n)
    return set(n) == set('123456789')

#print(math.ceil(np.log10(3)))

def g(n):
    l = math.ceil(math.log10(n))
    x = int(n/(10**(l-9)))
    return f(x)   

#print(g(1234516789364619),isPandig(987654321))

start = time.time()    
x = 1000000
i = 1
j = 1
c = 3

while c < x:
    if c % 1000 == 0: 
        print(c)                
    t = j
    j = i + j
    i = t    
    if f(j%1000000000) and g(j):
        print(c)
        break  
    c += 1

stop = time.time()
print(stop-start,' seconds.')