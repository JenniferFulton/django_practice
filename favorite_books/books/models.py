from operator import imod
from django.db import models
from login.models import User

class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}

        if len(postData['title']) == 0:
            errors['title'] = "Please enter a book title!"

        if len(postData['description']) < 5:
                errors['description'] = "Book description must be atleast 5 characters."

        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete='', null=True)
    user_who_like = models.ManyToManyField(User, related_name="liked_books", null=True)
    objects = BookManager()
