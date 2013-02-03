import numpy as n

def priorPeak(V,Vprior):
    """ Detects the previous peak """
    return n.array([Vprior[find(Vprior<i)][-1] for i in V])