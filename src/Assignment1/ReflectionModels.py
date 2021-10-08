# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 20:58:00 2021

@title: Reflection Models -
        1. Free Space Reflection Model
        2. Two-Ray Reflection Model
@author: Vineet Aggarwal - BITS ID: 2020MT13016
"""

import numpy as np #BITS ID: 2020MT13016
import matplotlib.pyplot as plt #BITS ID: 2020MT13016

#Constant Values for Antenna Parameters - BITS ID: 2020MT13016
Pt = 50     #Transmitted Power in Watts - BITS ID: 2020MT13016
Gt = 1      #Transmitting Antenna Unity Gain - BITS ID: 2020MT13016
Gr = 1      #Receiving Antenna Unity Gain - BITS ID: 2020MT13016
f = 900e6   #Carrier Frequency (Hz) - BITS ID: 2020MT13016
c = 3e8     #Velocity of Light (m/sec) - BITS ID: 2020MT13016
lamda = c/f #Wavelength of Wave (m) - BITS ID: 2020MT13016

d = np.linspace(100,10000,2000)     #Free Space Distance (m) - BITS ID: 2020MT13016

#%%Free Space Reflection Model - BITS ID: 2020MT13016
# Formula for Free Space Reflection Model - Received Power in Watts - BITS ID: 2020MT13016
Pr = (Pt*Gt*Gr*(lamda**2))/(((4*np.pi)**2)*(d**2))  #BITS ID: 2020MT13016

Pr_DB = 10*np.log10(Pr)     #ReceivedPower (dB) - BITS ID: 2020MT13016
plt.plot(d,Pr_DB,label='Free Space Path Model') #BITS ID: 2020MT13016


#%% Two Ray Reflection Model - BITS ID: 2020MT13016
ht = 50     #Height of Transmitting Antenna - BITS ID: 2020MT13016
hr = 1.5    #Height of Recieving Antenna - BITS ID: 2020MT13016
#Formula for Received Power Due to Two-Ray Reflection Model
Pr_tw_ray = (Pt*Gt*Gr*((ht*hr)**2))/(d**4)  #BITS ID: 2020MT13016, ReceivedPower in Watts
Pr_tw_ray_db = 10*np.log10(Pr_tw_ray)   #Received Power in dB - BITS ID: 2020MT13016
plt.plot(d, Pr_tw_ray_db, label='Two Ray Propagation Model') #BITS ID: 2020MT13016


#Plot Scaling and Labeling - BITS ID: 2020MT13016
plt.grid()          #BITS ID: 2020MT13016
plt.xscale('log')   #BITS ID: 2020MT13016
plt.xlabel('Distance [m]')  #BITS ID: 2020MT13016
plt.ylabel('Received Power [dB]')  #BITS ID: 2020MT13016
plt.legend()    #BITS ID: 2020MT13016