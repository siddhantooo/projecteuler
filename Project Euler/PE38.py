# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 20:22:48 2014

@author: Siddhant
"""
def isPandig(n,m=9):
    'Checks whether n is pandigital for (1,2,...,m).'
    n = str(n)
    M = list(range(1,m+1))
    if len(n) > m:
        return False
    for i in n:
        if int(i) in M:
            M.remove(int(i))
        else:
            return False
    return True

l = {}    
d = 1
while d < 5:
    Max = int(9/d)
    for i in range(10**(d-1),10**d): 
        p = str(i*1) + str(i*2)
        j = 3
        while len(p) < 9:
            p += str(i*j)
            j += 1
        if isPandig(p):
            l[(i,j-1)] = int(p)
    d += 1
    
print(max(l.values()))