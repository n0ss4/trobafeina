from django.urls import path,include

from . import views

app_name = 'oferta'

urlpatterns = [
    path('', views.crearoferta, name='oferta'),
]