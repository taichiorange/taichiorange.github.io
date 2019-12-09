# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 11:05:11 2019

"""
import numpy as np
import matplotlib.pyplot as plt

Nzc = 839   # for preamble format 0,1,2;
#Nzc = 139  # for preamble format 3

u = 22     # 0---837

n = np.arange(0,Nzc)
exp_e = -np.pi * u * n * (n+1) /Nzc * 1j

Xn = np.exp(exp_e)

# frequency domain, plot
plt.subplot(2,1,1), plt.plot(np.real(Xn),".--")
plt.subplot(2,1,2), plt.plot(np.imag(Xn),".--")