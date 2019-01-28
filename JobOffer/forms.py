from django.forms import ModelForm
from django import forms
from .models import JobOffer
class PubJobOffer(ModelForm):
    class Meta:
        model = JobOffer
        fields = ["requirements","nom","experience","minimum_requirements","description","numero_de_vacants","salari"]#Seran els que es mostraran al formulari
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder':'nom'}),
            'requirements': forms.Textarea(attrs={'placeholder': 'nom'}),

        }