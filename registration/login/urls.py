from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration_login),
    path('register', views.register),
]