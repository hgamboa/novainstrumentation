from scipy import signal

def highpass(s, f, order = 2, fs = 1000.0):
    '''
    @brief: for a given signal s rejects (attenuates) the frequencies lower then the cuttof frequency f
    and passes the frequencies higher than that value by applying a Butterworth digital filter
    
    @params:
    
    s: array-like
    signal
    
    f: int
    the cutoff frequency
    
    order: int
    Butterworth filter order
    
    fs: float
    sampling frequency  
    
    @return:
    
    signal: array-like
    filtered signal
    
    '''
    
    b, a=signal.butter(order, f/fs, btype = 'highpass')
    return signal.lfilter(b, a, s)

