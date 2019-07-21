"""Todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.urls import path,include
from django.conf.urls import *



urlpatterns = [
    path(r'^$', TodoListView.as_view(), name='base'),
    path(r'^todo/(?P<id>\d+)/$', TodoDetailView.as_view(), name='list_detail'),
    path(r'^todo/new/$', TodoCreateView.as_view(), name='make_list'),
    path(r'^todo/edit/(?P<id>\d+)/$', TodoUpdateView.as_view(), name='update_list'),
    path(r'^todo/delete/(?P<id>\d+)/$', TodoDeleteView.as_view(), name='delete_list'),
    path(r'^todo/finish/(?P<id>\d+)/$', 'Finish', name='finish'),
]