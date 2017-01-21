# -*- coding: utf-8 -*-
'''
本文件用于数据接口定义，定义与模板交互的各种数据接口类
'''

from qz_master import web_settings
from abc import ABCMeta, abstractmethod
import logging

logger = logging.getLogger('django')

class DictDataBase(object):
    '''
    以字典格式返回class数据的基类
    '''
    def __init__(self):
        pass
    def getDict(self):
        return self.__dict__


class DataBase(DictDataBase):
    '''
    定义base数据类，所有模板共用的数据放在这里
    '''
    def __init__(self):
        self.settings = web_settings
        self.login_state = {}


class IndexData(DataBase):
    '''
    定义供首页用的数据
    '''
    def __init__(self):
        super(IndexData, self).__init__()
        pass


class JobDesc(DictDataBase):
    '''
    工作tag数据描述类
    '''
    def __init__(self, *args, **kwargs):
        self.href = kwargs.get('href') or '#'
        self.name = kwargs.get('name') or ''


class BookDesc(DictDataBase):
    '''
    推荐数据数据描述类
    '''
    def __init__(self, *args, **kwargs):
        self.href = kwargs.get('href') or '#'
        self.name = kwargs.get('name') or ''
        self.img_src = kwargs.get('img_src') or ''


class IntroductData(DataBase):
    '''
    定义供入门介绍页用的数据
    其中，job_tags和book_list是数组，存放字典
    ~~~~~~JobDesc~~~~BookDesc~~~~
    '''
    def __init__(self):
        super(IntroductData, self).__init__()
        self.job_tags = []
        self.book_list = []

    def addJobTag(self, *args, **kwargs):
        self.job_tags.append(JobDesc(*args, **kwargs).getDict())
    
    def addJobTagObj(self, jobTag):
        self.job_tags.append(jobTag.getDict())
    
    def addBookDesc(self, *args, **kwargs):
        self.book_list.append(BookDesc(*args, **kwargs).getDict())

    def addBookDescObj(self, bookDesc):
        self.book_list.append(bookDesc.getDict())


class QuestionDesc(DictDataBase):
    '''
    题目描述类
    '''
    def __init__(self, *args, **kwargs):
        self.qnum = kwargs.get('qnum') or 0
        self.qurl = kwargs.get('qurl') or '#'
        self.qname = kwargs.get('qname') or ''
        self.difficulty = kwargs.get('difc') or ''
        self.acceptance = kwargs.get('accep') or ''
        self.advisable = kwargs.get('advi') or False


class QuesTagDesc(DictDataBase):
    '''
    题目标签描述类
    '''
    def __init__(self, *args, **kwargs):
        self.href = kwargs.get('href') or '#'
        self.nums = kwargs.get('nums') or 0
        self.tag = kwargs.get('tag') or ''

class AlgorithmData(DataBase):
    '''
    算法题目汇总页数据描述类
    '''
    def __init__(self):
        super(AlgorithmData, self).__init__()
        self.qlist = []
        self.tag_list = []
        self.state = {}

    def addQuestion(self, *args, **kwargs):
        self.qlist.append(QuestionDesc(*args, **kwargs).getDict())

    def addQuestionObj(self, quest):
        self.qlist.append(quest.getDict())

    def addTag(self, *args, **kwargs):
        self.tag_list.append(QuesTagDesc(*args, **kwargs).getDict())

    def addTagObj(self, quesTag):
        self.tag_list.append(quesTag.getDict())

    def setState(self, fqnum, tqnum, pnum):
        self.state = {
            'finish_qnum': fqnum,
            'total_qnum': tqnum,
            'page_num': pnum,
        }


class ProjTagDesc(DictDataBase):
    '''
    项目标签描述类
    '''
    def __init__(self, *args, **kwargs):
        self.href = kwargs.get('href') or '#'
        self.name = kwargs.get('name') or ''

class ProjTermDesc(DictDataBase):
    '''
    项目描述类
    '''
    def __init__(self, *args, **kwargs):
        self.imgurl = kwargs.get('imgurl') or '#'
        self.title = kwargs.get('title') or ''
        self.desc_p1 = kwargs.get('desc_p1') or ''
        self.desc_p2 = kwargs.get('desc_p2') or ''
        self.num = kwargs.get('num') or 0
        self.lang = kwargs.get('lang') or ''
        self.autor = kwargs.get('autor') or ''
        self.detailurl = kwargs.get('detailurl') or '#'
        self.discussurl = kwargs.get('discussurl') or '#'
        self.crurl = kwargs.get('crurl') or '#'

class ProjectsData(DataBase):
    '''
    练习项目数据描述类
    '''
    def __init__(self):
        super(ProjectsData, self).__init__()
        self.tag_list = []
        self.proj_terms = []

    def addTag(self, *args, **kwargs):
        self.tag_list.append(ProjTagDesc(*args, **kwargs).getDict())

    def addTagObj(self, projTag):
        self.tag_list.append(projTag.getDict())

    def addProjTerm(self, *args, **kwargs):
        self.proj_terms.append(ProjTermDesc(*args, **kwargs).getDict())
   
    def addProjTermObj(self, projTerm):
        self.proj_terms.append(projTerm.getDict())


class LangDesc(DictDataBase):
    '''
    语言描述类
    '''
    def __init__(self, *args, **kwargs):
        self.val = kwargs.get('val') or ''
        self.name = kwargs.get('name') or ''

class QuestionData(DataBase):
    '''
    问题详情数据描述类
    '''
    def __init__(self, *args, **kwargs):
        super(QuestionData, self).__init__()
        self._setData(*args, **kwargs)
        self.lang_list = []

    def _setData(self, *args, **kwargs):
        self.qtitle = kwargs.get('qtitle') or ''
        self.discussurl = kwargs.get('discussurl') or '#'
        self.rand_question = kwargs.get('rand_question') or '#'
        self.qcontent = kwargs.get('qcontent') or ''
        self.qexample = kwargs.get('qexample') or ''

    def addQuestionDetailData(self, *args, **kwargs):
        self._setData(*args, **kwargs)

    def addLang(self, *args, **kwargs):
        self.lang_list.append(LangDesc(*args, **kwargs).getDict())

    def addLangObj(self, lang):
        self.lang_list.append(lang.getDict())


class ProjTermData(DataBase):
    '''
    项目详情描述类
    '''
    def __init__(self, *args, **kwargs):
        super(ProjTermData, self).__init__()
        self._setData(*args, **kwargs)
        
    def _setData(self, *args, **kwargs):
        self.ptitle = kwargs.get('ptitle') or ''
        self.discussurl = kwargs.get('discussurl') or '#'
        self.rand_question = kwargs.get('rand_question') or '#'
        self.pcontent = kwargs.get('pcontent') or ''
        self.ptodo = kwargs.get('ptodo') or ''

    def addProjTermData(self, *args, **kwargs):
        self._setData(*args, **kwargs)

class DiscussData(DataBase):
    '''
    讨论页数据接口类
    '''
    def __init__(self):
        super(DiscussData, self).__init__()
        pass
    
