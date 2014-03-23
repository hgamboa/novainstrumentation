from numpy import std

def stdwave(signal):
    """ This function computes the standard deviation error wave of various 
    signals.
    
    Given a set of signals, with the same number of samples, this function 
    returns an array representative of the error wave of those signals - which 
    is a wave computed with the standard deviation error values of each signal's
    samples. 
    
    Parameters
    ----------
    signals: matrix-like
      the input signals.

    Returns
    -------
    stdw: array-like
      the resulting error wave.  
    """    
    return std(signal,0)
