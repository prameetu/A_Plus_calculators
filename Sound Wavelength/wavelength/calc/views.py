from django.shortcuts import render
from django.urls.conf import path

# Create your views here.
def convert(val,inp,num):
    if val == 'freq':
        if inp == 'Hz':
            return num
        elif inp == 'kHz':
            return num*1000
        elif inp == 'MHz':
            return num*1000000
        elif inp == 'GHz':
            return num*1000000000
        else:
            return num
    if val == 'vel':
        if inp == 'm/s':
            return num
        elif inp == 'km/h':
            return num*0.2777;
        else:
            return num
        
def sound_wavelength(request):

    if request.method == "POST":
        print("POSt")
        freq = int(request.POST.get('freq'))
        freq_unit = request.POST.get('freq_unit')
        vel = int(request.POST.get('vel'))
        vel_unit = request.POST.get('vel_unit')

        initial_freq = freq
        initial_vel = vel
        initial_freq_unit = freq_unit
        initial_vel_unit = vel_unit

        freq = convert("freq",freq_unit,freq)
        vel = convert("vel",vel_unit,vel)

        wavelength = vel/freq
        wavelength = round(wavelength,3)



        context_dict = {
            'freq':freq,
            'vel':vel,
            'freq_unit':freq_unit,
            'vel_unit':vel_unit,
            'initial_freq':initial_freq,
            'initial_vel':initial_vel,
            'initial_freq_unit' :initial_freq_unit,
            'initial_vel_unit':initial_vel_unit,
            'wavelength':wavelength,
            'id':1
        }
        return render(request,'wavelengthCalc.html',context_dict)
    else:
        return render(request,'wavelengthCalc.html')

