from django.shortcuts import render
from .forms import PubJobOffer
from .models import Joboffer,Company
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
    if request.user.is_authenticated:#si el usuari esta autentificat
        nom_autentifiat=str(request.user.get_username())#agafem el user del usuari autentificat i el passem a string
        totes_les_empreses=Company.objects.all()#agafem totes les empreses
        variable=False
        for x in totes_les_empreses:#recorrem tots els usuaris que son de empresa
            k=str(x)#passem a string
            if k == nom_autentifiat:#si el usuari autentificat es de una empresa la variable sera true
                variable=True
        if variable:
            return render(request, 'company/index_company.html')#si es empresa anira al login de empres
        return render(request, 'student/index_student.html')#al contrari anira al login
    else:
        print('user no autentificat')
        return render(request, 'JobOffer/index.html')
def formularis(request):
    return render(request, 'JobOffer/registres.html')
