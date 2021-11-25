# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 14:17:41 2021

@title: Standard Frequency Modulated Signal
@description: This Program generates the frequency modulated signal and
              shows on matplot lib
@author: Vineet Aggarwal 
"""

import numpy as np  
import matplotlib.pyplot as plt  

Am = 1  #Amplitude of MessageSignal 
fm = 0.7e3      #Message Signal Frequency in KHz 
fc = 10.2e3       #Carrier Signal Frequency in KHz 
fs = 1000e3     #Sampling Frequency in KHz 
ts = 1/fs       #Sampling Period in cycles per second 
tstop = 2*(1/fm)    #Four cycles of Message Signals 

t = np.arange(0,tstop,ts)       #Time Domain 
kf = 3000   #Frequency Sensitivity 
beta = (kf*Am)/fm    #Modulation Index 

xm = np.cos(2*np.pi*fm*t)   #Message Signal 
xc = np.sin(2*np.pi*fc*t)   #Carrier Signal 
s_fm = np.cos(2*np.pi*fc*t + beta*np.sin(2*np.pi*fm*t))     #Single Tone FM Signal 


fig, axs = plt.subplots(3,1,figsize=(9,8))   #Initializing SubPlots 
axs[0].plot(t/1e-3, xm, linewidth=2, color='g')   
axs[0].grid(True)             
axs[0].tick_params(axis='both', which='major', labelsize=15)  
for tick in axs[0].get_xticklabels():                   
    tick.set_fontname("Times New Roman")        
for tick in axs[0].get_yticklabels():           
    tick.set_fontname("Times New Roman")        
    
axs[1].plot(t/1e-3, xc, linewidth=2, color='r')  
axs[1].grid(True)                                
axs[1].set_ylabel('Voltage [V]', fontsize=20, fontname='Times New Roman')   
axs[1].tick_params(axis='both', which='major', labelsize=15)                
for tick in axs[1].get_xticklabels():            
    tick.set_fontname("Times New Roman")         
for tick in axs[1].get_yticklabels():            
    tick.set_fontname("Times New Roman")         
    
axs[2].plot(t/1e-3, s_fm, linewidth=2, color='#ffa500')       
axs[2].grid(True)                            
axs[2].set_xlabel('time [ms]', fontsize=20, fontname='Times New Roman')     
axs[2].tick_params(axis='both', which='major', labelsize=15)                
for tick in axs[2].get_xticklabels():        
    tick.set_fontname("Times New Roman")     
for tick in axs[2].get_yticklabels():        
    tick.set_fontname("Times New Roman")     
    
