from django.db import models
from django.db.models.base import ModelStateFieldsCacheDescriptor

class Shows(models.Model): 
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
