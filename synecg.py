import numpy as np

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
    
    
    
signal, peaks = synthbeats(10)

