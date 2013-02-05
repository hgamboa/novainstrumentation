from numpy import abs, linspace 
import matplotlib.pyplot as plt
import numpy as np
from os import path 

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
    
    
    fs = abs(np.fft(s))
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
    


def load_with_cache(file, recache = False, sampling = 1, columns = None):
    """@brief This function loads a file from the current directory and saves
    the cached file to later executions. It's also possible to make a recache
    or a subsampling of the signal and choose only a few columns of the signal,
    to accelerate the opening process.
    
    @param file String: the name of the file to open.
    @param recache Boolean: indication whether it's done recache or not 
    (default = false).
    @param sampling Integer: the sampling step. if 1, the signal isn't
    sampled (default = 1).
    @param columns Array-Like: the columns to read from the file. if None,
    all columns are considered (default = None).
      
    @return data Array-Like: the data from the file.
    TODO: Should save cache in a different directory
    """   
     
    cfile = '%s.npy' % file
    
    if (not path.exists(cfile)) or recache:
        if columns == None:
            data = np.loadtxt(file)[::sampling, :]
        else:
            data = np.loadtxt(file)[::sampling, columns]
        
        np.save(cfile, data)
        
    else:
        print('Loading with cache...')
        data = np.load(cfile)
    return data

