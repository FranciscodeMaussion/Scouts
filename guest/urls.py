from django.conf.urls import include, url
from guest import views

urlpatterns = [
    url(r'^$', views.view_index, name='inup'),
    url(r'^login/$', views.login_for_the_admin, name='login'),
    url(r'^lista_afiliados/$', views.affiliates_list, name='affiliates'),
    url(r'^perfil/(?P<afDni>[0-9]+)/$', views.affiliate_profile, name='profile'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^eventos/$', views.view_events, name='eventos'),
]
