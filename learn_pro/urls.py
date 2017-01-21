# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url, include
from learn_pro import views
import logging

logger = logging.getLogger('django')

core_urls = [
    url(r'^$', views.index.index),
    url(r'^introduct$', views.introductor.introduct),
    url(r'^problems/algorithms$', views.algorithms.algorithms),
    url(r'^problems/projects$', views.projects.projects),
    url(r'^problems/algorithms/1$', views.algorithms.question),
    url(r'^problems/projects/1$', views.projects.projterm),
    url(r'^discuss$', views.discuss.discuss),
]

