from django.conf.urls import patterns, include, url
from guest import views

urlpatterns = [
    url(r'^$', views.inup, name='inup'),
    url(r'^login/$', views.adminLogIn, name='login'),
    url(r'^lista_afiliados/$', views.affiliatesList, name='affiliates'),
    url(r'^perfil/(?P<afDni>[0-9]+)/$', views.profile, name='profile'),
    url(r'^logout/$', views.adminLogOut, name='logout'),
    url(r'^eventos/$', views.eventos, name='eventos'),
]
