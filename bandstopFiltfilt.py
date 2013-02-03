from filtfilt import *
from scipy import signal

def bandstop(s, f1, f2, order = 2, fs = 1000.0):
    b, a = signal.butter(order, [f1/fs, f2/fs], btype = 'bandstop')
    return filtfilt(b, a, s)