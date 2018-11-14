# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 11:25:24 2018

@author: Mingming
"""
import numpy as np
import matplotlib.pyplot as plt 


#%%
################################################################
##################  EDUCATIONAL EXAMPLE ########################
################################################################

"""
FFT EXAMPLE
https://stackoverflow.com/questions/25735153/plotting-a-fast-fourier-transform-in-python

An educational example showing how to use fft to analyze signal in 
frequency domain.
"""
def fftExample():
    from scipy.fftpack import fft
    # Number of samplepoints
    N = 600
    # sample spacing
    T = 1.0 / 800.0
    # Signal in time domain
    x = np.linspace(0.0, N*T, N)
    y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
    
    # Conduct fft and plot the signal as show case
    yf = fft(y)
    xf = np.linspace(0.0, 1.0/(2.0*T), int(N/2))
    plt.figure()
    plt.subplot(2,1,1)
    plt.plot(x, y)
    plt.xlabel('time in s')
    plt.subplot(2,1,2)
    plt.plot(xf, 2.0/N * np.abs(yf[0:int(N/2)]))
    plt.xlabel('frequency')
    plt.grid()
    plt.show()
