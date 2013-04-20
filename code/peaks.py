"""
novainstrumentation

peak finding module
"""

from numpy import array, clip, argsort, sort
from pylab import find
from scipy.signal import argrelmax


def peaks(signal, tol=None):
    """ This function detects all the peaks of a signal and returns those time
    positions. To reduce the amount of peaks detected, a threshold is
    introduced so only the peaks above that value are considered.

    Parameters
    ----------
    x: array-like
     the signal with the peaks to detect.
    tol: int
      the threshold used to limit the peak detection. in case none is given,
      the value used is the minimum of the signal (detection of peaks in all
      signal)

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

    if (tol is None):
        tol = min(signal)
    pks = argrelmax(clip(signal, tol, signal.max()))
    return pks[0]


def post_peak(v, v_post):
    """ Detects the next peak """
    return array([v_post[find(v_post > i)[0]] for i in v])


def prior_peak(v, v_prior):
    """ Detects the previous peak """
    return array([v_prior[find(v_prior < i)[-1]] for i in v])


def clean_near_peaks(signal, peaks_, min_distance):
    """ Given an array with all the peaks of the signal ('peaks') and a
    distance value ('min_distance') and the signal, by argument, this function
    erases all the unnecessary peaks and returns an array with only the maximum
    peak for each period of the signal (the period is given by the
    min_distance).

    Parameters
    ----------
    signal: array-like
      the original signal.
    peaks: array-like
      the peaks to filter.
    min_distance: int
      the distance value to exclude the unnecessary peaks.

    Returns
    -------
    fp: array-like
      the new peaks, after filtering just the maximum peak per period.

    See also: clean_near_events()
    """

    #order all peaks
    ars = argsort(signal[peaks])
    pp = peaks[ars]

    fp = []

    #clean near peaks
    while len(pp) > 0:
        fp += [pp[-1]]
        pp = pp[abs(pp - pp[-1]) > min_distance]

    return sort(array(fp))


def clean_near_events(points, min_distance):
    """ Given an array with some specific points of the signal and a distance
    value, this function erases all the surplus points and returns an array
    with only one point (the first point) per distance samples values

    Parameters
    ----------
    points: array-like
      the events to filter.
    min_distance: int
      the distance value to exclude the unnecessary events.

    Returns
    -------
    fp: array-like
      the new events, after filtering just one per period.
    Example
    -------
    >>> clean_near_events([1,3,5,50,65,68,83,88],10)
    array([ 1, 50, 65, 83])

    See also: clean_near_peaks()
    """

    fp = []
    points = array(points)
    while len(points) > 0:
        fp += [points[0]]
        points = points[abs(points - points[0]) > min_distance]

    return array(fp)
