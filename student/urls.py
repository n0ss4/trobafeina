from django.urls import path
from . import views
app_name = 'estudiant'
urlpatterns = [
    path('', views.formulari_student, name='registre'),
]