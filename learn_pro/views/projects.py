# -*- coding: UTF-8 --*-
from django.shortcuts import render
from interface import *
import logging

logger = logging.getLogger('django')

def projects(request):
    data = ProjectsData()
    data.addTag(href='#', name='c++')
    data.addProjTerm(imgurl='http://imgsize.ph.126.net/?imgurl=http://p1.music.126.net/CMyxhRIEYQg-xxk84OE7TQ==/116548232550847.jpg_500x500x0x95.jpg', \
        title='项目标题标题啦', \
        desc_p1='项目描述的第一部分，分两部分是用于限制字数，以兼容pc和移动场景，第一部分是必须显示的', \
        desc_p2='项目描述的第而部分，当是移动场景时将不显示，后面将这个接口合并，用函数来处理自动分part', \
        num='99', \
        lang='c/c++/python', \
        autor='小汪汪', \
        detailurl='/problems/projects/1')

    return render(request, 'projects.html', data.getDict())

def projterm(request):
    data = ProjTermData()
    data.addProjTermData(ptitle='项目标题标题拉', pcontent='详细描述项目是干什么的，作用是什么，怎么做，可以怎样，邀请伙伴等等', ptodo='1.干嘛。2.干什么。3.xxxx。')
    return render(request, 'projterm.html', data.getDict())

