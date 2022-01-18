#Import des librairies

import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft
import numpy as np

fs = 100000 #Échantillonnage
d = 5 #Temps de réception

print("Start recording")

a = sd.rec(int(d * fs), samplerate=fs, channels=1) #Réception du signal (fréquence de 1000)
sd.wait()

print("End recording")

plt.figure(figsize=(12,6)) #Taille de la figure

ax = plt.axes()
plt.xlim(80000,80300)

ax.plot(a)

ax.set_xlabel("Temps (s)")
ax.set_ylabel("Amplitude")

amplitude = (np.max(a) - np.min(a))/2
print(amplitude)

motifs = 0
for i in range(len(a[:-1])):
    if a[i] < 0 and a[i + 1] > 0:
        motifs +=1
        
periode = d/motifs
frequence = 1/periode
print("frequence :", frequence, "amplitude :", amplitude)

