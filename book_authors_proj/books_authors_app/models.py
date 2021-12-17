from django.db import models
from django.db.models.fields import DateTimeField, TextField

class Book(models.Model):
    title = models.CharField(max_length= 255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Author:
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    books = models.ManyToManyField(Book, related_name= "authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


