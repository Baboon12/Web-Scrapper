from enum import Flag
from unicodedata import name
from django.db import models
 
class Destination(models.Model):
    
    name = models.CharField(max_length=200)
    
    desc=  models.TextField()
    price= models.IntegerField
    offer = models.BooleanField(default=False)