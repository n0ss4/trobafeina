from django.http import HttpResponseRedirect
from django.shortcuts import render

from company.models import Company
from django.urls import reverse

def index(request):
    if request.user.is_authenticated:#si el usuari esta autentificat
        print('autentificat')
        nom_autentifiat=str(request.user.get_username())#agafem el user del usuari autentificat i el passem a string
        totes_les_empreses=Company.objects.all()#agafem totes les empreses
        variable=False
        for x in totes_les_empreses:#recorrem tots els usuaris que son de empresa
            k=str(x)#passem a string
            if k == nom_autentifiat:#si el usuari autentificat es de una empresa la variable sera true
                variable=True
        if variable:
            return HttpResponseRedirect(reverse('home:empresa:index_empresa',))
            #return render(request, 'company/index_company.html')#si es empresa anira al login de empres
        return HttpResponseRedirect(reverse('home:estudiant:index_student', ))

        #return render(request, 'student/index_student.html')#al contrari anira al login
    else:
        print('user no autentificat')
        return render(request, 'JobOffer/index.html')
def formularis(request):
    return render(request, 'JobOffer/registres.html')
