from django.contrib import admin
from django.urls import path
from django.urls import include
from form import views

urlpatterns = [
    path('',views.registration,name='registration'),
    path('signin',views.signin,name='signin'),
    path('homepage',views.homepage,name='homepage'),
    
]