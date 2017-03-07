import novainstrumentation as ni
import numpy as np
from numpy import *
import pylab as pl

from novainstrumentation.code.sandbox.wfdbtools import rdsamp, rdann, plot_data
#from pprint import pprint
    
    # Record is a format 212 record from physiobank.
    # Note that name of record does not include extension.
record = '100'

    # Read in the data from 0 to 10 seconds
data, info = rdsamp(record, 0, 10)
    
    # returned data is an array. The columns are time(samples),
    # time(seconds), signal1, signal2
print(data.shape)

    # info is a dictionary containing header information
print(info)
#    {'first_values': [995, 1011],
#    'gains': [200, 200],
#    'samp_count': 650000,
#    'samp_freq': 360,
#    'signal_names': ['MLII', 'V5'],
#    'zero_values': [1024, 1024]}
    
ann = rdann(record, 'atr', 0, 10)

print(ann[:4,:])
#       array([[  18.   ,    0.05 ,   28.   ],
#              [  77.   ,    0.214,    1.   ],
#              [ 370.   ,    1.028,    1.   ],
#              [ 662.   ,    1.839,    1.   ]])
#    
    
    # Plot the data and the mark the annotations
#plot_data(data, info, ann)


s = data[936+100:1222+100,2]

duration = 30 # in seconds

signal, beats = ni.synthbeats(duration, meanhr = 60, stdhr = 3, samplingfreq = 500)

time = np.arange(len(signal))/250.

ns=np.convolve(signal,s+0.4)


s=ns+pl.randn(len(ns))*0.01

s = s+sin(arange(len(ns))/1000.+pl.randn(len(ns))/5.)*.1



pl.plot(s)



pl.draw()
#pl.show()

