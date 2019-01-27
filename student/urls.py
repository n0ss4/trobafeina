from django.urls import path
from . import views
app_name = 'student'
urlpatterns = [
    path('', views.formulari_student, name='formulari_student'),
    path('pagina/',views.pagina, name='pagina')
]