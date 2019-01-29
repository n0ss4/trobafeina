from django.urls import path,include
from . import views
app_name = 'joboffer'
urlpatterns = [
    path('', views.index, name='index'),
    path('registre_estudiant/', include('student.urls')),
<<<<<<< HEAD
    path('registre_empresa/', include('company.urls')),
    path('formularis/', views.formularis, name='formularis'),

=======
>>>>>>> aa12a5994c8063dfc4a80bbd8d79e0345d42eb36
]