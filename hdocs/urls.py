from django.urls import path
from . import views

urlpatterns = [
    path('', views.hdocs, name="hdocs"),
    path('declaration_of_independence', views.declaration_of_independence, name="declaration_of_independence"),
]

#    path('about', views.about, name="about"),
#    path('contactus', views.contactus, name="contactus"),
#   path('usefulinfo', views.usefulinfo, name="usefulinfo"),
