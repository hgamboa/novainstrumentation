import novainstrumentation as ni
import numpy as np
import pylab as pl

duration = 30  # in seconds

time, signal, beats = ni.synthbeats(duration, meanhr=60, stdhr=3, samplingfreq=250)


# TODO INSPECT VECTORS WITH print
# TODO ADD NOISE TO SIGNAL HERE WITH pl.randn


# TODO IMPROVE BEAT DETECTOR
ebeats = pl.find(signal == 1.0)


# Plotting part
pl.subplot(2, 1, 1)
pl.title('HR Report')
pl.plot(time, signal)

pl.subplot(2, 1, 2)

pl.bar(ebeats[1:] / 250., np.diff(ebeats), .8)

# TODO ADD HISTOGRAM OF HR pl.hist

# TODO GENERATE PDF WITH pl.savefig
pl.show()
