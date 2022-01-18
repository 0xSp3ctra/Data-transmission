import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fttpack import ftt
import numpy as np
plt.close('all')

fs = 16000
d = 3

print("Start recording")

a = sd.rec(int(d * fs), fs, 1, blocking=True)

print("End recording")

sd.play(a, fs)
plt.plot(a); plt.title("Recorded sound")

# spectre
x_t = fft(a)

# axes de fréquence
x_f = np.size(a)
fr = (Fs / 2) * np.linspace(0, 1, round(n/2))
X_m = (2 / n) * abs(X_f([0,np.size(fr)]))

# figure du spectre
plt.figure()
plt.plot(fr, X_m)
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Magnitude")
plt.title(Spectre)


