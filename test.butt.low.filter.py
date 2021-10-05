#moduli utili:
import tkinter as tk
from tkinter import ttk,messagebox
from tkinter import filedialog as fd 
from tkinter.constants import SUNKEN #per bordo label
from tkinter.messagebox import showinfo
from numpy import ceil, log2 #per finestre di dialogo
import pandas as pd #per grafico
#per grafico:
import numpy as np #per grafico
from numpy import* #per grafico
import matplotlib.pyplot as plt #per grafico 
from scipy.signal import butter, lfilter,filtfilt #per filtraggio
from scipy.fft import fft,fftfreq    #per fourier
import math


# #NORMALE:
def butter_bandpass(lowcut, highcut, fs, order=3):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band', analog=False)
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=3):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

order = 3
fs = 800       
lowcut = 0.1
highcut = 40
filename = fd.askopenfilename(
    title='Open a file',
    initialdir='/')
y_temp = pd.read_csv(filename,  skiprows = 1, sep = ',',  header=None)
data=y_temp[2]
t = np.arange(0,len(data)/800,1/800)
T = 1/800             
n = int(T * fs)     
y = butter_bandpass_filter(data, lowcut,highcut, fs, order)
plt.plot(t, data, 'b-', label='data')
plt.plot(t, y, 'g-', linewidth=2, label='filtered data')
plt.xlabel('Time [sec]')
plt.grid()
plt.legend()
plt.show()


# #CON FOURIER:

# order=3
# fs = 800       
# lowcut = 0.1
# highcut = 40
# filename = fd.askopenfilename(
#     title='Open a file',
#     initialdir='/')
# y_temp = pd.read_csv(filename,  skiprows = 1, sep = ',',  header=None)
# data=y_temp[2]
# T = 1/800             
# n = int(T * fs) 
# N = len(data)
# T = 1.0 / 800
# media=mean(data)
# ordinata_y_filtrata_media=data-media

# n=log2(len(ordinata_y_filtrata_media))
# n=math.ceil(n)

# y = np.append(ordinata_y_filtrata_media, np.repeat(0,(pow(2,n))-N))
# yorig = fft(y)

# yf = butter_bandpass_filter(y, lowcut, highcut, fs, order)
# yfourier = fft(yf)

# N = pow(2, n)
# xf = fftfreq(N, T)[:N//2]

# plt.plot(xf, 2.0/N * np.abs(yorig[0:N//2]))
# plt.plot(xf, 2.0/N * np.abs(yfourier[0:N//2]))
# plt.show()