
import email
from turtle import mode
from unicodedata import name
from django.db import models
 
class feedback(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    feedback=models.CharField(max_length=1000)
    class meta:
        db_table="feedback"