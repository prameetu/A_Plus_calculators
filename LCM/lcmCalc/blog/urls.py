from blog import views
from django.urls import path



urlpatterns = [
    path('',views.lcm1,name='lcm1'),
    path('lcm-of-<str:num1>-and-<str:num2>/',views.lcm_func,name='lcm_func')
]