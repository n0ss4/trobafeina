from django.urls import path,include
from . import views
app_name = 'joboffer'
urlpatterns = [
    path('', views.index, name='index'),
    path('registre_estudiant/', include('student.urls')),
    path('registre_empresa/', include('company.urls'))

]