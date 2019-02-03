from django.http import HttpResponseRedirect
from django.shortcuts import render
from company.models import Company
from student.models import Student
from django.urls import reverse


def index(request):
    # Si l'usuari esta autenticat entrara.
    if request.user.is_authenticated:
        # Seguidament agafara l'usuari a traves del request.user
        usuari=request.user
        # Agafarem totes les empreses i tots els estudiants.
        companys = Company.objects.all()
        students = Student.objects.all()
        # Farem un filter de tots els companys per veure si dintre de empreses existeix aquest usuari.
        if companys.filter(user=usuari):
            # Si es aixi el returnarem al panell d'empresa.
            return HttpResponseRedirect(reverse('home:empresa:index_empresa',))
        # Si no es una empresa pero es un estudiant...
        elif students.filter(user=usuari):
            # Entrara dintre del panell d'estudiants...
            return HttpResponseRedirect(reverse('home:estudiant:index_student', ))
        # Si no es un estudiant i tampoc es una empresa, pero el seu nom es 'admin'
        elif str(request.user.get_username()) == 'admin':
            # Entrara dintre del panell d'administracio
            return HttpResponseRedirect('/admin')
    else:
        # I finalment si no es cap dels altres el retornara al index.html
        return render(request, 'JobOffer/index.html')


def formularis(request):
    return render(request, 'JobOffer/registres.html')
