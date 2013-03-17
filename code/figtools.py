#!/usr/bin/python
# -*- coding: utf-8 -*-

from scipy import *
from pylab import *


##########
#Initial configurations

def pylabconfig():

    #    rc('lines',linewidth=2,color='k')
    rc('lines',linewidth=1,color='k')
    
    rc('font',**{'family':'serif','serif':['Palatino']})
    rc('font',style='italic', size=10)
    
    
    rc('text', color='grey')
    
    #       rc('text', usetex=True)
    
    rc('text', usetex=False)
    
    rc('figure', figsize= (8, 5), dpi=80) 
    rc('axes', grid= True, edgecolor= 'grey', labelsize=10,)
    rc('grid', color= 'grey')
    rc('xtick',color= 'grey', labelsize=10)
    rc('ytick',color= 'grey', labelsize=10)
    
    close('all')



def plotwithhist(t,s,bins=50):

    from matplotlib.ticker import NullFormatter
    
    nullfmt=NullFormatter()
    figure()
    ax2=axes([0.125+0.5,0.1,0.2,0.8])
    ax1=axes([0.125,0.1,0.5,0.8])

    ax1.plot(t,s)
    ax1.set_xticks(ax1.get_xticks()[:-1])

    

    ax2.hist(s,bins,normed=True,facecolor='white',orientation='horizontal',lw=2)

    ax2.axis([0,1,ax1.axis()[2],ax1.axis()[3]])

    ax2.yaxis.set_major_formatter(nullfmt)
    ax2.set_xticks([0,0.5,1])
    

    return ax1,ax2


    ###########

def plotwithstats(t,s):


    from matplotlib.ticker import NullFormatter

    nullfmt=NullFormatter()
    figure()
    ax2=axes([0.125+0.5,0.1,0.2,0.8])

    ax1=axes([0.125,0.1,0.5,0.8])
    
    ax1.plot(t,s)        
    ax1.set_xticks(ax1.get_xticks()[:-1])

    meanv=s.mean()
    mi=s.min()
    mx=s.max()
    sd=s.std()




    ax2.bar(-0.5,mx-mi,1,mi,lw=2,color='#f0f0f0')
    ax2.bar(-0.5,sd*2,1,meanv-sd,lw=2,color='#c0c0c0')
    ax2.bar(-0.5,0.2,1,meanv-0.1,lw=2,color='#b0b0b0')
    ax2.axis([-1,1,ax1.axis()[2],ax1.axis()[3]])

    ax2.yaxis.set_major_formatter(nullfmt)
    ax2.set_xticks([])
    



    return ax1,ax2





#########
def syntheticdata():
    figure()
    t = arange(0.0, 8, 0.05)
    l = len (t)
    x = sin(t*2) 
    plot(t, x)
    axis('equal')

    xlabel('tempo (s)',color='grey')
    ylabel('amplitude',color='grey')
    title("Peri\`odico", fontsize=12, color='grey')

    savefigs('sinewave')

    ###########

    #non periodic from emg

    # discrete

    figure()
    xlabel('time (s)',color='grey')
    ylabel('amplitude',color='grey')
    title('Discrete signal', fontsize=12, color='grey')

    plot(t[::4],(x*8).astype('i')[::4],ls='steps')
    
    savefigs('discretesinewave')

