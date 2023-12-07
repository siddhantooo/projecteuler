# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 02:47:56 2015

@author: Siddhant
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

def digitalsum(n):
    s = 0
    while n > 0:
        s += n%10
        n = n//10
    return s

start = time.time()

maxsum = 0
for i in range(50,100):
    for j in range(50,100):
        x = i**j
        ds = digitalsum(x)
        if ds >= maxsum:
            maxsum = ds
            best = x

print(maxsum)            

stop = time.time()
print(stop - start)
