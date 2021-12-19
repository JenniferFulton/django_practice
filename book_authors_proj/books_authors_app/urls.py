from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_book', views.create_book),
    # Need path for /books/<books.id>
    path('authors', views.authors),
    path('create_author', views.create_author),
    # Need path for /authors/<author.id>
]