from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dev_list, name='dev_list'),
    url(r'^conf$', views.hab_config, name='hab_config'),
]
