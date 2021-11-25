# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 22:47:02 2021

@title: Amplitude Modulation
@description: This explains the generation of AM DSB-SC Signal with its plots and the Calculation
              of Power Spectral Density (PSD)
@author: Vineet Aggarwal
"""

import numpy as np 
import matplotlib.pyplot as plt 
import scipy.fftpack   

Fm = 2e3  #Frequency of Modulating Signal 
Fc = 12e3   #Frequency of Carrier Signal 
Fs = 500e3  #Sampling Frequency 
Ts = 1/Fs   #Sampling Period 
Tstop = 6*(1/Fm)  #Four cycles of Message Signal 
kf = 0.4    #Modulation Index 

t = np.arange(0, Tstop, Ts)   #Time Domain 
N = t.size

carrier = np.cos(2*np.pi*Fc*t)   #Carrier Signal 
msgSignal = np.cos(2*np.pi*Fm*t) #Modulating Signal (MessageSignal) 
dsb_sc = msgSignal*carrier #AM DSB-SC Signal 

#%%
'''
Plotting following: Message, Carrier and AM DSB-SC Signals 
'''
fig, axss = plt.subplots(3, 1, figsize=(15,14), dpi=80)  
#Plotting Message/Modulating Signal
axss[0].plot(t/1e-3, msgSignal, linewidth=2, color='g')  
axss[0].set_xlabel("Message Signal")        
axss[0].set_title("DSB-SC Modulation")      
axss[0].tick_params(axis='both',which='major',labelsize=15)   
for tick in axss[0].get_xticklabels():      
    tick.set_fontname("Times New Roman")    
for tick in axss[0].get_yticklabels():      
    tick.set_fontname("Times New Roman")    

#Plotting Carrier Signal
axss[1].plot(t/1e-3, carrier, linewidth=2, color='r')   
axss[1].set_xlabel("Carrier Signal")                    
axss[1].set_ylabel("Amplitude", fontsize=20, fontname="Times New Roman")  
axss[1].tick_params(axis='both',which='major',labelsize=15)               
for tick in axss[1].get_xticklabels():                 
    tick.set_fontname("Times New Roman")               
for tick in axss[1].get_yticklabels():                 
    tick.set_fontname("Times New Roman")               

#Plotting AM Signal
axss[2].plot(t/1e-3, dsb_sc, linewidth=2)         
axss[2].plot(t/1e-3, msgSignal, color='g', linestyle="dashed", linewidth=3)  
axss[2].plot(t/1e-3, -msgSignal, color='g', linestyle="dashed", linewidth=3) 
axss[2].set_xlabel("time [ms]", fontsize=20, fontname="Times New Roman")     
axss[2].tick_params(axis='both',which='major',labelsize=15)       
for tick in axss[2].get_xticklabels():      
    tick.set_fontname("Times New Roman")    
for tick in axss[2].get_yticklabels():      
    tick.set_fontname("Times New Roman")    


#%%
'''
Plotting PSD for above signal messages 
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
S_AM = scipy.fftpack.fft(dsb_sc)  
f_id_am = scipy.fftpack.fftfreq(len(dsb_sc))*Fs  
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

    
