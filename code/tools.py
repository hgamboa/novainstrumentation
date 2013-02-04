from numpy import abs, linspace, copy
from scipy import fft
import matplotlib.pyplot as plt
import numpy as np

def plotfft(s, fmax, doplot = True):
    """ This functions computes the fft of a signal, returning the frequency 
    and their magnitude values.
    
    Parameters
    ----------
    s: array-like
      the input signal.
    fmax: int
      the sampling frequency.
    doplot: boolean
      a variable to indicate whether the plot is done or not. 

    Returns
    -------
    f: array-like
      the frequency values (xx axis)
    fs: array-like
      the amplitude of the frequency values (yy axis)
      
    """
    
    
    fs = abs(fft(s))
    f = linspace(0, fmax/2, len(s)/2)
    if doplot:
        plt.plot(f[1:len(s)/2], fs[1:len(s)/2])
    return (f[1:len(s)/2].copy(), fs[1:len(s)/2].copy())


def synthbeats(duration, meanhr= 60, stdhr=1, samplingfreq = 250 ):
    #Minimaly based on the parameters from:
    #http://physionet.cps.unizar.es/physiotools/ecgsyn/Matlab/ecgsyn.m
    #Inputs: duration in seconds
    #Returns: signal, peaks
    
    ibi = 60/float(meanhr)*samplingfreq
    sibi= ibi-60/(float(meanhr)-1)*samplingfreq
    
    peaks=np.arange(0,duration*samplingfreq, ibi )
    
    peaks[1:]=peaks[1:]+np.random.randn(len(peaks)-1)*sibi
    
    if peaks[-1] >= duration*samplingfreq:
        peaks=peaks[:-1]
    
    peaks = peaks.astype('int')
    
    signal = np.zeros(duration*samplingfreq)

    signal[peaks] = 1.0
    
    return signal,peaks
    
