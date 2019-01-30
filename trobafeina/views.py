from django.shortcuts import render


def index(request):
    return render(request, 'JobOffer/index.html')

#def salir(request):
 #   print("eiiii")
  #  return render(request, 'JobOffer/index.html')