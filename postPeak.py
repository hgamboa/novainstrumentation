import numpy as n

def postPeak(V,Vpost):
    """ Detects the next peak """
    return n.array([Vpost[find(Vpost>i)][-1] for i in V])