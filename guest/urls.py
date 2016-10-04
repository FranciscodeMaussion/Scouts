from django.conf.urls import include, url
from guest import views

urlpatterns = [
    url(r'^$', views.view_index, name='inup'),
    url(r'^login/$', views.login_for_the_admin, name='login'),
    url(r'^presupuesto_del_(?P<idEvento>[0-9]+)/$', views.view_presupuesto_evento, name='view_presupuesto_evento'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^eventos/$', views.view_events, name='eventos'),
    url(r'^transaccion/$', views.view_transaccion, name='transaccion'),
]
