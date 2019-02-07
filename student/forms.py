from django.forms import ModelForm
from django import forms

from .models import Student


class FormStudent(ModelForm):
    nom_usuari = forms.CharField()
    contrasenya = forms.CharField(widget=forms.PasswordInput)
    widgets = {
        'password': forms.PasswordInput()
    }

    class Meta:
        model = Student
        fields = ["nom","cognom","dni","adreca","poblacio","codi_postal","telefon","correu_electronic","edat","estudis","experiencia"]#Seran els que es mostraran al formulari

class EditStudent(ModelForm):
     class Meta:
        model = Student
        fields = ["nom","cognom","adreca","poblacio","codi_postal","telefon","correu_electronic","edat","estudis","experiencia"]#Seran els que es mostraran al formulari

