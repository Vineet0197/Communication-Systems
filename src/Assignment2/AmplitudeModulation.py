# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 10:24:52 2021

@title: Amplitude Modulation
@author: Vineet Aggarwal - BITS ID: 2020MT13016
"""

import numpy as np # BITS ID: 2020MT13016
import matplotlib.pyplot as plt # BITS ID: 2020MT13016

Ac = 15     #Carrier Wave Amplitude - BITS ID: 2020MT13016
Am = 10     #Amplitude of Modulating Signal - BITS ID: 2020MT13016
Fm = 50     #Frequency of Modulating Signal - BITS ID: 2020MT13016
Fc = 900e6  #Frequency of Carrier Signal - BITS ID: 2020MT13016
beta = Am/Ac    #Modulation Index - BITS ID: 2020MT13016

t = np.linspace(0,100,1000)     #Time Domain - BITS ID: 2020MT13016

carrier = Ac*np.cos(2*np.pi*Fc*t)   #Carrier Signal - BITS ID: 2020MT13016
msgSignal = Am*np.cos(2*np.pi*Fm*t) #Modulating Signal (MessageSignal) - BITS ID: 2020MT13016
AMModulatedSignal = (Ac+(Am*np.cos(2*np.pi*Fm*t)))*np.cos(2*np.pi*Fc*t) #AM Signal - BITS ID: 2020MT13016

#%%Plotting Message/Modulating Signal
plt.subplot(3, 1, 1) # BITS ID: 2020MT13016
plt.title('Amplitude Modulation') # BITS ID: 2020MT13016
plt.plot(msgSignal,'g') # BITS ID: 2020MT13016
plt.xlabel('Message Signal') # BITS ID: 2020MT13016
plt.ylabel('Amplitude') # BITS ID: 2020MT13016

#%%Plotting Carrier Signal
plt.subplot(3,1,2) # BITS ID: 2020MT13016
plt.plot(carrier,'r') # BITS ID: 2020MT13016
plt.ylabel('Amplitude') # BITS ID: 2020MT13016
plt.xlabel('Carrier Signal') # BITS ID: 2020MT13016

#%%Plotting AM Signal
plt.subplot(3,1,3) # BITS ID: 2020MT13016
plt.plot(AMModulatedSignal) # BITS ID: 2020MT13016
plt.ylabel('Amplitude') # BITS ID: 2020MT13016
plt.xlabel('AM Signal') # BITS ID: 2020MT13016

#%%Scaling
plt.subplots_adjust(hspace=1) # BITS ID: 2020MT13016
plt.rc('font', size=15) # BITS ID: 2020MT13016
fig = plt.gcf() # BITS ID: 2020MT13016
fig.set_size_inches(16,9) # BITS ID: 2020MT13016
