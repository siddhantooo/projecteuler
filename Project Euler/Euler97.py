# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 03:49:40 2015

@author: Siddhant
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import math
start = time.time()


n = 193498252232
x = math.log10(n)
print(x)
print(10**(x-11))

x = math.log(28433) + 7830457*math.log(2)
print(x)
print(10**(x-5427669))




stop = time.time()
print(stop - start)
