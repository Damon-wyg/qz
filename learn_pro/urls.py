# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url, include
from learn_pro import views

core_urls = [
    url(r'^$', views.index),
    url(r'^introduct$', views.introduct),
    url(r'^problems/algorithms$', views.algorithms),
    url(r'^problems/projects$', views.projects),
    url(r'^problems/algorithms/1$', views.question),
    url(r'^problems/projects/1$', views.projterm),
    url(r'^discuss$', views.discuss),
]

