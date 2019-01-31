from django.shortcuts import render
from oferta.forms import PubJobOffer
from oferta.models import Oferta
# Create your views here.
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
        obj = Oferta.objects.create(nom=abc,requirements=abc1,experience=abc2,minimum_requirements=abc3,description=abc4,numero_de_vacants=abc6,salari=abc7)
    context={
        "el_form_crearoferta":form,
    }
    return render(request, 'oferta/formulari_crea_oferta.html', context)