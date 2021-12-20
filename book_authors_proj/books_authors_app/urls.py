from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_book', views.create_book),
    path('books/<int:book_id>', views.book_info),
    path('authors', views.authors),
    path('create_author', views.create_author),
    path('authors/<int:author_id>', views.author_info),
]