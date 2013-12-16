'''
Created on 2013-10-24

@author: heruilong
'''
from django.conf.urls import patterns, url
from downfile import views
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^downloadfile', views.download, name='downloadfile'),
    url(r'^d3', views.d3, name='d3'),
)
