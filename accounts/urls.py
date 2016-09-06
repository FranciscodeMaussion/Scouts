from django.conf.urls import include, url
from accounts import views

urlpatterns = [
    url(r'^crear_transaccion/$', views.create_transaction, name='createTransaction'),
    url(r'^crear_evento/$', views.new_event, name='newEvent'),
    url(r'^crear_budget/$', views.new_budget, name='newBudget'),
    url(r'^crear_items/$', views.addItem, name='addItem'),
    url(r'^crear_venta/$', views.new_sale, name='newVenta'),
]
