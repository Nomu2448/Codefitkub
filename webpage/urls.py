from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('',  views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('bmi', views.bmi, name='bmi'),
    path('nutrition/', views.nutrition, name='nutrition'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
