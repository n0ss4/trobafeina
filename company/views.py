from django.shortcuts import render
from .models import Company
from .forms import FormCompany
from django.contrib.auth.models import User


def formulari(request):
    form=FormCompany(request.POST or None)
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
        obj1 = Company.objects.create(user=obj,cif=a1,sector=a2,descripcio=a3,nomResponsable=a4,cognomResponsable=a5)
        obj1.save()
    context={
        "el_form_registre_nova_empresa":form,
    }

    return render(request, 'company/company_form.html',context)

