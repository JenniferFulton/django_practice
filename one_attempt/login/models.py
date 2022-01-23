from django.db import models
import re
import bcrypt
import datetime

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        check_user = User.objects.filter(email = postData['email'])

        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name should be atleast 2 characters'

        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name should be atleast 2 characters'

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email address'
        
        if len(check_user) != 0:
            errors['duplicate_email'] = 'Email already registered, please use a different email to resister'
        

        if len(postData['password']) < 8:
            errors['password'] = 'Password must be atleast 8 characters'

        if postData['password'] != postData['confirm_pw']:
            errors['confirm_pw'] = 'Passwords do not match'
        
        return errors
    
    def login_validator(self, postData):
        errors = {}
        check_user = User.objects.filter(email = postData['logemail'])

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['logemail']):
            errors['email'] = 'Please provide valid email address'
        
        if len(check_user) == 0:
            errors['no_user'] = 'User does not exist, please register first'

        elif not bcrypt.checkpw(postData['logpassword'].encode(), check_user[0].password.encode()):
            errors['invalid_pw'] = 'Password does not match username'

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    objects = UserManager()