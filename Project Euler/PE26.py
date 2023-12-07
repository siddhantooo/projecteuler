# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 00:54:13 2014

@author: Siddhant
"""
from math import ceil, log10
from time import time
import itertools as it
start = time()
maxprec = 2000
maxlen = 0
best = 1
for n in range(980,1000):
#    if n % 10 == 0:
#        print(n)
    prec = 0
    found = False
    i = n
    Q = []
    j = 10
    c = 1
    while j != 0 and prec < maxprec and not found:   
#        print(n,j)
        while j <= i:
            j = j*10
        q = (int(j/i))
        Q.append(q)
        prec += 1
        j = j%i
        if prec % 20 == 0:
            
            k = 0
            while k+9 < prec and not found:
                Q1 = Q[k+1:]
                r = int(prec/10) - 1
                while r+10 < prec:
#                    print(k,Q,r)        
#                    input()
                    if Q[k:k+10] == Q1[r:r+10]:
                       l = r + 1
                       if l > maxlen:
                           best = n
                           maxlen = l
                           print(best,maxlen)
                       found = True    
                       break    
                    r += 1
                k += 1
            
        
print('done.',time()-start,'seconds',best,maxlen)
        