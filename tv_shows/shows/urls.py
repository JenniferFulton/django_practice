from django.urls import path
from . import views

urlpatterns = [
    path('', views.root_route),
    path('shows', views.all_shows),
]