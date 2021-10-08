# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 21:44:23 2021

@title: Diffraction Gain - Knife Edge Diffraction Gain
@author: Vineet Aggarwal - BITS ID: 2020MT13016
"""

import numpy as np #BITS ID: 2020MT13016
import scipy.special as sc  #BITS ID: 2020MT13016
import matplotlib.pyplot as plt   #BITS ID: 2020MT13016


v = np.arange(-3,5.1,0.1)    #BITS ID: 2020MT13016

T2_A, T1_A = sc.fresnel(np.inf)     #BITS ID: 2020MT13016
T2_B, T1_B = sc.fresnel(v)          #BITS ID: 2020MT13016

T1 = T1_A*np.ones(v.size)-T1_B      #BITS ID: 2020MT13016
T2 = T2_A*np.ones(v.size)-T2_B      #BITS ID: 2020MT13016

MI = T1-1j*T2               #BITS ID: 2020MT13016
Fv = 0.5*(1+1j)*MI          #BITS ID: 2020MT13016
Gd = 20*np.log10(np.abs(Fv))  #BITS ID: 2020MT13016
plt.plot(v, Gd, label='Exact Solution')   #BITS ID: 2020MT13016
plt.grid()                  #BITS ID: 2020MT13016
plt.xlim(-3, 5)             #BITS ID: 2020MT13016
plt.ylim(-30,5)             #BITS ID: 2020MT13016
plt.xlabel('Fresnal Diffraction Parameter [v]')  #BITS ID: 2020MT13016
plt.ylabel('Knife-Edge Diffraction Gain [dB]')   #BITS ID: 2020MT13016

#%%Approximate Solution
v_asol = np.arange(-1,5.1,0.1)      #BITS ID: 2020MT13016
G_asol = np.zeros(v_asol.size)      #BITS ID: 2020MT13016

for i in range(0, v_asol.size) :   #BITS ID: 2020MT13016
    if v_asol[i] >= -1 and v_asol[i] <= 0:   #BITS ID: 2020MT13016
        G_asol[i] = 20*np.log10(0.5-0.62*v_asol[i])   #BITS ID: 2020MT13016
    elif v_asol[i] > 0 and v_asol[i] <= 1:      #BITS ID: 2020MT13016
        G_asol[i] = 20*np.log10(0.5*np.exp(-0.95*v_asol[i]))    #BITS ID: 2020MT13016
    elif np.all(v_asol[i]>1 and v_asol<=2.4):       #BITS ID: 2020MT13016
        G_asol[i] = 20*np.log10(0.4-np.sqrt(0.1184-(0.38-0.1*v_asol[i])**2))  #BITS ID: 2020MT13016
    else:   #BITS ID: 2020MT13016
        G_asol[i] = 20*np.log10(0.225/v_asol[i])     #BITS ID: 2020MT13016
        
plt.plot(v_asol, G_asol, label='Approximate Solution')    #BITS ID: 2020MT13016
plt.legend()         #BITS ID: 2020MT13016