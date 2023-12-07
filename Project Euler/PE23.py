# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 22:49:49 2014

@author: Siddhant
"""
import primesieve as ps

largest = 28123
abundant = []
p = ps.soe(28123)
for i in range(1,largest+1):
    if i in p:
        continue
    z = int(i**0.5) + 1
    f = [1]
    for j in range(2,z):
        if i%j == 0:
            f.append(j)
            if int(i/j) not in f:
                f.append(int(i/j))
    if sum(f) > i:
        abundant.append(i)
#    print(i,sum(f))
#    input()
print(len(abundant),abundant[0],abundant[-1])

d = {}
for i in range(1, largest + 1):
    d[i] = True
keys = d.keys()
for i in abundant:
    print(i)
    for j in abundant:
        if (i+j) in d:
            d[i+j] = False
    
r = []    
for key in d:
    if d[key]:
        r.append(key)
print(len(r),sum(r))
