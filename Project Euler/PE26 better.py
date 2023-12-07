# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 01:24:12 2014

@author: Siddhant
"""
best = 0
maxlen = 0
for i in range(983,984):
    n = i
    r = 10
    R = []
    c = 0
    while r != 0:
        if r < n:
            m = 0
            while r <= n:
                c += 1
                r = r*10  
#            c += m
        r = r%n
        c += 1
        if r in R:
            print(r)
            break
        R.append(r)
    l = c - R.index(r) - 1
    if l > maxlen:
        maxlen = l
        best = i
#        print(l,best,c,R.index(r),R)
    
print(best,maxlen)