from django.db import models
from company.models import Company


class Joboffer(models.Model):
    nom = models.CharField(max_length=50,blank=False,null=False)
    requirements = models.CharField(max_length=1000, blank=False)
    EXPERIENCE_REQUIRED = (
        ('0','Experiència no requerida'),
        ('1', 'Al menys un any'),
        ('2', 'Al menys dos any'),
        ('3', 'Més de 3 anys'),
    )
    experience = models.CharField(max_length=1,choices=EXPERIENCE_REQUIRED, blank=False,null=True)
    minimum_requirements = models.CharField(max_length=5000, blank=False)
    description = models.CharField(max_length=40000, blank=False,null=True)
    #publicada = models.DateTimeField(auto_now_add=True,auto_now=False)
    numero_de_vacants = models.IntegerField(blank=False,null=True)
    salari = models.CharField(max_length=200, blank=False,null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)#el set hace todos
