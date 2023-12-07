# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 22:17:50 2014

@author: Siddhant
"""
from time import time
from primesieve import soe
start = time()
primes = soe(1000000)
#maxl = 1
#critical = 1000001
#for n in primes:
#    if n > 100000:
#        break
#    else:
#        i = primes.index(n)
#        p = primes[:i]
#        shuru = 0
#        found = False
#        while shuru + maxl < i and p[shuru] < 15 and p[shuru+maxl] < n/5 and not found:
#            s = 0      
#            for q in p[shuru:]:
#                s += q
#                if s == n:
#                    if p.index(q) - shuru + 1 > maxl:
#                        maxl = p.index(q) - shuru + 1
#                        best = n
#                        print('yay',n,maxl,shuru)
##                        input()
#                    found = True
#                    break
#                elif s > n:
#                    break                    
#            shuru += 1

supermax = 1
maxl = 1
l = 1

for i in range(10):
    l = maxl
    while l < 1000:
            s = sum(primes[i:i+l+1])
            if s in primes:
                maxl, best = l+1, s
                print(maxl,best,i)
            l += 1
#    print(i,maxl,s)
#    input()
    
print(maxl,best,time()-start,'seconds.')
