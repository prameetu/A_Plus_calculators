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
    
        
def angular_speed(request):

    if request.method == "POST":
        freq = int(request.POST.get('freq'))
        freq_unit = request.POST.get('freq_unit')
        

        initial_freq = freq
        initial_freq_unit = freq_unit

        freq = convert("freq",freq_unit,freq)
        
        ans = 2 * 3.14 * freq
        ans = round(ans,3)



        context_dict = {
            'freq':freq,
            'freq_unit':freq_unit,
            'initial_freq':initial_freq,
            'initial_freq_unit' :initial_freq_unit,
            'ans':ans,
            'id':1
        }
        return render(request,'angular_speed.html',context_dict)
    else:
        return render(request,'angular_speed.html')

