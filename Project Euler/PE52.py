# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 21:42:51 2014

@author: Siddhant
"""
import time as time
start = time.time()
found = False
x = 1
dontcheck = []
while not found:
    if x not in dontcheck:    
        m = set(str(x))
#        print(x,m)
        if set(str(2*x)) == m:
            if set(str(3*x)) == m:
                if set(str(4*x)) == m:
                    if set(str(5*x)) == m:
                        if set(str(6*x)) == m:
                            found = True
                        else:
                            dontcheck.append(3*x)
                            dontcheck.append(2*x)
                            x += 1
                else:
                    dontcheck.append(2*x)
    if x % 100 == 0:
        print(x,len(dontcheck))
    x += 1

print(x-1,2*(x-1),len(dontcheck),time.time()-start,'sec.')    