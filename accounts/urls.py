from django.conf.urls import patterns, include, url
from accounts import views

urlpatterns = [
    url(r'^create_movement/$', views.createMovement, name='createMovement'),
    url(r'^crear_evento/$', views.newEvent, name='newEvent'),
    url(r'^crear_budget/$', views.newBudget, name='newBudget'),
    url(r'^crear_item/$', views.newItem, name='newItem'),
]
