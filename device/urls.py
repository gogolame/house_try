from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dev_list, name='dev_list'),
<<<<<<< HEAD
    url(r'^conf$', views.hab_config, name='hab_config'),
]
=======
]
>>>>>>> 77f1a1b2602a9cd7b679f64812aa35dda1ab8d04
