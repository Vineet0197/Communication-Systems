# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 10:24:52 2021

@title: Amplitude Modulation
@description: This explains the generation of Standard Full AM Signal with its plots and the Calculation
              of Power Spectral Density (PSD)
@author: Vineet Aggarwal
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

Ac = 1     #Carrier Wave Amplitude
Am = 1     #Amplitude of Modulating Signal
Fm = 1e3  #Frequency of Modulating Signal
Fc = 10e3   #Frequency of Carrier Signal
Fs = 500e3  #Sampling Frequency
Ts = 1/Fs   #Sampling Period 
Tstop = 6*(1/Fm)  #Four cycles of Message Signal
beta = Am/Ac    #Modulation Index

t = np.arange(0, Tstop, Ts)   #Time Domain

carrier = Ac*np.cos(2*np.pi*Fc*t)   #Carrier Signal
msgSignal = Am*np.cos(2*np.pi*Fm*t) #Modulating Signal (MessageSignal)
AMModulatedSignal = (Ac+(Am*np.cos(2*np.pi*Fm*t)))*np.cos(2*np.pi*Fc*t) #AM Signal 

#%%
'''
Plotting following: Message, Carrier and AM Signals
'''
#Plotting Message/Modulating Signal
plt.subplot(3, 1, 1) 
plt.title('Amplitude Modulation') 
plt.plot(msgSignal,'g') 
plt.xlabel('Message Signal') 
plt.ylabel('Amplitude') 

#Plotting Carrier Signal
plt.subplot(3,1,2) 
plt.plot(carrier,'r') 
plt.ylabel('Amplitude')  
plt.xlabel('Carrier Signal') 

#Plotting AM Signal
plt.subplot(3,1,3) 
plt.plot(AMModulatedSignal) 
plt.ylabel('Amplitude') 
plt.xlabel('AM Signal') 

#Scaling
plt.subplots_adjust(hspace=1) 
plt.rc('font', size=15) 
fig = plt.gcf() 
fig.set_size_inches(16,9) 

#%%
'''
Plotting PSD for above signals
'''
fig1, axs = plt.subplots(3, 1, figsize=(9,8))

#This plots PSD for Message Signal 
S_msg = scipy.fftpack.fft(msgSignal)
f_id_msg = scipy.fftpack.fftfreq(len(msgSignal))*Fs
axs[0].plot(f_id_msg/1e3,np.abs(S_msg)**2/(np.max(np.abs(S_msg)**2)), linewidth=2, color="green")
axs[0].set_xlim([-15,15])   
axs[0].tick_params(axis='both',which='major',labelsize=15)
for tick in axs[0].get_xticklabels():    
    tick.set_fontname("Times New Roman")  
for tick in axs[0].get_yticklabels():     
    tick.set_fontname("Times New Roman")
    

#This plots PSD for Carrier Signal 
S_carrier = scipy.fftpack.fft(carrier)  
f_id_carrier = scipy.fftpack.fftfreq(len(carrier))*Fs  
axs[1].plot(f_id_carrier/1e3,np.abs(S_carrier)**2/(np.max(np.abs(S_carrier)**2)), linewidth=2, color="red") 
axs[1].set_xlim([-15,15])  
axs[1].tick_params(axis='both',which='major',labelsize=15)  
for tick in axs[1].get_xticklabels():  
    tick.set_fontname("Times New Roman")  
for tick in axs[1].get_yticklabels():     
    tick.set_fontname("Times New Roman")  
    

#This plots PSD for AM Modulated Signal
S_AM = scipy.fftpack.fft(AMModulatedSignal)  
f_id_am = scipy.fftpack.fftfreq(len(AMModulatedSignal))*Fs  
axs[2].plot(f_id_am/1e3,np.abs(S_AM)**2/(np.max(np.abs(S_AM)**2)), linewidth=2)  
axs[2].set_xlim([-15,15])  
axs[2].tick_params(axis='both',which='major',labelsize=15)  
for tick in axs[2].get_xticklabels():  
    tick.set_fontname("Times New Roman")  
for tick in axs[2].get_yticklabels():     
    tick.set_fontname("Times New Roman")  
    
#Setting x and y labels for PSD
axs[1].set_ylabel("PSD", fontsize=15, fontname="Times New Roman")  
axs[2].set_xlabel("frequency [KHz]", fontsize=15, fontname="Times New Roman")  

    



