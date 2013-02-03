from scipy import signal

def bandpass(s, f1, f2, order = 2, fs = 1000.0):
    '''
    @brief: for a given signal s passes the frequencies within a certain range (between f1 and f2)
    and rejects (attenuates) the frequencies outside that range by applying a Butterworth digital filter
    
    @params:
    
    s: array-like
    signal
    
    f1: int
    the lower cutoff frequency
    
    f2: int
    the upper cutoff frequency
    
    order: int
    Butterworth filter order
    
    fs: float
    sampling frequency  
    
    @return:
    
    signal: array-like
    filtered signal
    
    '''
    b, a = signal.butter(order, [f1/fs, f2/fs], btype = 'bandpass')
    return signal.lfilter(b, a, s)