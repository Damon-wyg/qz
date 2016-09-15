# -*- coding: UTF-8 --*-
from django.shortcuts import render

# Create your views here.
def index(request):
    # temp data
    data = {
        'webName': '曲直网'
    }

    return render(request, 'index.html', data)


