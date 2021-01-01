from django.urls import path
from . import views

urlpatterns = [
    path('', views.hdocs, name="hdocs"),
]

#    path('about', views.about, name="about"),
#    path('contactus', views.contactus, name="contactus"),
#   path('usefulinfo', views.usefulinfo, name="usefulinfo"),
