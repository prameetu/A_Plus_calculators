from django.urls import path

from calc import views

urlpatterns = [
    path('absolute-pressure/',views.abs_pressure,name='absolute-pressure')
]