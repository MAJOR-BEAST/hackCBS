from django.conf.urls import include, url
from django.contrib import admin
from convertor import views

urlpatterns = (
    url(r'^$', views.index, name='index'),
    url(r'login/$', views.login, name='login'),
    url(r'dashboard/$', views.dashboard, name='dashboard'),
    url(r'data/$', views.simple_upload, name='data'),
)
