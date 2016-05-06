from numpy import *
import numpy as np

#   Improvement suggestions:
#       - when the segments are ignored there should be a warning containing the corresponding events
#       - make it work with matrixes....

def waves(signal, events, lowerBound, upperBound):
    """
    waves function segments a signal based on the indexes represented by 'events' array, each segment will
    have the size of W = upperBound - lowerBound. The starting point of each segment will be event + lowerBound and
    the ending point will be event + upperBound.
    If the signal is (NxM) matrix (N number of points and M number of channels), than the function will return
    an array with the segmented signal where each position is a matrix (W,M).

    Parameters
    ----------
    signal      - array or matrix (NxM) - N number of points and M number of channels
    events      - array containing the indexes of the event points
    lowerBound  - integer that after summed with the event position will give the index of the signal that represents
                    the first value of respective the segment (if negative will subtract, giving a point previous to
                    the event). Must be lower than the
    upperBound  - integer that after summed with the event position will give the index of the signal that represents the
                    last value of respective the segment

    Returns
    -------
    if signal is an array, than a matrix (ExW), where E is the number of successful events and W is the window size
    (W = higherBound - lowerBound), with the segments of the signal. If the signal is a matrix than a matrix (ExWxM)
    is given (array with (WxM) matrix segments), where M is number of channels. If the segment if out of the boundaries of the signal it will be neglected

    Examples
    --------
    >>> signal = [0,0,0,0,0,1,1,1,1,0,0,0,0]
    >>> waves(signal, [3,5,6,8], -1, 2)
    Out:
        array([[0, 0, 0],
           [0, 1, 1],
           [1, 1, 1],
           [1, 1, 0]])

    >>> signal = array([[0,0,0,0,0,1,1,1,1,0,0,0,0],[1,2,3,4,5,6,7,8,9,10,11,12,13]]).transpose()
    >>> waves(signal, [3,5,6,8], -1, 2)
    Out:
        array([[[ 0,  3],
                [ 0,  4],
                [ 0,  5]],

               [[ 0,  5],
                [ 1,  6],
                [ 1,  7]],

               [[ 1,  6],
                [ 1,  7],
                [ 1,  8]],

               [[ 1,  8],
                [ 1,  9],
                [ 0, 10]]])

    """
    signal = [signal[(center + lowerBound):(center + upperBound)] for center in events]
    return np.array(list(filter(lambda i: (upperBound - lowerBound) == len(i), signal)))