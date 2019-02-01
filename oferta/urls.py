from django.conf.urls import url,include

from . import views

app_name = 'oferta'

urlpatterns = [
    url(r'^$', views.crearoferta, name='oferta'),
]