#!/usr/bin/python
# -*- coding: utf-8 -*-

from pylab import rc, close, figure, axes


##########
#Initial configurations
def pylabconfig():

    rc('lines', linewidth=2, color='k')
    #rc('lines', linewidth=1, color='k')

    rc('font', **{'family': 'serif', 'serif': ['Palatino']})
    rc('font', style='italic', size=10)

    rc('text', color='grey')

    #       rc('text', usetex=True)

    rc('text', usetex=False)

    rc('figure', figsize=(8, 5), dpi=80)
    rc('axes', grid=True, edgecolor='grey', labelsize=10,)
    rc('grid', color='grey')
    rc('xtick', color='grey', labelsize=10)
    rc('ytick', color='grey', labelsize=10)

    close('all')


def plotwithhist(t, s, bins=50):
    from matplotlib.ticker import NullFormatter

    nullfmt = NullFormatter()
    figure()
    ax2 = axes([0.125 + 0.5, 0.1, 0.2, 0.8])
    ax1 = axes([0.125, 0.1, 0.5, 0.8])

    ax1.plot(t, s)
    ax1.set_xticks(ax1.get_xticks()[:-1])

    ax2.hist(s, bins, normed=True, facecolor='white',
             orientation='horizontal', lw=2)

    ax2.axis([0, 1, ax1.axis()[2], ax1.axis()[3]])

    ax2.yaxis.set_major_formatter(nullfmt)
    ax2.set_xticks([0, 0.5, 1])

    return ax1, ax2


    ###########

def plotwithstats(t, s):

    from matplotlib.ticker import NullFormatter

    nullfmt = NullFormatter()
    figure()
    ax2 = axes([0.125 + 0.5, 0.1, 0.2, 0.8])

    ax1 = axes([0.125, 0.1, 0.5, 0.8])

    ax1.plot(t, s)
    ax1.set_xticks(ax1.get_xticks()[:-1])

    meanv = s.mean()
    mi = s.min()
    mx = s.max()
    sd = s.std()

    ax2.bar(-0.5, mx - mi, 1, mi, lw=2, color='#f0f0f0')
    ax2.bar(-0.5, sd * 2, 1, meanv - sd, lw=2, color='#c0c0c0')
    ax2.bar(-0.5, 0.2, 1, meanv - 0.1, lw=2, color='#b0b0b0')
    ax2.axis([-1, 1, ax1.axis()[2], ax1.axis()[3]])

    ax2.yaxis.set_major_formatter(nullfmt)
    ax2.set_xticks([])

    return ax1, ax2
