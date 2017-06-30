from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^labels$', views.label_list, name='label_list'),
    url(r'^(?P<slug>[a-z, 0-9]+)/$', views.label, name='label'),
]
