# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 21:58:25 2014

@author: Siddhant
"""
from time import time
from math import *
start = time()

f = [factorial(x) for x in range(10)]

gmemo = {169:36301, 36301:1454, 1454:169, 871:45361,45361:871,872:45362,45362:872}
c = 0
for i in range(3,1000000):
    lmemo = [] 
    z = i
    while True:
        if z in gmemo:
            j = gmemo[z]
        else:
            j = 0
            for k in str(z):
                j += f[int(k)]
            if z < 1000000:
                gmemo[z] = j
        if j in lmemo:
            if len(lmemo) == 59:
                c += 1
                print(len(lmemo)+1,i,lmemo,j)
#            input()
            break
        else:            
            lmemo.append(j)
        z = j
        


print(c, time()-start,'seconds.')
