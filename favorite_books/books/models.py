from django.db import models

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
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
