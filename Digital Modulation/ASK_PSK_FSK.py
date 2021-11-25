# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 23:35:45 2021

@title:  Digital Modulation Techniques
@description:  This Program includes Digital Modulation Techniques such as
               ASK, PSK and FSK.
@author: Vineet Aggarwal 
"""

import numpy as np        
import matplotlib.pyplot as plt    

bit_seq = np.array([1,0,1,0]) #Input Bit Sequence

Tb = 2e-3        # Bit Duration 
Tc = 0.5e-3      # Carrier Duration 
fc = 1/Tc        # Carrier Frequency 
td = bit_seq.size*Tb    
tseq = np.linspace(0,td,4000,endpoint=False)   

ct = np.cos(2*np.pi*fc*tseq[0:-1])    # Carrier Signal 
if bit_seq[0]>0:          
    bseq = np.ones((999)) 
else:                     
    bseq = np.zeros((999)) 

for idx in range (1,bit_seq.size):   
    if bit_seq[idx]>0:               
        temp = np.ones((1000))       
    else:                            
        temp = np.zeros((1000))      
    bseq = np.hstack([bseq,temp])    

s_ask = bseq*ct    #ASK Signal 

bseq_bpsk = -np.ones((bseq.size))+2*bseq      
s_bpsk = bseq_bpsk*ct    #BPSK Signal 

bseq_fsk1 = bseq        
bseq_fsk2 = np.ones((bseq.size))-bseq     
ct1 = ct                #First Carrier for FSK 
ct2 = np.cos(2*np.pi*2*fc*tseq[0:-1])    #Second Carrier for FSK 

s_fsk = ct1*bseq_fsk1+ct2*bseq_fsk2     #FSK Signal 

# For ASK
fig, axs = plt.subplots(3, 1, figsize=(9, 8), dpi=80, facecolor='w', edgecolor='k')  
axs[0].plot(tseq[0:-1]/1e-3,bseq,linewidth=2)        
axs[0].grid(True)                  
axs[0].tick_params(axis='both',which='major',labelsize=15)    
axs[0].set_ylabel(r'$m(t)$',fontsize=20,fontname="Times New Roman")  
for tick in axs[0].get_xticklabels():   
    tick.set_fontname("Times New Roman")     
for tick in axs[0].get_yticklabels():        
    tick.set_fontname("Times New Roman")      
axs[1].plot(tseq[0:-1]/1e-3,ct,color="red",linewidth=2)  
axs[1].grid(True)          
axs[1].set_ylabel(r'$c(t)$',fontsize=20,fontname="Times New Roman")       
axs[1].tick_params(axis='both',which='major',labelsize=15)       
for tick in axs[1].get_xticklabels():          
    tick.set_fontname("Times New Roman")         
for tick in axs[1].get_yticklabels():            
    tick.set_fontname("Times New Roman")       

axs[2].plot(tseq[0:-1]/1e-3,s_ask,color="green",linewidth=2)     
axs[2].grid(True)              
axs[2].set_xlabel('time [ms]',fontsize=20,fontname="Times New Roman")     
axs[2].tick_params(axis='both',which='major',labelsize=15)      
for tick in axs[2].get_xticklabels():          
    tick.set_fontname("Times New Roman")         
for tick in axs[2].get_yticklabels():          
    tick.set_fontname("Times New Roman")       
axs[2].set_ylabel(r'$S_{BASK}(t)$',fontsize=20,fontname="Times New Roman")   


# For BPSK
fig, axs = plt.subplots(3, 1, figsize=(9, 8), dpi=80, facecolor='w', edgecolor='k')   
axs[0].plot(tseq[0:-1]/1e-3,bseq_bpsk,linewidth=2)    
axs[0].grid(True)     
axs[0].tick_params(axis='both',which='major',labelsize=15)    
axs[0].set_ylabel(r'$m(t)$',fontsize=20,fontname="Times New Roman")    
for tick in axs[0].get_xticklabels():       
    tick.set_fontname("Times New Roman")    
for tick in axs[0].get_yticklabels():       
    tick.set_fontname("Times New Roman")    
axs[1].plot(tseq[0:-1]/1e-3,ct,color="red",linewidth=2)     
axs[1].grid(True)       
axs[1].set_ylabel(r'$c(t)$',fontsize=20,fontname="Times New Roman")     
axs[1].tick_params(axis='both',which='major',labelsize=15)      
for tick in axs[1].get_xticklabels():     
    tick.set_fontname("Times New Roman")  
for tick in axs[1].get_yticklabels():     
    tick.set_fontname("Times New Roman")  

axs[2].plot(tseq[0:-1]/1e-3,s_bpsk,color="green",linewidth=2)    
axs[2].grid(True)    
axs[2].set_xlabel('time [ms]',fontsize=20,fontname="Times New Roman")   
axs[2].tick_params(axis='both',which='major',labelsize=15)       
for tick in axs[2].get_xticklabels():           
    tick.set_fontname("Times New Roman")        
for tick in axs[2].get_yticklabels():           
    tick.set_fontname("Times New Roman")        
axs[2].set_ylabel(r'$S_{BPSK}(t)$',fontsize=20,fontname="Times New Roman")   


# For FSK
fig, axs = plt.subplots(4, 1, figsize=(9, 8), dpi=80, facecolor='w', edgecolor='k')  
axs[0].plot(tseq[0:-1]/1e-3,bseq_bpsk,linewidth=2)       
axs[0].grid(True)        
axs[0].tick_params(axis='both',which='major',labelsize=15)    
axs[0].set_ylabel(r'$m(t)$',fontsize=20,fontname="Times New Roman")   
for tick in axs[0].get_xticklabels():        
    tick.set_fontname("Times New Roman")     
for tick in axs[0].get_yticklabels():        
    tick.set_fontname("Times New Roman")     
axs[1].plot(tseq[0:-1]/1e-3,ct1,color="red",linewidth=2)      
axs[1].grid(True)         
axs[1].set_ylabel(r'$c_{1}(t)$',fontsize=20,fontname="Times New Roman")  
axs[1].tick_params(axis='both',which='major',labelsize=15)      
for tick in axs[1].get_xticklabels():      
    tick.set_fontname("Times New Roman")   
for tick in axs[1].get_yticklabels():      
    tick.set_fontname("Times New Roman")   
    
axs[2].plot(tseq[0:-1]/1e-3,ct2,color="orange",linewidth=2)    
axs[2].grid(True)      
axs[2].set_ylabel(r'$c_{2}(t)$',fontsize=20,fontname="Times New Roman")  
axs[2].tick_params(axis='both',which='major',labelsize=15)     
for tick in axs[2].get_xticklabels():          
    tick.set_fontname("Times New Roman")       
for tick in axs[2].get_yticklabels():          
    tick.set_fontname("Times New Roman")       

axs[3].plot(tseq[0:-1]/1e-3,s_fsk,color="green",linewidth=2)     
axs[3].grid(True)        
axs[3].set_xlabel('time [ms]',fontsize=20,fontname="Times New Roman")    
axs[3].tick_params(axis='both',which='major',labelsize=15)       
for tick in axs[3].get_xticklabels():         
    tick.set_fontname("Times New Roman")      
for tick in axs[3].get_yticklabels():        
    tick.set_fontname("Times New Roman")      
axs[3].set_ylabel(r'$S_{FSK}(t)$',fontsize=20,fontname="Times New Roman")   


