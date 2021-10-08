# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 11:42:54 2021

@title: Digital Modulation Techniques -- PSK
@author: Vineet Aggarwal - BITS ID: 2020MT13016
"""

import matplotlib.pyplot as plt # BITS ID: 2020MT13016
import numpy as np              # BITS ID: 2020MT13016

A=5                     #Amplitude - BITS ID: 2020MT13016
t=np.arange(0,1,0.001)  #Time Domain - BITS ID: 2020MT13016
Fc=10                   #Carrier Frequency - BITS ID: 2020MT13016
Fm=2                    #Message Frequency - BITS ID: 2020MT13016

#%%Carrier Signal 
x=A*np.sin(2*np.pi*Fc*t) #Equation for Carrier Signal - BITS ID: 2020MT13016
plt.subplot(3,1,1) # BITS ID: 2020MT13016
plt.plot(t,x,color='red') # BITS ID: 2020MT13016
plt.xlabel("Carrier Signal") # BITS ID: 2020MT13016
plt.ylabel("Amplitude") # BITS ID: 2020MT13016

#%%MessageSignal
u=[]#Message signal - BITS ID: 2020MT13016
b=[0.2,0.4,0.6,0.8,1.0] # BITS ID: 2020MT13016
s=1 # BITS ID: 2020MT13016
for i in t: # BITS ID: 2020MT13016
    if(i==b[0]): # BITS ID: 2020MT13016
        b.pop(0) # BITS ID: 2020MT13016
        if(s==0): # BITS ID: 2020MT13016
            s=1 # BITS ID: 2020MT13016
        else: # BITS ID: 2020MT13016
            s=0 # BITS ID: 2020MT13016
    u.append(s) # BITS ID: 2020MT13016

plt.subplot(3,1,2) # BITS ID: 2020MT13016
plt.plot(t,u,color='green') # BITS ID: 2020MT13016
plt.xlabel('Message Signal') # BITS ID: 2020MT13016
plt.ylabel('Amplitude') # BITS ID: 2020MT13016

#%%PSK Signal
v=[]#Sine wave multiplied with square wave - BITS ID: 2020MT13016
for i in range(len(t)): # BITS ID: 2020MT13016
    if(u[i]==1): # BITS ID: 2020MT13016
        v.append(A*np.sin(2*np.pi*Fc*t[i])) # BITS ID: 2020MT13016
    else: # BITS ID: 2020MT13016
        v.append(A*np.sin(2*np.pi*Fc*t[i])*-1) # BITS ID: 2020MT13016

plt.subplot(3,1,3)  # BITS ID: 2020MT13016
plt.plot(t,v)       # BITS ID: 2020MT13016
plt.xlabel("PSK")  # BITS ID: 2020MT13016
plt.ylabel("y")   # BITS ID: 2020MT13016

#%%Scaling - BITS ID: 2020MT13016
plt.subplots_adjust(hspace=1)   # BITS ID: 2020MT13016
plt.rc('font', size=12)         # BITS ID: 2020MT13016
