# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 23:00:02 2014

@author: Siddhant
"""
#from decimal import *
#getcontext().prec = 10000
#J = []
#for i in range(2,1000):
##    decimal.FloatOperation(1/i)
#    j = str(1/Decimal(i))[2:4999]
#    J.append(j)
##for j in J:
##print(J[:10])
#L = {}
#for j in J:
#    start = 0
#    flag = True
#    while start < len(j) and flag:    
#        ind = 1
#        while ind < int(len(j)/2):
#            k = 2
#            recur = False
#            while k < int((len(j))/ind):
#                if j[start:start+ind] != j[start+ind:start+(k*ind)]:
#                    break
#                k += 1
#                recur = True
#            if recur:
#                x = J.index(j)+2
#                L[x] = ind
#                flag = False
##                print(j,x,ind)
##                input()
#                break
#                
#            ind += 1
#        start += 1
#m = max(L.values())
#for key in L.keys():
#    if L[key] == m:
#        print(key,L[key],J[key-2])
##print(len(L))
