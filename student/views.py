from django.shortcuts import render
from .forms import FormStudent
from django.contrib.auth.models import User

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
            return render(request, 'student/index_student.html')
    context={
        "el_form_formulari_student":form,
    }

    return render(request, 'student/student_form.html',context)

def index_student(request):
    return render(request, 'student/index_student.html')
