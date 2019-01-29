from django.db import models
from django.contrib.auth.models import User
#divad/david22

class Student(models.Model):
<<<<<<< HEAD
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Nom del usuari")
    name = models.CharField(max_length=500, blank=True, verbose_name="Nom")
    surname = models.CharField(max_length=500, blank=True, verbose_name="Cognoms")
    dni = models.CharField(max_length=9, blank=True, verbose_name="DNI", primary_key=True)

    def __str__(self):
        return self.name+" "+self.surname
=======
    user = models.OneToOneField(User, on_delete=models.CASCADE)#si eliminem al user, s'elimina el estudiant
    #name = models.CharField(max_length=500, blank=True)
    #surname = models.CharField(max_length=500, blank=True)
    #dni = models.CharField(max_length=9, blank=True)
    experiencia = models.CharField(max_length=40000,blank=False,default='')
    estudis = models.CharField(max_length=400,blank=True,default='')
    idiomes = models.CharField(max_length=400,blank=True,default='')#!!!!!!!!
    coneixements = models.CharField(max_length=400,blank=True,default='')
    carnet_de_conduir=models.CharField(max_length=400,blank=True,default='')#BooleandField
    situacio_laboral=models.CharField(max_length=400,blank=True,default='')
>>>>>>> david
