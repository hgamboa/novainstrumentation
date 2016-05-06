from scipy import *
from scipy import signal
from scikits.talkbox import *

import numpy as np
import scipy as sp
import scipy.signal as sig

def lpcar2cc(ar):
    """

    Parameters
    ----------
    ar

    Returns
    -------

    """
    sh = shape(ar)

    if len(sh) == 1:
        p1 = len(ar)
        nf = 1
        b = zeros(len(ar))
    else:
        p1 = len(ar[0])
        nf = len(ar)
        b = zeros(len(ar[0]))
    p = p1 - 1

    cm = arange(1, p + 1) ** (-1.)

    xm = -arange(1, p + 1)

    b[0] = 1
    cc = []

    for k in range(nf):
        if nf > 1:
            cc += [signal.lfilter(b, ar[k], ar[k, 1:p1] * xm) * cm]
        else:
            cc = signal.lfilter(b, ar, ar[1:p1] * xm) * cm

    return cc


def lpc_coef(s, coefNumber):
    # you have to install scikits.talkbox library before you can use it.

    order = coefNumber - 1

    est, e, k = lpc(s, order)

    return est
