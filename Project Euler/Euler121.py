# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 22:51:19 2015

@author: Siddhant
"""
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
import time
import itertools as it
start = time.time()

def probblue(n):
    return 1/(1+n)
    
def probtimesblue(m,n):
    prob = 0    
    for comb in it.combinations(range(1,n+1),m):
        combprob = 1        
        for turn in comb:
            combprob *= probblue(turn)
        for turn in set(range(1,n+1)).difference(comb):
            combprob *= (1-probblue(turn))
        prob += combprob
    return prob

def probwinning(n):
    prob = 0
    for i in range(n//2+1,n+1):
        prob += probtimesblue(i,n)
    return prob

#print(probtimesblue(4,4)+probtimesblue(3,4))
print(probwinning(15),probwinning(15)**(-1))

stop = time.time()
print(stop - start)
