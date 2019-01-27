from django.forms import ModelForm
from django import forms

from .models import JobOffer

class RegModelForm(ModelForm):
    class Meta:
        model = JobOffer
        fields = ["requirements","nom","experience","minimum_requirements","description","numero_de_vacants","salari"]#Seran els que es mostraran al formulari
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder':'nom'}),
            'requirements': forms.Textarea(attrs={'placeholder': 'nom'}),

        }
"""
class RegForms(forms.Form):
   nom = forms.CharField()
    requirements = forms.CharField()
    experience = forms.CharField(label="",initial='', widget=forms.Select(),required=True)#si fico aquest peta
    minimum_requirements = forms.CharField(attrs={'placeholder':'eldavid'})
    description = forms.CharField()
    publicada = forms.DateTimeField(auto_now_add=True, auto_now=False)
    numero_de_vacants = forms.IntegerField()
    salari = forms.CharField()"""