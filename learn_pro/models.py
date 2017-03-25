# -*- coding: utf-8 -*-
from django.db import models
import logging

logger = logging.getLogger('django.models')

# Create your models here.
# book相关表
class Book(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    classify = models.CharField(max_length=10)
    #coverurl = models.ImageField()

    def __str__(self):
        return self.name


class ProposeBook(models.Model):
    bookid = models.ForeignKey(Book)
    propnum = models.IntegerField()
    isprops = models.NullBooleanField()


class BookDiscusses(models.Model):
    bookid = models.ForeignKey(Book)
    discuss = models.TextField()
    propsindex = models.IntegerField()


# 基础知识相关表
class KnowledgeQuestion(models.Model):
    question = models.CharField(max_length=200)
    desc = models.TextField()
    answer = models.TextField()


class QuestionDiscuss(models.Model):
    knowledgeid = models.ForeignKey(KnowledgeQuestion)
    discuss = models.TextField()
    propsindex = models.IntegerField()


# 编程题库表
class Program(models.Model):
    title = models.CharField(max_length=300)
    source = models.CharField(max_length=20)


class ProgramAnswers(models.Model):
    programid = models.ForeignKey(Program)
    answer = models.TextField()
    language = models.CharField(max_length=20)
    isprops = models.BooleanField()


class programAnsDiscuss(models.Model):
    answerid = models.ForeignKey(ProgramAnswers)
    discuss = models.TextField()
    propsindex = models.IntegerField()


# 项目题库表
class Project(models.Model):
    title = models.CharField(max_length=300)
    desc = models.TextField()
    tips = models.TextField()


class ProjectProcess(models.Model):
    projectid = models.ForeignKey(Project)
    answer = models.TextField()
    reviewer = models.CharField(max_length=50)


class ProjectDiscuss(models.Model):
    projectid = models.ForeignKey(Project)
    processid = models.ForeignKey(ProjectProcess)
    discuss = models.TextField()
    propsindex = models.IntegerField()

