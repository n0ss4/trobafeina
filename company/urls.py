from django.conf.urls import url,include

from . import views

app_name = 'empresa'

urlpatterns = [
    url(r'^$', views.formulari, name='registre'),
    url(r'^index_empresa/', views.index_empresa, name='index_empresa'),
    url(r'^crearoferta/', include('oferta.urls')),
]