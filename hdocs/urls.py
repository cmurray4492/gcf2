from django.urls import path
from . import views

urlpatterns = [
    path('', views.hdocs, name="hdocs"),
    path('declaration_of_independence', views.declaration_of_independence, name="declaration_of_independence"),
    path('us_constitution', views.us_constitution, name="us_constitution"),
    path('us_bill_of_rights', views.us_bill_of_rights, name="us_bill_of_rights"),
]
