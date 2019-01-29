from django.shortcuts import render
from .forms import PubJobOffer
from .models import Joboffer
from django.contrib.auth.models import User


def crearoferta(request):
    form=PubJobOffer(request.POST or None)
    #print(dir(form))
    if form.is_valid():
        #print(form.cleaned_data)
        form_data = form.cleaned_data
        abc = form_data.get("nom")
        abc1 = form_data.get("requirements")
        abc2 = form_data.get("experience")
        abc3 = form_data.get("minimum_requirements")
        abc4 = form_data.get("description")
        #abc5 = form_data.get("publicada")
        abc6 = form_data.get("numero_de_vacants")
        abc7 = form_data.get("salari")
        obj = Joboffer.objects.create(nom=abc,requirements=abc1,experience=abc2,minimum_requirements=abc3,description=abc4,numero_de_vacants=abc6,salari=abc7)
    context={
        "el_form_crearoferta":form,
    }
    return render(request, '', context)

def index(request):
    return render(request, 'JobOffer/index.html')

def formularis(request):
    return render(request, 'JobOffer/registres.html')
