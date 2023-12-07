# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 16:20:15 2014

@author: Siddhant
"""

def sqrt2(n):
    if n == 1:
        return 1,1
    else:
        c = n
        y = 1
        x = 2
        while c > 1:
            t = x            
            x = x*2 + y
            y = t
            c -= 1
        t = x
        x = x + y
        y = t
        return x,y

if __name__ == "__main__":
    count = 0    
    for i in range(1,1001):
        if len(str(sqrt2(i)[0])) > len(str(sqrt2(i)[1])):
            count += 1
    print(count)