from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cif = models.CharField(max_length=9, blank=False,)
    sector = models.CharField(max_length=500, blank=False)
    descripcio = models.CharField(max_length=500, blank=False)
    nomResponsable = models.CharField(max_length=500, blank=False)
    cognomResponsable = models.CharField(max_length=500, blank=False)
