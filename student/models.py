from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Nom del usuari")
    name = models.CharField(max_length=500, blank=True, verbose_name="Nom")
    surname = models.CharField(max_length=500, blank=True, verbose_name="Cognoms")
    dni = models.CharField(max_length=9, blank=True, verbose_name="DNI", primary_key=True)

    def __str__(self):
        return self.name+" "+self.surname
