from django.http import HttpResponseRedirect
from django.shortcuts import render
from company.models import Company
from student.models import Student
from django.urls import reverse


def index(request):
    if request.user.is_authenticated:#si el usuari esta autentificat
        print('autentificat')
        id_autentifiat=request.user
        print(request.user)
        nom_autentifiat=str(request.user.get_username())#agafem el user del usuari autentificat i el passem a string
        companys = Company.objects.all()
        students = Student.objects.all()
        if companys.get().user.get_username().find(nom_autentifiat) == 0:
            return HttpResponseRedirect(reverse('home:empresa:index_empresa',))
        elif students.get().user.get_username().find(nom_autentifiat) == 0:
            return HttpResponseRedirect(reverse('home:estudiant:index_student', ))
        elif nom_autentifiat == 'admin':
            return HttpResponseRedirect('/admin')
    else:
        print('user no autentificat')
        return render(request, 'JobOffer/index.html')


def formularis(request):
    return render(request, 'JobOffer/registres.html')
