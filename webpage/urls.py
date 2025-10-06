from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bmi', views.bmi, name='bmi'),
    path('nutrition/', views.nutrition, name='nutrition'),
    path('profile/', views.profile, name='profile'),
]
