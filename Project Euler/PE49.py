# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 19:14:16 2014

@author: Siddhant
"""

from PE41 import soe

def isPerm(n,m):
    '''Checks whether m is a permutation of n.'''
    n = str(n)
    m = str(m)
    for i in m:
        if i not in n:
            return False
    return True

#print(isPerm(1,101))
primes = soe(9999)
p = []
for i in primes:
    if i > 1000:
        p.append(i)
print(len(p))
primeseq = []
for i in p:
    k = p.index(i)
    j = 1
    while j <= k:
        seq = []    
        d = i - p[k-j]
        if (i+d) in p and isPerm(i,i+d) and isPerm(i,p[k-j]) and isPerm(i+d,i):
            seq.append(p[k-j])                        
            seq.append(i)            
            seq.append(i+d)
            primeseq.append(seq)
        j += 1
print(len(primeseq),primeseq)            