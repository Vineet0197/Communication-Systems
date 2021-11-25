# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 11:40:20 2021

@author: Vineet Aggarwal
"""

import matplotlib.pylab as plt
import numpy as num

a = 4
f = 3

t = num.arange(0,2,0.02) # for a total of 16 samples
# %generation of an impulse signal
x1=[]
for i in range(len(t)):
    x1.append(1)
x2 = a*num.sin(2*num.pi*f*t)# %generation of sine wave
y = x1*x2; #modulation step
    
#for impulse signal plot
plt.stem(t,x1);
plt.title('Impulse Signal');
plt.xlabel('Time');
plt.ylabel('Amplitude ');
plt.grid(True)
plt.show()

#for sine wave plot
plt.plot(t,x2); 
plt.title('Sine Wave');
plt.xlabel('Time ');
plt.ylabel('Amplitude ');
plt.grid(True)
plt.show()

#for PAM wave plot
plt.stem(t,y);
plt.title('PAM Wave');
plt.xlabel('Time');
plt.ylabel('Amplitude');
plt.grid(True)
plt.show()