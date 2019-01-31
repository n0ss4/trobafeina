from django.urls import path,include

from . import views

app_name = 'empresa'

urlpatterns = [
    path('', views.formulari, name='registre'),
    path('index_empresa/', views.index_empresa, name='index_empresa'),
    path('crearoferta/', include('oferta.urls')),
]