from django.shortcuts import render
from django.urls.conf import path

# Create your views here.


def ac_dc_calc(request):

    if request.method== 'POST':
        given_data = request.POST.get('given_data')

        if request.POST.get('ac_curr'):
            ac_curr = int(request.POST.get('ac_curr'))
        else:
            ac_curr = None

        if request.POST.get('dc_curr'):
            dc_curr = int(request.POST.get('dc_curr'))
        else:
            dc_curr = None


        if given_data == 'form1' and ac_curr:
            ans = ac_curr * 0.636
            ans = round(ans,3)
            
            cont_dict = {
                'ac_curr' : ac_curr,
                'ans' : ans,
                'given_data':given_data,
                'id':1
            }

            return render(request,'ac_dc_calc.html',cont_dict)

        elif given_data == 'form2' and dc_curr:
            ans = dc_curr / 0.636
            ans = round(ans,3)

            
            cont_dict = {
                'dc_curr' : dc_curr,
                'ans' : ans,
                'given_data':given_data,
                'id':1

            }

            return render(request,'ac_dc_calc.html',cont_dict)
        
        else:
            return render(request, 'ac_dc_calc.html',{'given_data':given_data})
    else:
            return render(request, 'ac_dc_calc.html',{'given_data':'form1'})






