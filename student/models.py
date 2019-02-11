# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Nom del usuari")
    nom=models.CharField(max_length=100, blank=False,default='', verbose_name="Nom")
    cognom=models.CharField(max_length=100, blank=False,default='', verbose_name="Cognom")
    dni=models.CharField(max_length=100, blank=False,default='', verbose_name="DNI", unique=True)
    adreca=models.CharField(max_length=100, blank=False,default='', verbose_name="Adreça")
    poblacio=models.CharField(max_length=100, blank=False,default='', verbose_name="Població")
    codi_postal=models.CharField(max_length=100, blank=False,default='', verbose_name="Codi Postal")
    telefon=models.CharField(max_length=100, blank=False,default='', verbose_name="Telèfon")
    correu_electronic=models.CharField(max_length=100, blank=False,default='', verbose_name="Correu electronic")
    edat=models.CharField(max_length=100, blank=False,default='', verbose_name="Edat")
    estudis=models.CharField(max_length=1000, blank=False,default='', verbose_name="Estudis")
    experiencia=models.CharField(max_length=1000, blank=False,default='', verbose_name="Experiencia")

    def __str__(self):
        return self.user.get_username()