def signalsdone():
################ BVP

    [t,s]=load('../data/bvp.txt.gz')

    t=t[:1024]
    s=s-mean(s)
    s=smooth(s[:1024],40)

    figure()
    xlabel('tempo (s)',color='grey')
    ylabel('amplitude',color='grey')
    title("Pulso de press\~{a}o sangu\\'{i}nea", fontsize=12, color='grey')

    plot(t,s)

    savefigs('bvp')
    close()
    
    #ecg clean
    
    [t,s]= load('../data/cleanecg.txt.gz')
    
    figure()
    xlabel('tempo (s)',color='grey')
    ylabel('amplitude (mV)',color='grey')
    title('ECG', fontsize=12, color='grey')
    plot(t,s)
    axis([0,6,-300,300])
    savefigs('cleanecg')
    close()
    
    
    #ecg noisy
    [t,s]= load('../data/noisyecg.txt.gz')
    figure()
    xlabel('tempo (s)',color='grey')
    ylabel('amplitude (mV)',color='grey')
    title('ECG', fontsize=12, color='grey')

    plot(t,s*100)
    axis([0,8,-3,3])
    
    
    savefigs('noisyecg')
    close()
    
    

    #eda noisy
    [t,s]= load('../data/eda.txt.gz')
    figure()
    xlabel('tempo (s)',color='grey')
    ylabel('amplitude (mV)',color='grey')
    #    title('Electrodermal activity', fontsize=12, color='grey')
    title("Actividade electrod\\'{e}rmica", fontsize=12, color='grey')

    plot(t,s)
    axis([0,40,0,1200])
    
    
    savefigs('eda')
    #close()
    
    

    
    #xyz

    #xyz cal
    [t,x,y,z]= load('../data/xyzcal.txt.gz')
    figure()
    xlabel('time (s)',color='grey')
    ylabel('amplitude (mV)',color='grey')
    title("Aceler\\'{o}metro", fontsize=12, color='grey')
    
    ix=arange(len(t))
    ix=ix[::10]
    plot(t[ix],smooth(x[ix]))
    plot(t[ix],smooth(y[ix]),'--',color='k')
    plot(t[ix],smooth(z[ix]),'-.',color='k')
    axis([0,25,400,1200])
    legend(('x','y','z'))
           
    savefigs('xyzcal')


    #xyz 5 steps and fall
    
    [t,x,y,z]= load('../data/xyz.txt.gz')
    figure()
    xlabel('time (s)',color='grey')
    ylabel('acelera\c{c}\~{a}o ($N/s^2$)',color='grey')
    #    title('Electrodermal activity', fontsize=12, color='grey')
    title("Aceler\\'{o}metro", fontsize=12, color='grey')
    
    ix=arange(len(t))
    ix=ix[::1]
    plot(t[ix],smooth(x[ix],3))
    plot(t[ix],smooth(y[ix],3),'--',color='k')
    plot(t[ix],smooth(z[ix],3),'-.',color='k')
    axis([0,8,-4,4])
    legend(('x','y','z'))
           
    savefigs('xyzsteps')


   #respirataion 
    [t,s]= load('../data/resp.txt.gz')
    figure()
    xlabel('time (s)',color='grey')
    ylabel('amplitude (mV)',color='grey')
    #    title('Electrodermal activity', fontsize=12, color='grey')
    title(u'Respira\c{c}\~{a}o', fontsize=12, color='grey')

    plot(t,s)
    axis([0,30,700,900])
    
    
    savefigs('resp')




    #force
    [t,s]= load('../data/force.txt.gz')
    figure()
    xlabel('tempo (s)',color='grey')
    ylabel('amplitude (mV)',color='grey')
    
    title(u'For\c{c}a', fontsize=12, color='grey')

    plot(t[::20],s[::20])
    
    
    savefigs('forca')
#    close()
    #emg

  
    
        
    [t,s]= load('../data/emg.txt.gz')
    figure()
    xlabel('time (s)',color='grey')
    ylabel('amplitude (mV)',color='grey')
    
    title('Electromiografia', fontsize=12, color='grey')

    plot(t[::2],s[::2])
    
    
    savefigs('emg')
    close()
    
    figure()
    
    
    ax1,ax2=plotwithstats(t[::10],s[::10])
    title("Caracter\\'{i}sticas estat\\'{i}sticas de um sinal de EMG")
    xlabel('tempo (s)',color='grey')
    ylabel('amplitude (mV)',color='grey')
    savefigs('statsemg')
    
    
    close()
    figure()
    ax1,ax2=plotwithhist(t[::10],s[::10])
    ax1.set_axes(ax1)
    title("Sinal de EMG com histograma")
    xlabel('tempo (s)',color='grey')
    ylabel('amplitude (mV)',color='grey')
    savefigs('histsemg')
    
    
    
    

    
    #switch
    
    [t,s]= load('../data/switch.txt.gz')
    figure()
    xlabel('tempo (s)',color='grey')
    ylabel('amplitude (mV)',color='grey')
    #    title('Electrodermal activity', fontsize=12, color='grey')
    title('Interruptor', fontsize=12, color='grey')

    plot(t,s)
    axis([0,1,0,5000])
    
    
    savefigs('switch')
    close()
    
def signalsdoing():
    figure()
    subplot(331)
    
    t = arange(0.0, 8, 0.05)
    l = len (t)
    x1 = sin(t*2) 
    plot(t, x1)
    axis('equal')
    axis((0,8,-2,2)) 

    subplot(332)
    x2 = sin(t*2*4+2)*0.6
    plot(t, x2)
    axis((0,8,-2,2)) 
     
    subplot(333)
    x3 = sin(t*2*15-243)*0.3

    plot(t, x3)
    axis((0,8,-2,2))     
    show()
    
    subplot(335)
    s=x1+x2+x3

    
    
    plot(t, s)
    axis((0,8,-2,2))     
    show()
    
    
    subplot(337)
    plot(t,lowpass(s,30,4))
    axis((0,8,-2,2))    
    

    subplot(338)
    plot(t,bandpass(s,30*2,100*2,4))
    axis((0,8,-2,2))     

    subplot(339)
    plot(t,highpass(s,100*2,4))
    axis((0,8,-2,2))    
        
    savefigs('addsin')
    
    
    
    figure()
    
    subplot(212)
    plotfft(s,20)
    xlabel('frequ\^{e}ncia (Hz)',color='grey')

    
    subplot(211)
    plot(t,s)

    xlabel('tempo (s)',color='grey')
    
    savefigs('addsinfft')
    return s
        
    
    
