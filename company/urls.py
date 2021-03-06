from django.conf.urls import url,include

from . import views

app_name = 'empresa'

urlpatterns = [
    url(r'^$', views.formulari, name='registre'),
    url(r'^index_empresa/', views.index_empresa, name='index_empresa'),
    url(r'^crearoferta/', include('oferta.urls')),
    url(r'^(?P<x_id>\d+)/$', views.info_oferta, name='info_oferta'),
    url(r'^eliminar/(?P<x_id>\d+)/$', views.eliminar, name='eliminar'),
    url(r'^personesinscrites/(?P<x_id>\d+)/$', views.persones_inscrites, name='persones_inscrites'),
    url(r'^editarperfil/(?P<id_user>\d+)/$', views.editar_perfil, name='editar_perfil'),
    url(r'^info_perfil_estudiant/(?P<id_student>\d+)/$', views.info_perfil_estudiant, name='info_perfil_estudiant'),

]