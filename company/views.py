from django.shortcuts import render,get_object_or_404
from .models import Company
from .forms import FormCompany
from django.urls import reverse
from oferta.models import Oferta, ofertainscrits
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from oferta.forms import PubJobOffer



def formulari(request):
    print("-------------------------------------------------")
    form=FormCompany(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form_data = form.cleaned_data
            print(form_data)
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
            obj1 = Company.objects.create(user=obj,cif=a1,sector=a2,descripcio=a3,nomResponsable=a4,cognomResponsable=a5,nomusuari=nom)
            obj1.save()
            user1=authenticate(username=nom, password=contra)
            login(request,user1)
            return HttpResponseRedirect(reverse('home:empresa:index_empresa',))
            #return render(request, 'company/index_company.html')

    context={
        "el_form_registre_nova_empresa":form,
    }

    return render(request, 'company/company_form.html',context)


def index_empresa(request):
    nom_autentifiat = str(request.user.get_username())
    toteslesempreses= Oferta.objects.all().filter(nomempresadelaoferta=nom_autentifiat)
    context = {
        "toteslesempreses": toteslesempreses,
    }
    return render(request, 'company/index_company.html', context)

def eliminar(request,x_id):
    print ('entro')
    Oferta.objects.filter(id=x_id).delete()
    return HttpResponseRedirect(reverse('home:empresa:index_empresa', ))


def info_oferta(request,x_id):
    oferta= get_object_or_404(Oferta,pk=x_id)
    form = PubJobOffer(request.POST or None,initial={"nom":oferta.nom,"requirements":oferta.requirements,"experience":oferta.experience,"minimum_requirements":oferta.minimum_requirements,"description":oferta.description,"numero_de_vacants":oferta.numero_de_vacants,"salari":oferta.salari})
    # print(dir(form))
    nom_autentifiat = str(request.user.get_username())

    empresa = User.objects.all()
    elquevull = empresa.get(username='empresa')
    print(elquevull.email)
    if request.method == 'POST':
        if form.is_valid():
            # print(form.cleaned_data)
            form_data = form.cleaned_data
            abc = form_data.get("nom")
            abc1 = form_data.get("requirements")
            abc2 = form_data.get("experience")
            abc3 = form_data.get("minimum_requirements")
            abc4 = form_data.get("description")
            # abc5 = form_data.get("publicada")
            abc6 = form_data.get("numero_de_vacants")
            abc7 = form_data.get("salari")
            nom_autentifiat = str(request.user.get_username())
            empresa = Company.objects.get(nomusuari=nom_autentifiat)
            obj = Oferta.objects.filter(pk=x_id).update(nom=abc, requirements=abc1, experience=abc2, minimum_requirements=abc3,
                                        description=abc4, numero_de_vacants=abc6, salari=abc7,
                                        empresadelaoferta=empresa, nomempresadelaoferta=nom_autentifiat)

            return HttpResponseRedirect(reverse('home:empresa:index_empresa', ))
    context = {
        "editar_oferta": form,
        "id":x_id,
    }
    return render(request,'company/info_oferta.html',context)

def persones_inscrites(request,x_id):
    totselsmembres=ofertainscrits.objects.all().filter(oferta=x_id)
    for x in totselsmembres:
        print (x.estudiant.user.get_username())

    context = {
        "totselsmembres": totselsmembres,
    }
    return render(request,'company/persones_inscrites.html',context)
