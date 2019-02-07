# -*- coding: utf-8 -*-

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

    if request.method=='POST':
        if form.is_valid():
            form_data = form.cleaned_data
            nom_oferta=form_data.get("nom_oferta")
            poblacio=form_data.get("poblacio")
            telefon=form_data.get("telefon")
            lloc_treball_sofereix=form_data.get("lloc_treball_sofereix")
            horari=form_data.get("horari")
            caracteristiques=form_data.get("caracteristiques")
            numero_vacants=form_data.get("numero_vacants")
            salari=form_data.get("salari")

            nom_autentifiat = str(request.user.get_username())
            empresa = Company.objects.get(nomusuari=nom_autentifiat)
            obj = Oferta.objects.create(nom_oferta=nom_oferta, poblacio=poblacio, telefon=telefon, lloc_treball_sofereix=lloc_treball_sofereix, horari=horari,
                                        caracteristiques=caracteristiques, numero_vacants=numero_vacants, salari=salari,empresadelaoferta=empresa,nomempresadelaoferta=nom_autentifiat)
            obj.save()
            return HttpResponseRedirect(reverse('home:empresa:index_empresa',))
    context = {
        "el_form_crearoferta": form,
    }
    return render(request, 'oferta/formulari_crea_oferta.html', context)