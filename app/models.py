from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    age=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)