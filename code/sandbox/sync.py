from numpy import *
from pylab import *

def sync(e1, s1, e2, s2, type='timelinear'):
    # type : 'timelinear' - First event vs last
    #        'locally linear' linear inside a sequential set of events
    # spline
    # linear
    # Sync s2 to s1
    # return the new s2


    ti1 = find(diff(e1) == 1)[0]
    tf1 = find(diff(e1) == -1)[-1]

    ti2 = find(diff(e2) == 1)[0]
    tf2 = find(diff(e2) == -1)[-1]


def isync(s1,s2):

    # considering f1 = 1.0 and f2 = f1 * len(s1)/len(s2)  
    t1 = arange( 0, len(s1) )
    t2 = arange( 0, len(s1), len(s1)/float(len(s2)) )

    # TODO test with scipy spline
    return interp(t1, t2, s2)


# signal frequencies
f1 = 1000.0
f2 = 1050.0 #

# signal duration
duration = 100 # 60 seconds

# temporal basis
t1 = arange(0, duration, 1.0/f1)
t2 = arange(0, duration, 1.0/f2)

# Signals out of phase
s1 = sin(2*pi*5*t1)
s2 = sin(2*pi*5*t2)

# Events
e1 = ((t1 % 2) > 1 ) * 1
e2 = ((t2 % 2) > 1 ) * 1

# sync signals
is1 = isync(s1,s2)
is2 = isync(s2,s1)

print(len(is1))
print(sum(abs(s1-is1))/len(s1))


close("all")
# show data

f = figure()
plot(s1,'g', label = "s1")
plot(s2,'r', label = "s2")
title("s1 and s2")
legend()
f.show()

f = figure()
plot(s2, label="s2", color='black' ,lw = 2)
plot(is2, label="is2", color= 'g', alpha = 0.5, lw = 5)
title("s2 and is2")
legend()
f.show()

f = figure()
plot(s2 - is2)
title("s2 - is2")
f.show()