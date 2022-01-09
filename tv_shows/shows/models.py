from django.db import models
from django.db.models.base import ModelStateFieldsCacheDescriptor
from datetime import date
from django.core.validators import MaxValueValidator

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors ={}

        if len(postData['title']) < 3:
            errors['title'] = "Ttitle should be atleast 3 characters"

        if len(postData['network']) < 3:
            errors['network'] = "Network needs to be atleast 3 characters"

        if len(postData['description']) < 10:
            errors['description'] = "Please provide more details! Description should be atleast 10 characters"

        # postData['release_date'] = [MaxValueValidator(limit_value = date.today())]
        
        return errors

class Show(models.Model): 
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = ShowManager()


