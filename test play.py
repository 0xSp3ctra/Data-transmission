import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
A = 0.5 #amplitude
f = 1000 #fréquence
fs = 100000 #échantillonage
t = np.arange(0, 10, 1/fs) #temps

signal = A * np.cos(f * 2 * np.pi * t) #sign
    
fig = plt.figure(figsize=(12, 6))
ax = plt.axes()
ax.plot(t,signal)
plt.xlim(0, 0.003)

stockSignal = np.array(signal)
sd.play(stockSignal, fs, loop=True)
