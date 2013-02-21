import novainstrumentation as ni
import numpy as np
import pylab as pl

duration = 30 # in seconds

signal, beats = ni.synthbeats(duration, meanhr = 60, stdhr = 3, samplingfreq = 250)


# TODO INSPECT VECTORS


# TODO ADD NOISE TO SIGNAL HERE

ebeats = np.where( signal == 1.0 )[0]

# TODO IMPROVE BEAT DETECTOR

pl.subplot(2,1,1)
pl.title('HR Report')
pl.plot(np.arange(len(signal))/250.,signal)

pl.subplot(2,1,2)

pl.bar(ebeats[1:]/250., np.diff(ebeats),.8)

# TODO ADD HISTOGRAM OF HR
# TOFO GENERATE PDF
pl.show()


