# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 04:08:02 2015

@author: Siddhant
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

def minpathsum(n,m):
    global matrix, memo
    print(n,m)
    if (n,m) in memo:
        return memo[(n,m)]
    elif n == 79:
        memo[(n,m)] = matrix[n][m] + minpathsum(n,m+1)
        return memo[(n,m)]
    elif m == 79:
        memo[(n,m)] = matrix[n][m] + minpathsum(n+1,m)
        return memo[(n,m)]
    else:
        memo[(n,m)] = matrix[n][m] + min(minpathsum(n+1,m),minpathsum(n,m+1))
        return memo[(n,m)]


start = time.time()
#matrix = [[131,201,630,537,805],[673,96,803,699,732],[234,342,746,497,524],[103,965,422,121,37],[18,150,111,956,331]]
#memo = {(4,4):331}
memo = {(79,79):7981}
matrix = pd.read_csv('C:\\Users\\Siddhant\\Downloads/p081_matrix.txt',index_col=False, header=None)
print(matrix)
print(minpathsum(0,0))
stop = time.time()
print(stop - start)
