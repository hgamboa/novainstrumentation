from numpy import *
import numpy as np

def waves(signal, events, lowerBound, upperBound):
    signal=[signal[(center+lowerBound):(center+upperBound)] for center in events]
    return np.array(filter(lambda i: len(i)==(upperBound-lowerBound), signal))