import numpy as np
import sounddevice as sd

fs = 44100
duration = 10.5  # seconds
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)

sd.default.samplerate = fs
sd.default.channels = 2

myrecording = sd.rec(int(duration * fs))

sd.wait()

myrecording = sd.rec(duration * fs, blocking=True)
myrecording = sd.rec(duration * fs, dtype='float64')