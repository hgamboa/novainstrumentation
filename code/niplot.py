from pylab import axis, draw, close, gcf
from novainstrumentation import *


def on_key_press(event):

    if event.key == '+':
        a = axis()
        w = a[1] - a[0]
        axis([a[0] + w * .2, a[1] - w * .2, a[2], a[3]])
        draw()

    if event.key in ['-', '\'']:
        a = axis()
        w = a[1] - a[0]
        axis([a[0] - w / 3.0, a[1] + w / 3.0, a[2], a[3]])
        draw()

    if event.key == '.':
        a = axis()
        w = a[1] - a[0]
        axis([a[0] + w * .2, a[1] + w * .2, a[2], a[3]])
        draw()

    if event.key == ',':
        a = axis()
        w = a[1] - a[0]
        axis([a[0] - w * .2, a[1] - w * .2, a[2], a[3]])
        draw()

    if event.key == 'q':
        close()
        #TODO: We should make the disconnect (mpl_disconect(cid)
        #But since the figure is destroyed we may keep this format
        # if implemented the mpl_connect should use the return cid

    #print('you pressed', event.key, event.xdata, event.ydata)


def on_key_release(event):
    #print('you released', event.key, event.xdata, event.ydata)
    pass


def niplot():
    fig = gcf()
    cid = fig.canvas.mpl_connect('key_press_event',  # @UnusedVariable
                                 on_key_press)
    cid = fig.canvas.mpl_connect('key_release_event',  # @UnusedVariable
                                 on_key_release)
