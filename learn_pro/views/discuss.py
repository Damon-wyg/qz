# -*- coding: UTF-8 -*-
from django.shortcuts import render
from interface import *
import logging

logger = logging.getLogger('django')

def discuss(request):
    data = DiscussData()

    return render(request, 'discuss.html',  data.getDict())

