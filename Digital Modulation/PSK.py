# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 11:42:54 2021

@title: Digital Modulation Techniques -- PSK
@author: Vineet Aggarwal 
"""

import matplotlib.pyplot as plt 
import numpy as np              

A=5                     #Amplitude 
t=np.arange(0,1,0.001)  #Time Domain 
Fc=10                   #Carrier Frequency 
Fm=2                    #Message Frequency 

#%%Carrier Signal 
x=A*np.sin(2*np.pi*Fc*t) #Equation for Carrier Signal 
plt.subplot(3,1,1) 
plt.plot(t,x,color='red') 
plt.xlabel("Carrier Signal") 
plt.ylabel("Amplitude") 

#%%MessageSignal
u=[]#Message signal 
b=[0.2,0.4,0.6,0.8,1.0] 
s=1 
for i in t: 
    if(i==b[0]): 
        b.pop(0) 
        if(s==0): 
            s=1 
        else: 
            s=0 
    u.append(s) 

plt.subplot(3,1,2) 
plt.plot(t,u,color='green') 
plt.xlabel('Message Signal') 
plt.ylabel('Amplitude') 

#%%PSK Signal
v=[]#Sine wave multiplied with square wave 
for i in range(len(t)): 
    if(u[i]==1): 
        v.append(A*np.sin(2*np.pi*Fc*t[i])) 
    else: 
        v.append(A*np.sin(2*np.pi*Fc*t[i])*-1) 

plt.subplot(3,1,3)  
plt.plot(t,v)       
plt.xlabel("PSK")  
plt.ylabel("y")   

#%%Scaling 
plt.subplots_adjust(hspace=1)   
plt.rc('font', size=12)         
