from scipy import signal

def filterhum50(s):


    hum_notch50 = array([0.95, 1.05])*Hz(50)
    hum_notch100 = hum_notch50*2



    [b,a] = signal.butter(filter_order, hum_notch50, btype="bandstop")
    fdata = signal.lfilter(b, a, s)

    [b,a] = signal.butter(filter_order, hum_notch100, btype="bandstop")
    fdata = signal.lfilter(b, a, fdata)
    return fdata