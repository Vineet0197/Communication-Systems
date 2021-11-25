# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 20:58:00 2021

@title: Reflection Models -
        1. Free Space Reflection Model
        2. Two-Ray Reflection Model
@author: Vineet Aggarwal 
"""

import numpy as np 
import matplotlib.pyplot as plt 

#Constant Values for Antenna Parameters 
Pt = int(input("Enter Power of Transmitting Antenna in Watts")) #Transmitted Power in Watts 
Gt = 1      #Transmitting Antenna Unity Gain 
Gr = 1      #Receiving Antenna Unity Gain 
f = int(input("Enter Carrier frequency in MHz"))   #Carrier Frequency (Hz) 
c = 3e8     #Velocity of Light (m/sec) 
lamda = c/f #Wavelength of Wave (m) 

d = np.linspace(100,10000,2000)     #Free Space Distance (m) 

#%%Free Space Reflection Model 
# Formula for Free Space Reflection Model - Received Power in Watts 
Pr = (Pt*Gt*Gr*(lamda**2))/(((4*np.pi)**2)*(d**2))  

Pr_DB = 10*np.log10(Pr)     #ReceivedPower (dB) 
plt.plot(d,Pr_DB,label='Free Space Path Model') 


#%% Two Ray Reflection Model 
ht = int(input("Enter Height of Transmitting Antenna in meters")) #Height of Transmitting Antenna 
hr = float(input("Enter Height of Receiving Antenna in meters")) #Height of Recieving Antenna 
#Formula for Received Power Due to Two-Ray Reflection Model
Pr_tw_ray = (Pt*Gt*Gr*((ht*hr)**2))/(d**4)  #ReceivedPower in Watts
Pr_tw_ray_db = 10*np.log10(Pr_tw_ray)   #Received Power in dB 
plt.plot(d, Pr_tw_ray_db, label='Two Ray Propagation Model') 


#Plot Scaling and Labeling 
plt.grid()          
plt.xscale('log')   
plt.xlabel('Distance [m]')  
plt.ylabel('Received Power [dB]')  
plt.legend()    