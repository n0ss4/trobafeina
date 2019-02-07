# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
from company.models import Company
from student.models import Student


class Oferta(models.Model):
    """nom = models.CharField(max_length=50,blank=False,null=False)
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

nomempresadelaoferta=models.CharField(blank=True,null=True,max_length=1000)"""
    nom_oferta = models.CharField(max_length=100, blank=False, null=False,verbose_name="Nom oferta")
    poblacio = models.CharField(max_length=100, blank=False, null=False,verbose_name="Població")
    telefon = models.CharField(max_length=100, blank=False, null=False,verbose_name="Telefon")
    lloc_treball_sofereix = models.CharField(max_length=500, blank=False, null=False,verbose_name="Lloc de treball que s'ofereix")
    horari = models.CharField(max_length=100, blank=False, null=False,verbose_name="Horari")
    caracteristiques = models.CharField(max_length=900, blank=False, null=False,verbose_name="Caracteristiques del treball a realitzar")
    numero_vacants = models.CharField(max_length=100, blank=False, null=False,verbose_name="Numero de vacants")
    salari = models.CharField(max_length=100, blank=False, null=False,verbose_name="Salari")
    empresadelaoferta = models.ForeignKey(Company, on_delete=models.CASCADE)#es la empresa
    oferta_inscrits=models.ManyToManyField(Student,through='ofertainscrits')
    nomempresadelaoferta=models.CharField(blank=True,null=True,max_length=1000)

class ofertainscrits(models.Model):
    estudiant=models.ForeignKey(Student, on_delete=models.CASCADE)
    oferta= models.ForeignKey(Oferta,on_delete=models.CASCADE)
    class Meta:
        unique_together = (("estudiant", "oferta"),)




