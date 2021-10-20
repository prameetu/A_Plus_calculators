from django.shortcuts import render
from django.urls.conf import path

# Create your views here.
def convert(val,inp,num):
    if val == 'gauge':
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
    if val == 'atm':
        if inp == 'm/s':
            return num
        elif inp == 'km/h':
            return num*0.2777;
        else:
            return num
        
def abs_pressure(request):

    if request.method == "POST":
        gauge = int(request.POST.get('gauge'))
        atm = int(request.POST.get('atm'))

        ans = atm + gauge
        ans = round(ans,3)



        context_dict = {
            'gauge':gauge,
            'atm':atm,
            'ans':ans,
            'id':1
        }
        return render(request,'absPressure.html',context_dict)
    else:
        return render(request,'absPressure.html')

