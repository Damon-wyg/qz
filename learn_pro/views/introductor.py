# -*- coding: UTF-8 --*-
from django.shortcuts import render
from interface import *
import logging

logger = logging.getLogger('django')

def introduct(request):
    data = IntroductData()
    data.addJobTag(href='#', name='工作啦')
    data.addBookDesc(href='#', img_src='https://dn-simplecloud.qbox.me/1471513730333.png', name='这是一个书名')
    logger.debug(data.getDict())
    return render(request, 'introduct.html', data.getDict())

