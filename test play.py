import numpy as np
import sounddevice as sd
from math import pi

fs = 41000

data = np.arange(0, 5, 1/fs)

f = 650


x = np.sin(2*pi*f*data)

sd.play(x, fs, blocking=True)

