from numpy import diff, sign, array
from pylab import find
import doctest

def peaks(signal, tol = None):
    """ This function detects all the peaks of a signal and returns those time
    positions. To reduce the amount of peaks detected, a threshold is introduced
    so only the peaks above that value are considered. 
    
    Parameters
    ----------
    x: array-like
     the signal with the peaks to detect.
    tol: int
      the threshold used to limit the peak detection. in case none is given, the
      value used is the minimum of the signal (detection of peaks in all signal) 

    Returns
    -------
    peaks: array-like
      the time sample where the peak occurs. 
        
    Example
    -------
    >>> peaks([1,2,4,3,2,5,7,7,4,9,2])
    array([2, 9])
    >>> peaks([1,2,-4,-3,-5,4,5])
    array([1, 3])
    >>> peaks([1,-4,-3,4,5],0)
    array([], dtype=int32)
    """
    
    if (tol == None):
        tol = min(signal)
    signal[signal < tol] = 0     

    return find((diff(sign(diff(signal)))) == -2) + 1


def postPeak(V,Vpost):
    """ Detects the next peak """
    return array([Vpost[find(Vpost>i)][-1] for i in V])




def priorPeak(V,Vprior):
    """ Detects the previous peak """
    return array([Vprior[find(Vprior<i)][-1] for i in V])

