from django.urls import path
from . import views

urlpaatterns = [
    path('', views.index),
]