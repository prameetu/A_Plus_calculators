from django.shortcuts import redirect, render
from math import gcd
from django.http import HttpResponse
# Create your views here.


def lcm1(request):
    if request.method == 'POST':
            res1 = int(request.POST['textfield1'])
            res2 = int(request.POST['textfield2'])
            return redirect(f'/lcm-of-{res1}-and-{res2}/')
    else:
        return render(request,'blog/lcm.html')

def lcm_func(request,num1,num2):
    gcf = gcd(int(num1),int(num2))
    ans = int(num1)*int(num2)//gcf
    d = {"ans":ans,"num1":num1,"num2":num2}
    return render(request,'blog/lcm_func.html',context=d)
