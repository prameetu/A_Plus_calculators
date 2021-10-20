from django.urls import path

from calc import views

urlpatterns = [
    path('angular-speed/',views.angular_speed,name='angular-speed')
]
