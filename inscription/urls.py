from django.conf.urls import include, url
from inscription import views

urlpatterns = [
    url(r'^perfil/(?P<afDni>[0-9]+)/$', views.admin_profile, name='profile'),
    url(r'^addAfiliado/$', views.add_affiliate, name='addAfiliado'),
]
