# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 22:34:28 2014

@author: Siddhant
"""
from time import time
from primesieve import *
start = time()

primes = soe(1000000)
check = soe(1000)
check.remove(2)
pairs = []

for i in check:
    for j in check:
        if (j,i) not in pairs:        
            if isPrime(int(str(i)+str(j))) and isPrime(int(str(j) + str(i))):
                pairs.append((i,j))
#                print(i,j)
#                input()            


print(len(pairs))

triples = []
for i in pairs:
    for j in pairs:
        if i[1] == j[0]:
            if (i[0],j[1]) in pairs:
                triples.append((i[0],i[1],j[1]))
quads = []
for i in triples:
    for j in triples:
        if i != j and i[:2] == j[:2]:
            if (i[0],j[2]) in pairs:
#                if (i[0],i[1],j[2],i[2]) not in quads:
                quads.append((i[0],i[1],i[2],j[2]))

quints = []
for i in quads:
    for j in quads:
        if i != j and i[:3] == j[:3]:
            if (i[0],j[3]) in pairs:
                quints.append([i[0],i[1],i[2],i[3],j[3]])
s = 100000
for i in quints:
    if sum(i) <= s:
        s, best = sum(i),i
print(s,best)
    
print(triples)
print(quads)
print(quints)

print(time()-start,'seconds.')
