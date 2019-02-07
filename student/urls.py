from django.conf.urls import url
from . import views

app_name = 'estudiant'

urlpatterns = [
    url(r'^$', views.formulari_student, name='registre'),
    url(r'^index_student/', views.index_student, name='index_student'),
    url(r'^info_oferta/(?P<x_id>\d+)/$', views.info_oferta, name='info_oferta'),
    url(r'^(?P<id_oferta>\d+)/$', views.inscriures, name='inscriures'),
    url(r'^editarperfil/(?P<id_user>\d+)/$', views.editar_perfil, name='editar_perfil'),

]