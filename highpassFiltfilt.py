from filtfilt import *
from scipy import signal


def highpass(s, f, order = 2, fs = 1000.0):
    b, a=signal.butter(order, f/fs, btype = 'highpass')
    return filtfilt(b, a, s)

