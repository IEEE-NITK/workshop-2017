from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    #url(r'^$', views.home, name="home"),
    url(r'^detail/(?P<studentid>[0-9]+)/$', views.detail, name="detail"),
]
