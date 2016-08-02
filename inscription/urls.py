from django.conf.urls import patterns, include, url
from inscription import views

urlpatterns = [
    url(r'^addAfiliado/$', views.addAfiliado, name='addAfiliado'),
]
