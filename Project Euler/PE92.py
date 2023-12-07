# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 21:25:57 2014

@author: Siddhant
"""
from math import ceil, log10
from time import time
start = time()
end = 10000000
memo = {1:False,10:False,58:True,85:True,89:True}
sq = [i**2 for i in range(10)]
kitne = []
for i in range(1,568):  
    s = i
    S = [s]
    found = False
    while not found:
        if s in memo:
            if memo[s]:
                for q in S:
                    if q <= 567:                    
                        memo[q] = True
                    if q not in kitne:
                        kitne.append(q)
                print('yes:',i)
                found = True
            else:
                for q in S:
                    memo[q] = False
#                print('no:',i)
                found = True
        j = s
        l = 1
        if j != 1:
            l = ceil(log10(j)+0.00000001)
        k = 1
        s = 0
#        print(i,j,l,memo)
#        input()
        while k <= l:
            s += (j%10)**2
            j = int(j/10)
            k += 1
        S.append(s)
klen = len(kitne)
for i in range(568,end):   
    if i%100000 == 0:
        print(i)
    j = i
    l = ceil(log10(j)+0.00000001)
    k = 1
    s = 0
    while k <= l:
        s += sq[j%10]
        j = int(j/10)
        k += 1
    if memo[s]:
        klen += 1

print(klen,time()-start)