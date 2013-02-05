from pylab import *
from novainstrumentation import *


def on_key_press(event):
    
    if event.key == '+':
        a=axis()
        w=a[1]-a[0]
        axis([a[0]+w*.2,a[1]-w*.2,a[2], a[3] ] )
        draw()

    if event.key in ['-', '\'']:
        a=axis()
        w=a[1]-a[0]
        axis([a[0]-w/3.0,a[1]+w/3.0,a[2], a[3] ] )
        draw()

    if event.key == '.':
        a=axis()
        w=a[1]-a[0]
        axis([a[0]+w*.2,a[1]+w*.2,a[2], a[3] ] )
        draw()
        
    if event.key == ',':
        a=axis()
        w=a[1]-a[0]
        axis([a[0]-w*.2,a[1]-w*.2,a[2], a[3] ] )
        draw()

    if event.key == 'q':
        close()
        
    #print('you pressed', event.key, event.xdata, event.ydata)


def on_key_release(event):
    #print('you released', event.key, event.xdata, event.ydata)
    pass

def niplot():
    fig = gcf()
    cid = fig.canvas.mpl_connect('key_press_event', on_key_press)
    cid = fig.canvas.mpl_connect('key_release_event', on_key_release)


