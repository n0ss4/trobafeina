from django.urls import path

from . import views

app_name = 'company'

urlpatterns = [
    path('', views.klk, name='entrada'),
    path('registreempresa/', views.formulari, name='formulari'),

]