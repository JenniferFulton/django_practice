from django.db import models
import re

class UserManager(models.Manager):
    def RegistrationManager(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name should be atleast 2 characters'

        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name should be atleast 2 characters'

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email address'

        if len(postData['password']) < 8:
            errors['password'] = 'Passoword must be atleast 8 characters'

        if postData['password'] != postData['confirm_pw']:
            errors['confirm_pw'] = 'Passwords do not match'

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    objects = UserManager()
