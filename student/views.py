from django.shortcuts import render, get_object_or_404
from oferta.models import Oferta,ofertainscrits
from .forms import FormStudent, EditStudent
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Student
from django.contrib.auth.decorators import login_required
def formulari_student(request):
    form=FormStudent(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data)
            form_data = form.cleaned_data
            nom=form_data.get("nom_usuari")
            contra = form_data.get("contrasenya")
            nom2=form_data.get("nom")
            cognom=form_data.get("cognom")
            dni=form_data.get("dni")
            adreca=form_data.get("adreca")
            poblacio=form_data.get("poblacio")
            codi_postal=form_data.get("codi_postal")
            telefon=form_data.get("telefon")
            correu_electronic=form_data.get("correu_electronic")
            edat=form_data.get("edat")
            estudis=form_data.get("estudis")
            experiencia=form_data.get("experiencia")
            print(form_data)
            obj= User.objects.create_user(nom,password=contra)
            obj.save()
            obj1 = Student.objects.create(user=obj,nom=nom2,cognom=cognom,dni=dni,adreca=adreca,poblacio=poblacio,
                                          codi_postal=codi_postal,telefon=telefon,
                                          correu_electronic=correu_electronic,edat=edat,estudis=estudis,experiencia=experiencia)
            obj1.save()
            user1 = authenticate(username=nom, password=contra)
            login(request, user1)
            return HttpResponseRedirect(reverse('home:estudiant:index_student',))
    context={
        "el_form_formulari_student":form,
    }

    return render(request, 'student/student_form.html',context)
@login_required
def index_student(request):
    toteslesofertes= Oferta.objects.all()
    context = {
        "toteslesofertes": toteslesofertes,
    }
    return render(request, 'student/index_student.html',context)
@login_required
def info_oferta(request,x_id):
    oferta= get_object_or_404(Oferta,pk=x_id)
    context = {
        "infooferta": oferta,
    }
    return render(request,'student/info_oferta.html',context)
@login_required
def inscriures(request,id_oferta):
    usuari = request.user
    estudiant = Student.objects.all().filter(user=usuari)[0]
    oferta = Oferta.objects.get(pk=id_oferta)
    tots=ofertainscrits.objects.all()
    texto="T'estas intentan registra a una oferta que ja t'has registrat"
    context = {
        "infooferta": oferta,
        "mensaje":texto,
    }
    if tots.filter(estudiant=estudiant,oferta=oferta):
        return render(request, 'student/info_oferta.html', context)
    else:
        ofertainscrits.objects.create(estudiant=estudiant,oferta=oferta)
    return HttpResponseRedirect(reverse('home:estudiant:index_student', ))
@login_required
def editar_perfil(request,id_user):
    estudiant=Student.objects.all().filter(user_id=id_user)[0]
    form = EditStudent(request.POST or None,initial={"nom":estudiant.nom,"cognom":estudiant.cognom,"dni":estudiant.dni,"adreca":estudiant.adreca,"poblacio":estudiant.poblacio,
                                          "codi_postal":estudiant.codi_postal,"telefon":estudiant.telefon,
                                          "correu_electronic":estudiant.correu_electronic,"edat":estudiant.edat,"estudis":estudiant.estudis,"experiencia":estudiant.experiencia})
    if request.method == 'POST':
        if form.is_valid():
            form_data = form.cleaned_data
            nom2 = form_data.get("nom")
            cognom = form_data.get("cognom")
            adreca = form_data.get("adreca")
            poblacio = form_data.get("poblacio")
            codi_postal = form_data.get("codi_postal")
            telefon = form_data.get("telefon")
            correu_electronic = form_data.get("correu_electronic")
            edat = form_data.get("edat")
            estudis = form_data.get("estudis")
            experiencia = form_data.get("experiencia")
            obj = Student.objects.filter(user_id=id_user).update(nom=nom2,cognom=cognom,adreca=adreca,poblacio=poblacio,
                                          codi_postal=codi_postal,telefon=telefon,
                                          correu_electronic=correu_electronic,edat=edat,estudis=estudis,experiencia=experiencia)

            return HttpResponseRedirect(reverse('home:estudiant:index_student', ))
    context = {
        "editar_perfil": form,
    }
    return render(request,'student/editar_perfil_estudiant.html',context)

