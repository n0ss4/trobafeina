from django.forms import ModelForm
from django import forms

from .models import Student

class FormStudent(ModelForm):
    nom_usuari = forms.CharField()
    contrasenya = forms.CharField()
    class Meta:
        model = Student
        fields = ["experiencia","estudis","idiomes","coneixements","carnet_de_conduir","situacio_laboral"]#Seran els que es mostraran al formulari

