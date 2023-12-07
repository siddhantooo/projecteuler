# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 21:05:23 2014

@author: Siddhant
"""
import itertools as it
import primesieve
p = primesieve.soe(1000000)
f = [0,4,6,8]
q = []
for i in p:    
    inq = True    
    i = str(i)
    if len(i) == 1:
        continue
#    if i[-1] != '3' and i[-1] != '7':
#        continue
#    if i[0] == '1' or i[0] == '9':
#        continue
#    if i[0] == '3' and i[1] == '3':
#        continue
#    if i[0] == '3' and i[1] == '9':
#        continue
#    if i[-1] == '3' and i[-2] in ['3','9']:
#        continue
        
    for j in i:
        if int(j) in f:
            inq = False            
            break
    if inq:
        q.append(i)
        
print(len(q),q[-1])

new = []
a = [1,3,7,9]
for i in it.combinations_with_replacement(a,6):
    k = ''
    for b in i:
        k += str(b)
    for j in it.combinations_with_replacement([3,7],2):
        l = str(j[0]) + k + str(j[1])
#        print(int(l))
#        input()
        if primesieve.isPrime(int(l)):
            new.append(int(l))
#            print('T')
print(len(new))

q = q + new
r = []
for i in q:
#    print(i,len(r))
    inr = True
    i = str(i)
    k = len(i)
    j = 1
    while j < k:
        if int(i[j:]) not in p or int(i[:-j]) not in p:
            inr = False            
            break
        j += 1
    if inr:
        r.append(int(i))

print(len(r),r, sum(r))        