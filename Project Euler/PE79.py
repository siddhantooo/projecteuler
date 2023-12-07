# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 20:01:18 2014

@author: Siddhant
"""

import csv
import numpy as np
data = open('p079_keylog.txt')
keys = []
for line in data:
    l = []
#    print (line)
#    input()
    l.append(line[0])
    l.append(line[1])
    l.append(line[2])    
    keys.append(l)
#print(keys[1:5])
x = [i for i in '01236789']
maxlen = 20
greatestkey = 10**maxlen
guess = ''
counts = {}
for i in x:
    counts[i] = np.zeros(3, dtype = int)
for line in keys:
    for i in line: 
        counts[i][line.index(i)] += 1
print(counts)
# so no 4s or 5s in the key.
# 7 is first digit, 0 is last digit.
i = 0
while i < 8:
    for line in keys:    
        if x[i] in line:
            print(line)
    input()
    i += 1
# so 3 is 2nd digit.
'73162890'
