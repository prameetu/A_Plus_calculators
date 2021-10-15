from django.urls import path

from calc import views

urlpatterns = [
    path('sound-wavelength/',views.sound_wavelength,name='sound-wavelength')
]