from django.db import models

# Create your models here.

class User(models.Model):
    ad= models.CharField(max_length=50)
    soyad= models.CharField(max_length=50)