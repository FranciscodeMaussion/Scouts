from django.conf.urls import include, url
from administrator import views

urlpatterns = [
    url(r'^register/$', views.admin_register, name='register'),
]
