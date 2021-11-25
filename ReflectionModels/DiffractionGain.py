# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 21:44:23 2021

@title: Diffraction Gain - Knife Edge Diffraction Gain
@author: Vineet Aggarwal
"""

import numpy as np 
import scipy.special as sc  
import matplotlib.pyplot as plt   


v = np.arange(-3,5.1,0.1)    

T2_A, T1_A = sc.fresnel(np.inf)     
T2_B, T1_B = sc.fresnel(v)          

T1 = T1_A*np.ones(v.size)-T1_B      
T2 = T2_A*np.ones(v.size)-T2_B      

MI = T1-1j*T2               
Fv = 0.5*(1+1j)*MI          
Gd = 20*np.log10(np.abs(Fv))  
plt.plot(v, Gd, label='Exact Solution')   
plt.grid()                  
plt.xlim(-3, 5)             
plt.ylim(-30,5)             
plt.xlabel('Fresnal Diffraction Parameter [v]')  
plt.ylabel('Knife-Edge Diffraction Gain [dB]')   

#%%Approximate Solution
v_asol = np.arange(-1,5.1,0.1)      
G_asol = np.zeros(v_asol.size)      

for i in range(0, v_asol.size) :   
    if v_asol[i] >= -1 and v_asol[i] <= 0:   
        G_asol[i] = 20*np.log10(0.5-0.62*v_asol[i])   
    elif v_asol[i] > 0 and v_asol[i] <= 1:      
        G_asol[i] = 20*np.log10(0.5*np.exp(-0.95*v_asol[i]))    
    elif np.all(v_asol[i]>1 and v_asol<=2.4):       
        G_asol[i] = 20*np.log10(0.4-np.sqrt(0.1184-(0.38-0.1*v_asol[i])**2))  
    else:   
        G_asol[i] = 20*np.log10(0.225/v_asol[i])     
        
plt.plot(v_asol, G_asol, label='Approximate Solution')    
plt.legend()         