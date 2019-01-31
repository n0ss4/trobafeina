from django.urls import path,include
from . import views
app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('triarformulari/registre_estudiant/', include('student.urls')),
    path('triarformulari/registre_empresa/', include('company.urls')),
    path('triarformulari/', views.formularis, name='formularis'),
    #path('entrada/', views.entrada,)
]
