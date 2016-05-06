from pylab import *
from numpy import *
from novainstrumentation.code.waves.waves import waves
from novainstrumentation.code.waves.meanwave import meanwave
import os


def plotheatmap( signal, events,lmin=0,lmax=0,dt=0.01,color='r'):
    w=waves(signal, events, lmin, lmax)
    w_=meanwave(w)
   # ws_=stdwave(w)
    t_=(arange(len(w_))+lmin)*dt
    
    for iw in w:
        plot(t_,iw,lw=3,alpha=.15,color=color) 

    plot(t_,w_,lw=2,color='k')
    #plot(t_,w_+ws_,lw=0.5,color='k',ls='--')
    #plot(t_,w_-ws_,lw=<0.5,color='k',ls='--')

path = '..' + os.path.sep + 'data' + os.path.sep
t, s = loadtxt(path + 'cleanecg.txt')
pr = array([20, 87, 156, 225, 291, 355, 418, 482, 550, 624, 694, 764, 834, 905, 978])

plotheatmap(s,pr, -10, 30)