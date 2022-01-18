import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft
import numpy as np
plt.close('all')
ax = plt.axes()

fs = 44100
d = 5

print("Start recording")

a = sd.rec(int(d * fs), fs, 1, blocking=True)
# Useless
a = a.flatten()
#
print(a)

print("End recording")

plt.plot(a)
plt.title("Recorded sound")

X_f = fft(a)

ax.set_xlabel('Temps (s)')
ax.set_ylabel('Amplitude')

n = np.size(a)
fr = (fs / 2) * np.linspace(0, 1, round(n/2))
X_m = (2 / n) * abs(X_f[0:np.size(fr)])
plt.show()
