# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 00:56:00 2014

@author: Siddhant
"""
x = 1000000
y = x*100
from primesieve import *
import itertools as it
primes = soe(x)
primes2 = [i for i in primes if i < 10000]
p = []
n = x + 1
print('start')
while n < y:
    if n % 10000 == 0:
        print(n)
    for i in primes2:
        if n%i == 0:
            break
        p.append(n)
    n += 2

print('done')
for i in p:
    i = str(i)
    k = len(i)
    ch = 1
    
    