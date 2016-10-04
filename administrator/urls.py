from django.conf.urls import include, url
from administrator import views

urlpatterns = [
    url(r'^register/$', views.admin_register, name='register'),
    url(r'^user_list/$', views.admin_user_list, name='admin_user_list'),
    url(r'^user/(?P<id_user>[0-9]+)/$', views.the_user_profile, name='the_user'),
]
