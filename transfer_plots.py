#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plottting curves for hohmann and bi-elliptic transfer 
for (n* = inf) case to draw comparison between the two.

Created on Fri Sep 13 22:59:51 2019

@author: ayushi
"""
import matplotlib.pyplot as plt
import math
import numpy as np

n = np.array([1, 3, 5, 7, 9, 10, 11, 13, 15, 40, 60], dtype=np.float64)
dVh = np.zeros(len(n))
dVb = np.zeros(len(n))

for i in range(len(n)) : 
    #hohmann transfer
    dVh[i] = (1 - math.sqrt(2/(n[i]+1)))/math.sqrt(n[i]) + math.sqrt(2*n[i]/(n[i]+1)) -1 
    
    #bi-elliptic transfer
    dVb[i] = (math.sqrt(2) - 1)*(1 + 1/math.sqrt(n[i]))

plt.plot(n, dVh, label='hohmann transfer')
plt.plot(n, dVb, label='Bi-elliptic transfer')
plt.show()