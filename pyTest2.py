# C:\GitHub\test2\pyTest2.py
# https://github.com/htylab/SS_EXP 

import matplotlib.pyplot as plt 
import numpy as np 

fs = 100 
t = np.arange(0, 1, 1/fs) 
y = np.cos( 2 * np.pi * 10 * t) 

plt.figure(figsize = [10, 5]) 

plt.plot(t, y) 
plt.title('Signal plot') 
plt.show() 

yf = np.fft.fft(y) 
w_hat = np.arange(0, 2 * np.pi, 2 * np.pi / fs) 

plt.figure(figsize=[15, 5]) 

plt.subplot(121) 
plt.plot(w_hat, abs(yf)) 
plt.xlabel(r'$\hat\omega$ (radian)') 
plt.title('The magnitude spectrum') 

plt.subplot(122) 
plt.plot(np.angle(yf)) 
plt.xlabel(r'$\hat\omega$ (radian)') 
plt.title('The phase spectrum') 

plt.show()
