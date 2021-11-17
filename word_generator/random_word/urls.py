from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('random_word', views.word),
    path('random_word/reset', views.reset),
]