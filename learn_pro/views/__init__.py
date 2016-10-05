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

def introduct(request):
    data = {
        'settings': web_settings,
        'job_tags': [
            {
                'href': '#',
                'name': '工作1',
            },
            {
                'href': '#',
                'name': '工作2',
            },
            {
                'href': '#',
                'name': '公共哦刚给你工作3',
            },
            {
                'href': '#',
                'name': '工作4',
            },
            {
                'href': '#',
                'name': '工作5',
            },
            {
                'href': '#',
                'name': '工作6',
            },
        ],
        'book_list': [
            {
                'href': '#',
                'img_src': 'https://dn-simplecloud.qbox.me/1471513730333.png',
                'name': '这是书名1'
            },
            {
                'href': '#',
                'img_src': 'https://dn-simplecloud.qbox.me/1471513730333.png',
                'name': '这是书名2'
            },
            {
                'href': '#',
                'img_src': 'https://dn-simplecloud.qbox.me/1471513730333.png',
                'name': '这是书名3'
            },
            {
                'href': '#',
                'img_src': 'https://dn-simplecloud.qbox.me/1471513730333.png',
                'name': '这是书名4'
            },
        ],
    }
    return render(request, 'introduct.html', data)

def algorithms(request):
    data = {
        'qlist': [
            {
                'qnum': 1,
                'qname': '算法题目标题标题标啦啦啦啦啦流量',
                'difficulty': '容易',
                'acceptance': '80%',
                'advisable': True
            },
        ],
        'state': {
            'finish_qnum': '1',
            'total_qnum': '100',
            'page_num': ['1', '2'],
            
        },
        'tag_list': [
            {
                'href': '#',
                'nums': 77,
                'tag': '数组',
            },
            {
                'href': '#',
                'nums': 47,
                'tag': '树',
            },
        ],
        'settings': web_settings,
    }
    return render(request, 'algorithms.html', data)

def projects(request):
    data = {
        'settings': web_settings,
        'tag_list': [
            {
                'href': '#',
                'name': 'c++',
            }
        ],
        'proj_terms': [
            {
                'imgurl': 'http://imgsize.ph.126.net/?imgurl=http://p1.music.126.net/CMyxhRIEYQg-xxk84OE7TQ==/116548232550847.jpg_500x500x0x95.jpg',
                'title': '项目标题标题标题',
                'desc_p1': '项目描述项目描述描述项目描述描述项目描述描述项',
                'desc_p2': '目描述描述项目描述描述项目描述描述项目描述描述项目描述描述项目',
                'num': 99,
                'lang': 'c/c++/python',
                'autor': '小汪汪',
                'detailurl': '#',
                'discussurl': '#',
                'crurl': '#',
            },
        ],
    }
    return render(request, 'projects.html', data)

def question(request):
    data = {
        'settings': web_settings,
        'qtitle': '问题标题标题',
        'discussurl': '#',
        'rand_question': '#',
        'qcontent': '倒序一个字符串，倒序一个字符串。。',
        'qexample': 'abscsd->dscsba',
        'lang_list': [
            {
                'val': 'cpp',
                'name': 'c++',
            },
            {
                'val': 'js',
                'name': 'javascript',
            },
        ]
    }
    return render(request, 'question.html', data)

def projterm(request):
    data = {
        'settings': web_settings,
        'ptitle': '项目名称名称',
        'discussurl': '#',
        'rand_question': '#',
        'pcontent': '描述一下项目是干嘛的，怎么做，可以怎样，邀请伙伴等等',
        'ptodo': '1.干嘛。2.干什么。3.xxxx。'
    }
    return render(request, 'projterm.html', data)

def discuss(request):
    data = {
        'settings': web_settings,
    }
    return render(request, 'discuss.html', data)

