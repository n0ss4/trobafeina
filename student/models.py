from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500, blank=True)
    surname = models.CharField(max_length=500, blank=True)
    dni = models.CharField(max_length=9, blank=True)
