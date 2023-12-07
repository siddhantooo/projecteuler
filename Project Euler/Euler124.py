# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 23:24:01 2015

@author: Siddhant
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

def primesieve(n):
    check = {i:True for i in range(2,n+1)}
#    print(check)
    for i in range(2,int(n**0.5+1)):
        if check[i]:
#            print(i)
            lim = n//i
#            print(lim)
            for j in range(2,lim+1):
                check[j*i] = False
#            print(check)
    primes = [i for i in check if check[i]]
    return primes

def rad(n):
    global primes
    if n in primes:
        return n
    rad = 1
    lim = n/2 + 1
#    lim = n + 1
#    print(lim)
    for i in primes:
#        print(i)
        if i >= lim:
            break
        elif n//i - n/i == 0:
            rad *= i
#            print(rad)
    return rad

start = time.time()

n = 100000
primes = primesieve(n)
print(primes[-1])
df = pd.DataFrame(data=np.arange(1,n+1),index=np.arange(1,n+1))
#df['rad'] = df.apply(lambda x: rad(x[0]), axis=1)
for i in range(1,n+1):
    df.loc[i,'rad'] = rad(i)
    if i/100 - i//100 == 0:
        print(i)
print('rad done')
print(df.sort(['rad',0],inplace=1))
print(df, df.iloc[9999])

stop = time.time()
print(stop - start)
