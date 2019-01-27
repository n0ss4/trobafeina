from django.forms import ModelForm
from django import forms
from .models import JobOffer,Company
class PubJobOffer(ModelForm):
    class Meta:
        model = JobOffer
        fields = ["requirements","nom","experience","minimum_requirements","description","numero_de_vacants","salari"]#Seran els que es mostraran al formulari
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder':'nom'}),
            'requirements': forms.Textarea(attrs={'placeholder': 'nom'}),

        }
class FormCompany(ModelForm):
    nom_usuari = forms.CharField()
    contrasenya = forms.CharField()
    class Meta:
        model = Company
        fields = ["cif","sector","descripcio","nomResponsable","cognomResponsable"]
