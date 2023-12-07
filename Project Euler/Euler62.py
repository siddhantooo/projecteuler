# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 03:06:35 2015

@author: Siddhant
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

def isPerm(n,m):
    digits_n = []
    while n > 0:
        digits_n.append(n%10)
        n = n//10
    digits_n.sort()
    digits_m = []
    while m > 0:
        digits_m.append(m%10)
        m = m//10
    digits_m.sort()
    return digits_n == digits_m
            
start = time.time()
n = int(1e3)
cubes = []
for i in range(500,10*n+1):
    cubes.append(i**3)

maxcount = 1
for j in cubes:
    ix = cubes.index(j)
    count = 1
    for i in cubes[ix+1:]:
        if isPerm(i,j):
            count += 1            
            print(j,i)
    if count == 5:
        print(j)
        break

stop = time.time()
print(stop - start)
