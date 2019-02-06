
from django.shortcuts import render, get_object_or_404

from oferta.models import Oferta,ofertainscrits
from .forms import FormStudent
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse


from .models import Student
def formulari_student(request):
    form=FormStudent(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data)
            form_data = form.cleaned_data
            nom=form_data.get("nom_usuari")
            contra = form_data.get("contrasenya")
            a1=form_data.get("experiencia")
            a2=form_data.get("estudis")
            a3=form_data.get("idiomes")
            a4=form_data.get("coneixements")
            a5=form_data.get("carnet_de_conduir")
            a6=form_data.get("situacio_laboral")
            print(form_data)
            obj= User.objects.create_user(nom,password=contra)
            obj.save()
            obj1 = Student.objects.create(user=obj,experiencia=a1,estudis=a2,idiomes=a3,coneixements=a4,carnet_de_conduir=a5,situacio_laboral=a6)
            obj1.save()
            user1 = authenticate(username=nom, password=contra)
            login(request, user1)
            return HttpResponseRedirect(reverse('home:estudiant:index_student',))
            #return render(request, 'student/index_student.html')
    context={
        "el_form_formulari_student":form,
    }

    return render(request, 'student/student_form.html',context)

def index_student(request):
    toteslesempreses= Oferta.objects.all()
    """totesofertesinscrits=ofertainscrits.objects.all()
    for x in totesofertesinscrits:
        print (x.estudiant.user.get_username())
        print (x.oferta.id)
        print (x.estudiant.id)
"""
    context = {
        "toteslesempreses": toteslesempreses,
    }

    return render(request, 'student/index_student.html',context)

def info_oferta(request,x_id):
    print ("--------------")
    oferta= get_object_or_404(Oferta,pk=x_id)

    context = {
        "infooferta": oferta,
    }
    return render(request,'student/info_oferta.html',context)

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
        print ("existeee")

        return render(request, 'student/info_oferta.html', context)

    else:
        ofertainscrits.objects.create(estudiant=estudiant,oferta=oferta)

    print (id_oferta)

    print (oferta.nom)
    #print (students)
    print (estudiant.user.get_username())
    #print (Student.user.get_username())
    return HttpResponseRedirect(reverse('home:estudiant:index_student', ))


