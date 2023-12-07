# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 17:58:43 2014

@author: Siddhant
"""
import itertools as it
def soe(n):
    d = {}    
    for i in range(2,n+1):
        d[i] = True
    z = int(n**0.5 + 1)
    for i in range(2,z):
        if d[i] == True:
            for j in range(2,int(n/i)):
                d[i*j] = False
    primes = []
    for i in d:
        if d[i]:
            primes.append(i)
    return primes
        
if __name__=="__main__":  
    largest = 987654321
    z = int(largest**0.5) + 1
    primes = soe(z)
    a = str(largest)
    
    maxpanprime = 0
    digits = 2
    while digits < 10:
        for k in it.permutations(a[-digits:],digits):
            i = ''
            for l in k:
                i += l       
            i = int(i)        
            isPrime = True        
            ptocheck = primes[:i]
            for j in ptocheck:
                if i%j == 0:
                    isPrime = False                
                    break
            if isPrime and i > maxpanprime:
                maxpanprime = i
        digits += 1
    print(maxpanprime)
            
        
        