from django.shortcuts import render
from oferta.forms import PubJobOffer
from oferta.models import Oferta
from django.contrib.auth.models import User
from company.models import Company
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def crearoferta(request):
    form=PubJobOffer(request.POST or None)
    #print(dir(form))
    nom_autentifiat = str(request.user.get_username())

    empresa = User.objects.all()
    elquevull=empresa.get(username='empresa')
    print(elquevull.email)
    if request.method=='POST':
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
            nom_autentifiat = str(request.user.get_username())
            empresa = Company.objects.get(nomusuari=nom_autentifiat)
            obj = Oferta.objects.create(nom=abc,requirements=abc1,experience=abc2,minimum_requirements=abc3,description=abc4,numero_de_vacants=abc6,salari=abc7,empresadelaoferta=empresa,nomempresadelaoferta=nom_autentifiat)
            obj.save()
            return HttpResponseRedirect(reverse('home:empresa:index_empresa',))
    context={
        "el_form_crearoferta":form,
    }
    return render(request, 'oferta/formulari_crea_oferta.html', context)