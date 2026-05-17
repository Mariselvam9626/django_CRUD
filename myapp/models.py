from django.db import models
from django.contrib.auth.models import AbstractUser


class Student(models.Model):           #Models creates the structure of database
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    ph_no = models.CharField(max_length=10,  null=True, blank=True)
    location = models.CharField(max_length=100, default="chennai")

    def __str__(self):
        return self.name
    

class User(AbstractUser):

    location = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.username

