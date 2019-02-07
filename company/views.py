from django.shortcuts import render,get_object_or_404
from .models import Company
from student.models import Student
from .forms import FormCompany, EditComany
from django.urls import reverse
from oferta.models import Oferta, ofertainscrits
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from oferta.forms import PubJobOffer
from django.contrib.auth.decorators import login_required

def formulari(request):
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
    context={
        "el_form_registre_nova_empresa":form,
    }
    return render(request, 'company/company_form.html',context)
@login_required
def index_empresa(request):
    nom_autentifiat = str(request.user.get_username())
    toteslesofertes= Oferta.objects.all().filter(nomempresadelaoferta=nom_autentifiat)
    context = {
        "toteslesempreses": toteslesofertes,
    }
    return render(request, 'company/index_company.html', context)
@login_required
def eliminar(request,x_id):
    print ('entro')
    Oferta.objects.filter(id=x_id).delete()
    return HttpResponseRedirect(reverse('home:empresa:index_empresa', ))
@login_required
def info_oferta(request,x_id):
    oferta= get_object_or_404(Oferta,pk=x_id)
    form = PubJobOffer(request.POST or None,initial={"nom_oferta":oferta.nom_oferta,"poblacio":oferta.poblacio,
                                                     "telefon":oferta.telefon,"lloc_treball_sofereix":oferta.lloc_treball_sofereix,
                                                     "horari":oferta.horari,"caracteristiques":oferta.caracteristiques,
                                                     "numero_vacants":oferta.numero_vacants,"salari":oferta.salari,})
    # print(dir(form))
    nom_autentifiat = str(request.user.get_username())

    if request.method == 'POST':
        if form.is_valid():
            # print(form.cleaned_data)
            form_data = form.cleaned_data
            nom_oferta = form_data.get("nom_oferta")
            poblacio = form_data.get("poblacio")
            telefon = form_data.get("telefon")
            lloc_treball_sofereix = form_data.get("lloc_treball_sofereix")
            horari = form_data.get("horari")
            caracteristiques = form_data.get("caracteristiques")
            numero_vacants = form_data.get("numero_vacants")
            salari = form_data.get("salari")
            nom_autentifiat = str(request.user.get_username())
            empresa = Company.objects.get(nomusuari=nom_autentifiat)
            obj = Oferta.objects.filter(pk=x_id).update(nom_oferta=nom_oferta, poblacio=poblacio, telefon=telefon, lloc_treball_sofereix=lloc_treball_sofereix,
                                                        horari=horari, caracteristiques=caracteristiques, numero_vacants=numero_vacants,salari=salari
                                    )

            return HttpResponseRedirect(reverse('home:empresa:index_empresa', ))
    context = {
        "editar_oferta": form,
        "id":x_id,
    }
    return render(request,'company/info_oferta.html',context)
@login_required
def persones_inscrites(request,x_id):
    totselsmembres=ofertainscrits.objects.all().filter(oferta=x_id)
    for x in totselsmembres:
        print (x)

    context = {
        "totselsmembres": totselsmembres,
    }
    return render(request,'company/persones_inscrites.html',context)
@login_required
def editar_perfil(request,id_user):
    empresa=Company.objects.all().filter(user_id=id_user)[0]
    form = EditComany(request.POST or None,initial={"sector":empresa.sector,"descripcio":empresa.descripcio,"nomResponsable":empresa.nomResponsable,"cognomResponsable":empresa.cognomResponsable})
    if request.method == 'POST':
        if form.is_valid():
            form_data = form.cleaned_data
            cif = form_data.get("cif")
            sector = form_data.get("sector")
            descripcio = form_data.get("descripcio")
            nomResponsable = form_data.get("nomResponsable")
            cognomResponsable = form_data.get("cognomResponsable")
            obj = Company.objects.filter(user_id=id_user).update(sector=sector,descripcio=descripcio,nomResponsable=nomResponsable,cognomResponsable=cognomResponsable)

            return HttpResponseRedirect(reverse('home:empresa:index_empresa', ))
    context = {
        "editar_perfil": form,
    }
    return render(request,'company/editar_perfil_empresa.html',context)
@login_required
def info_perfil_estudiant(request,id_student ):
    estudiant=Student.objects.get(id=id_student)
    context = {
        "estudiant": estudiant,
    }
    return render(request,'company/info_perfil_estudiant.html',context)

