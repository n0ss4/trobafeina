from django.conf.urls import url,include
from . import views
app_name = 'home'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^triarformulari/registre_estudiant/', include('student.urls')),
    url(r'^triarformulari/registre_empresa/', include('company.urls')),
    url(r'^triarformulari/', views.formularis, name='formularis'),
    #path('entrada/', views.entrada,)
]
