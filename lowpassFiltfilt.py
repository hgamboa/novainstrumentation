from filtfilt import *
from scipy import signal


def lowpass(s, f, order = 2, fs = 1000.0):
    b, a = signal.butter(order, f/fs)
    return filtfilt(b, a, s)

