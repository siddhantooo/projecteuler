# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 04:41:12 2014

@author: Siddhant
"""
d = {}
for i in range(10):
    d[i]=i**5
print(d)
n = 2    
l = []
while n < 500000:
    s = 0
    x = n
    c = 0
    while x != 0:
        i = x%(10)
        s += d[i]
        x = int(x/10)
        c += 1
    if s == n:
        l.append(n)
    n += 1
        
print(l,sum(l))