# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 14:11:38 2014

@author: Siddhant
"""
from time import time
import numpy as np
import itertools as it
import csv
import string
start = time()

file = open('cipher.txt')
cipher = []
for i in csv.reader(file):
    cipher = i
cipher = np.array(cipher, dtype=int)
asc = {}
for i in string.ascii_lowercase:
    asc[i] = ord(i)
ascfull = {}
for i in string.ascii_letters:
    ascfull[i] = ord(i)
count = 0
cand = []
l = [x for x in range(97,123)]
m = [111,]
print(cipher,'\n',asc, '\n',l,'\n', ascfull, len(cipher)) 
#for combo in it.combinations_with_replacement(l,3):    
#    count += 1 
#    print(combo, count)
##    input()
#    
#    for k in range(0,100):
#        if (np.bitwise_xor(cipher[k],combo[k%3])) == 116:
#            if np.bitwise_xor(cipher[k+1],combo[(k+1)%3]) == 104:
#                if np.bitwise_xor(cipher[k+2],combo[(k+2)%3]) == 101:
#                    print(k%3, (k+1)%3, (combo[k%3]), (combo[(k+1)%3]),(combo[(k+2)%3]),count)
#                    cand.append([(combo[k%3]), (combo[(k+1)%3]),(combo[(k+2)%3])])            
##                    input()
#                    
#for c in cand:
#    for k in range(20):    
#        print(chr(np.bitwise_xor(cipher[k],c[k%3])))
#    input()
#print(cand)
#for q in l[:]:
#    for p in l[:]:
#        for r in l[:]:
#            s = ''
#            for j in range(0,250):
#                if j%3 == 0:
##                    print(chr(np.bitwise_xor(cipher[j],q)))
#                    s += chr(np.bitwise_xor(cipher[j],q))
#                elif j%3 == 1:
##                    print(chr(np.bitwise_xor(cipher[j],p)))
#                    s += chr(np.bitwise_xor(cipher[j],p))
#                else:
##                    print(chr(np.bitwise_xor(cipher[j],r)))
#                    s += chr(np.bitwise_xor(cipher[j],r))
##            print(s,q,p,r)
##            input()
#            if 'the' in s:
#                print(s,q,p,r)
#                input()

total = 0
for j in range(0,1201):
    if j % 3 == 0:
        a = np.bitwise_xor(cipher[j],103)
    elif j % 3 == 1:
        a = np.bitwise_xor(cipher[j],111)
    else:
        a = np.bitwise_xor(cipher[j],100)
        
    total += a
print(total)



#for q in l:
#    s = ''
#    for j in range(100):
#        if j%3 == 0:
###                    print(chr(np.bitwise_xor(cipher[j],q)))
#            s += chr(np.bitwise_xor(cipher[j],q))
#            print(j,j%3,cipher[j],q)
#    print(s,q)
#    input()

#check = ['th','nt','ht']
#for combo in it.combinations_with_replacement(l,3):
#    count += 1
#    print(combo, count)
##    input()
#    for k in range(100):
#        if chr(np.bitwise_xor(cipher[k],combo[k%3])) + chr(np.bitwise_xor(cipher[k+1],combo[(k+1)%3]))== 'th':
#            for j in range(0,101):
#                print(chr(np.bitwise_xor(cipher[j],combo[k%3])))
#                input()
                
    

print(time()-start,'seconds.')
