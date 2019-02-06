from django.forms import ModelForm
from django import forms
from .models import Company


class FormCompany(ModelForm):
    nom_usuari = forms.CharField()
    contrasenya = forms.CharField()

    class Meta:
        model = Company
        fields = ["cif", "sector", "descripcio", "nomResponsable", "cognomResponsable"]
