from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('create', views.create_book),
    path('int:id', views.book_info),
    
]