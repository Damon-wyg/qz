# -*- coding: UTF-8 --*-
from django.shortcuts import render
from interface import *
import logging

logger = logging.getLogger('django')

def algorithms(request):
    data = AlgorithmData()
    data.addQuestion(qnum='1', qname='这是一个算法问题的题目', difc='easy', accep='good', advi='true', qurl='/problems/algorithms/1')
    data.addTag(href='#', nums='10', tag='算法')
    data.setState(1, 60, xrange(1, 4))
    
    return render(request, 'algorithms.html', data.getDict())

def question(request):
    data = QuestionData()
    data.addQuestionDetailData(qtitle='这个一个算法题目的标题', qcontent='倒序一个字符串，倒序一个字符串。。', qexample='abscsd->dscsba')
    data.addLang(val='cpp', name='c++')
    data.addLang(val='js', name='javascript')

    return render(request, 'question.html', data.getDict())

