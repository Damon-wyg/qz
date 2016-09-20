# -*- coding: UTF-8 --*-
from django.shortcuts import render
from qz_master import web_settings

# Create your views here.
def index(request):
    # temp data
    data = {
        'webName': '曲直网',
        'settings': web_settings,
    }

    return render(request, 'index.html', data)


