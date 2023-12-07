# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 05:14:51 2014

@author: Siddhant
"""
from primesieve import *
primes = soe(200000)
found = False
l = []
n = 2
y =134043 
print(491 in primes)
while not found and n < 200005:
    
#    print(n)
    c = 0
    for p in primes:
        if p*2*3*5 <= n and c <= 4:
            if n%p == 0:
                c += 1
        else:
            break
        
    if c == 4:
        l.append(n)
        print(n)
#        input()
        i = l.index(n)
        if n-1 == l[i-1] and n-2 == l[i-2] and n-3 == l[i-3]:
            print(l[i-3:i+1])        
            found = True
#    print(n,c)
#    input()
    n += 1
print(len(l))
#for n in l:
#    if n%1000 == 0:
#        print(n)
#    if n+1 in l:
#        if n+2 in l:
#            if n+3 in l:
#                print('yay',n)
#                break
#        else:
#            continue
#    else:
#        continue
        
    
print(y in l)