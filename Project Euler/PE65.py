# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 06:57:50 2014

@author: Siddhant
"""
#import itertools as it
#import numpy as np
#
#def factorial(n):
#    s = 1
#    for i in range(2,n+1):
#        s = s*i
#    return int(s)

def x(n):
    if n == 1:
        return 2
    elif n % 3 == 0:
        return 2*int(n/3)
    else:
        return 1

#def num(n):
#    return x(n+1)
#def den(n):
#    return (x(n)*x(n+1))+1
    
def e(n):
    if n == 1:
        return 2,1
    X = [0]
    for i in range(1,n+1):
        X.append(x(i))
    c = n
    y = 1
    while c >= 1:
        print(c,y,X)
#        input()        
        X[c-1] = X[c]*X[c-1]+y
        y = X[c]
        c -= 1
    return X[1],X[2]
    
    
        
y = 100

ans = e(y)
s = 0
for i in str(ans[0]):
    s += int(i)
print ('num,den:',ans,'\nsum of num:',s)

#def e(n):
#    y = factorial(n)
#    num = 2*y
#    for i in range(n):
        