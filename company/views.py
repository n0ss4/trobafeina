from django.shortcuts import render
from .forms import PubJobOffer
from .models import JobOffer,Company
from .forms import FormCompany
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
        obj = JobOffer.objects.create(nom=abc,requirements=abc1,experience=abc2,minimum_requirements=abc3,description=abc4,numero_de_vacants=abc6,salari=abc7)
    context={
        "el_form_crearoferta":form,
    }
    return render(request, 'company/formulari_crea_oferta.html',context)

def formulari(request):
    form=FormCompany(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        nom=form_data.get("nom_usuari")
        contra = form_data.get("contrasenya")
        a1=form_data.get("cif")
        a2=form_data.get("sector")
        a3=form_data.get("descripcio")
        a4=form_data.get("nomResponsable")
        a5=form_data.get("cognomResponsable")
        print(form_data)
        obj= User.objects.create_user(nom,password=contra)
        obj.save()
        obj1 = Company.objects.create(user=obj,cif=a1,sector=a2,descripcio=a3,nomResponsable=a4,cognomResponsable=a5)
        obj1.save()
    context={
        "el_form_registre_nova_empresa":form,
    }

    return render(request, 'company/company_form.html',context)