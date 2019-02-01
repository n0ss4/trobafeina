from django.conf.urls import url
from . import views

app_name = 'estudiant'

urlpatterns = [
    url(r'^$', views.formulari_student, name='registre'),
    url(r'^index_student/', views.index_student, name='index_student'),
]