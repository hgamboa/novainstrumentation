from numpy import abs, linspace, copy
from scipy import fft
import matplotlib.pyplot as plt

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
