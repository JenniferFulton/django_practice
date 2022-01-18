from django.db import models

class UserManager(models.Manager):
    def RegistrationManager(self, postData):
        errors = {}
        

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
