from django.conf.urls import patterns, include, url
from administrator import views

urlpatterns = [
    url(r'^register/$', views.adminRegister, name='register'),
    url(r'^templateAdmin/$', views.templateAdmin, name='templateAdmin'),
    url(r'^perfil/(?P<afDni>[0-9]+)/$', views.adminProfile, name='profile'),

]
