#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 23:31:58 2019

@author: ayushi
"""
import math
import matplotlib.pyplot as plt
import numpy as np

#defining constants
pi = 3.14159
mu = 3.98574405E+14
au = 1.496e+11

def hohmann(ra, rb, theta_1, theta_2):
    
    
    
    r1 = ra*au
    r2 = rb*au
    theta1 = theta_1*pi/180
    theta2 = theta_2*pi/180
    n = r2/r1
    print('n: ', n)
    
    v1 = math.sqrt(mu/r1)
    #impulse1 at perigee
    dV1 = v1*( (1 - math.sqrt(2/(n+1)))/math.sqrt(n)) 
    #impulse2 at apogee
    dV2 = v1*(math.sqrt(2*n/(n+1)) -1) 
    
    print('impulse required at extreme positions: ', dV1, ' ', dV2)
    
    w1 = math.sqrt(mu/r1**3) 
    w2 = math.sqrt(mu/r2**3)
    print('omega: ', w1, ', ', w2)
    a = 0.5*(r1+r2)
    
    T = pi*math.sqrt(a**3/mu) #time period for half trajectory
    print('trajectory time: ', T/86400, 'days')
    
    
    #by equating time and angle conditions
    d_theta1 = (theta2 - theta1 + T*w2 - pi)/(1 - w2/w1) %3.14
    d_theta2 = w2*(theta1/w1 +T)
    
    print('true anomaly at launch date: ',d_theta1, ', ', d_theta2 )
    
    tA = theta1/(w1*86400)
    print('time period for launch from position 1:', tA, 'days')
    
    #plot
    theta = np.linspace(-pi, pi, 100)
    theta_e = theta1+d_theta1
    
    x1 = np.zeros(len(theta))
    y1 = np.zeros(len(theta))
    
    x2 = np.zeros(len(theta))
    y2 = np.zeros(len(theta))
    
    x = np.zeros(len(theta))
    y = np.zeros(len(theta))
    h = r1*(v1+dV1)
    e = math.sqrt(1 - (h**2/(mu*a)))
    b = a*math.sqrt(1- e**2)
    
    for i in range(len(theta)):
        x1[i] = r1*math.cos(theta[i])
        y1[i] = r1*math.sin(theta[i])
        
        x2[i] = r2*math.cos(theta[i])
        y2[i] = r2*math.sin(theta[i])
        
        x[i] = a*math.cos(theta[i])*math.cos(theta_e) + b*math.sin(theta[i])*math.sin(theta_e) - (a-r1)*math.sin(theta_e)
        y[i] = -a*math.cos(theta[i])*math.sin(theta_e) + b*math.sin(theta[i])*math.cos(theta_e) + (a-r1)*math.cos(theta_e)
        
    plt.plot(x1, y1, label='orbit1')
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.plot(x2, y2, label='orbit2')
    plt.plot(x, y, label='transfer orbit')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    
    return

hohmann(2, 3.5, 139, 271)
