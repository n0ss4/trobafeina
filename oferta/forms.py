from django.forms import ModelForm
from django import forms
from oferta.models import Oferta


class PubJobOffer(ModelForm):
    class Meta:
        model = Oferta
        fields = ["nom_oferta","poblacio","telefon","lloc_treball_sofereix","horari","caracteristiques","numero_vacants","salari"]#Seran els que es mostraran al formulari
