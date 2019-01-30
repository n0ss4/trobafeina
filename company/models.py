from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Nom del usuari")
    cif = models.CharField(max_length=9, blank=False,verbose_name="CIF", primary_key=True)
    sector = models.CharField(max_length=500, blank=False)
    descripcio = models.TextField(max_length=500, blank=False,verbose_name="Descripció")
    nomResponsable = models.CharField(max_length=500, blank=False, verbose_name="Nom del responsable")
    cognomResponsable = models.CharField(max_length=500, blank=False, verbose_name="Cognom del responsable")
    esempresaa=models.BooleanField(default=True)
    esempresaa11=models.BooleanField(default=True)

    def __str__(self):
        return self.user.get_username()

