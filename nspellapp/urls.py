from django.conf.urls import include, url
from django.contrib import admin

from nspellapp import views

urlpatterns = [
    #url(r'^$', views.API.as_view(), name="api"),
    url(r'^api/$', views.API.as_view(), name="api"),
]
