# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 01:54:14 2014

@author: Siddhant
"""

def pent(n):
    return int((1.5)*(n**2) -(0.5*n))

pents = []
for i in range(1,10000):
    pents.append(pent(i))

print (pents[-1])

pkneg = {}
for p in pents[:5000]:
    pkneg[str(p)] = []
    if pents.index(p)%200==0:
        print(pents.index(p))
#    print(p)
#    input()
    pless = pents[:pents.index(p)]
    for q in pless:
        if (p - q) in pless:
            if (p + q) in pents[p:]:
                pkneg[str(p)].append(q)

pk = {}
for p in pkneg.keys():
    if pkneg[p] != []:
        pk[p] = pkneg[p]

print (len(pkneg), pk)