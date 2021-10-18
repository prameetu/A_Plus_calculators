from django.urls import path

from calc import views

urlpatterns = [
    path('ac-dc-calculator/',views.ac_dc_calc,name='ac-dc-calculator')
]