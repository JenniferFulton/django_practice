from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('result', views.results),
    path('success', views.success)
]