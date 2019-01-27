from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cif = models.CharField(max_length=9, blank=False,)
    sector = models.CharField(max_length=500, blank=False)
    descripcio = models.CharField(max_length=500, blank=False)
    nomResponsable = models.CharField(max_length=500, blank=False)
    cognomResponsable = models.CharField(max_length=500, blank=False)

class JobOffer(models.Model):
    nom = models.CharField(max_length=50,blank=False,null=False)
    requirements = models.CharField(max_length=1000, blank=False)
    EXPERIENCE_REQUIRED = (
        ('no','Experiència no requerida'),
        ('1', 'Al menys un any'),
        ('2', 'Al menys dos any'),
        ('3', 'Més de 3 anys'),
    )
    experience = models.CharField(max_length=1,choices=EXPERIENCE_REQUIRED, blank=False,null=True)
    minimum_requirements = models.CharField(max_length=5000, blank=False)
    description = models.CharField(max_length=40000, blank=True,null=False)
    #publicada = models.DateTimeField(auto_now_add=True,auto_now=False)
    numero_de_vacants = models.IntegerField(blank=False,null=True)
    salari = models.CharField(max_length=200, blank=False,null=True)
