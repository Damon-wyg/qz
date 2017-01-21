# -*- coding: UTF-8 --*-
from django.shortcuts import render
from qz_master import web_settings
from interface import *
import logging

logger = logging.getLogger(__name__)

def index(request):
    data = IndexData()

    return render(request, 'index.html', data.getDict())