def freqgraphs():
    
    from matplotlib.ticker import NullFormatter
    
    
    t = arange(0.0, 8, 0.05)
    l = len (t)
    x1 = sin(t*2) 
    
    nullfmt=NullFormatter()
    
    random.seed(230)
    
    figure()
    vx=[]
    
    for i in range(10):
        v=sin(t*rand(1)*80+rand(1)*150)*rand(1)
        vx+=[v]
        ax=subplot(11,1,i+1)
        ax.yaxis.set_major_formatter(nullfmt)
        ax.xaxis.set_major_formatter(nullfmt)
  
        plot(t,v,color='grey')
        axis((0,8,-3,3))
        
    ax=subplot(11,1,11)
    ax.yaxis.set_major_formatter(nullfmt)  
#    ax.xaxis.set_major_formatter(nullfmt)  
    vx=array(vx)
    plot(t,vx.sum(0))
    axis((0,8,-3,3))
    savefigs('sumsin')
    
    
    figure()
    plotfft(vx.sum(0),1000)
    ylabel('amplitude',color='grey')
    xlabel('frequ\^{e}ncia (Hz)',color='grey')
    savefigs('fft')
    
    
    
    
    
    #SQUARE wave
    figure()
    
    xx=sign(x1)
    
    subplot(4,2,1)
    plot(t,xx)
    f=fft(xx)
    axis((0,8,-1.2,1.2))
    subplot(4,2,2)
    plotfft(xx,1000)

    subplot(4,2,3)
    f[50:750]=0
    plot(t,ifft(f))
    axis((0,8,-1.2,1.2))
    subplot(4,2,4)
    plotfft(ifft(f),1000)
    

    subplot(4,2,5)
    f[20:780]=0
    plot(t,ifft(f))
    axis((0,8,-1.2,1.2))
    subplot(4,2,6)
    plotfft(ifft(f),1000)


    subplot(4,2,7)
    f[5:795]=0
    plot(t,ifft(f))
    axis((0,8,-1.2,1.2))
    subplot(4,2,8)
    plotfft(ifft(f),1000)

    savefigs('squarewave')    
    
    
def stats():
    return
    #ecg + hist
    figure()
    plotwithhist(arange(100),randn(100),bins=20)
    
    figure()
    plotwithstats(arange(100),randn(100))


def noise():
    ###########


    figure()
    t = arange(0.0, 8, 0.05)
    l = len (t)
    x=randn(l)*.5+4
    plot(t,x)
    axis([0,8,-10,10])

    xlabel('tempo (s)',color='grey')
    ylabel('amplitude',color='grey')
    title('$\mu = 4$, $\sigma = \\frac{1}{2}$', fontsize=14, color='grey')

    savefigs('noise1')

    #######

    figure()
    t = arange(0.0, 8, 0.05)
    x=randn(l)*2
    plot(t,x)

    axis([0,8,-10,10])
    xlabel('tempo (s)',color='grey')
    ylabel('amplitude',color='grey')
    title('$\mu = 0, \sigma = 2$', fontsize=14, color='grey')

    savefigs('noise2')

    figure()
    
    s=randn(1000)
    
    s[380:385]=s[380:385]+sin(arange(380,385)/2)*20
    
    s=s+sin(arange(len(s))/200)
    
    plot(s[300:450])
    xlabel('tempo (s)',color='grey')

    savefigs('noisesample')
    show()

def processing():
    #derivative
    pass

def applications():
    #Linear regression
    
    #Linear regression example
    # This is a very simple example of using two scipy tools 
    # for linear regression, polyfit and stats.linregress
    
    #Sample data creation
    #number of points 
    n=50
    t=linspace(-5,5,n)
    #parameters
    a=0.8; b=-4
    x=polyval([a,b],t)
    #add some noise
    xn=x+randn(n)
    
    #Linear regressison -polyfit - polyfit can be used other orders polys
    (ar,br)=polyfit(t,xn,1)
    xr=polyval([ar,br],t)
    #compute the mean square error
    err=sqrt(sum((xr-xn)**2)/n)
    
    #print('Linear regression using polyfit')
    #print('parameters: a=%.2f b=%.2f \nregression: a=%.2f b=%.2f, ms error= %.3f' % (a,b,ar,br,err))
    
    #matplotlib ploting
    title('Regress\~{a}o linear')
    plot(t,x,'k--')
    plot(t,xn,'k.')
    plot(t,xr,'k-.')
    legend(['original',"com ru\\'{i}do", 'regression'])

    
    #interpolation up and down
    pass

if __name__ == '__main__':
    pylabconfig()
    syntheticdata()
    freqgraphs()
    signalsdone()
    signalsdoing()
#    stats()
#    noise()
#    processing()
#    applications()
    noise()
    show()
