# -*-coding:utf-8-*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User_Login(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    def __unicode__(self):
        return self.username

class UserInfo(models.Model):
    '''
    账户信息表
    '''
    username = models.OneToOneField(User_Login)
    user = models.CharField(max_length=32)
    groups = models.ManyToManyField('UserGroup')
    def __unicode__(self):
        return self.user

class UserGroup(models.Model):
    '''
    用户组
    '''
    group_name = models.CharField(max_length=64,unique=True)
    def __unicode__(self):
        return self.group_name

class Article(models.Model):
    '''
    帖子
    '''
    title = models.CharField(u"文章标题",max_length=255,unique=True)
    category = models.ForeignKey("Category",verbose_name=u"板块")
    head_img = models.ImageField(upload_to="uploads",null=True,blank=True)
    summary = models.CharField(max_length=255)
    content = models.TextField(u"内容")
    author = models.ForeignKey(UserInfo)
    publish_date = models.DateTimeField(auto_now=True)
    hidden = models.BooleanField(default=True)
    priority = models.IntegerField(u"优先级",default=1000)

    def __unicode__(self):
        return "<%s, author:%s>" %(self.title,self.author)

class Comment(models.Model):
    '''
    评论
    '''
    article = models.ForeignKey(Article)
    user = models.ForeignKey(UserInfo)
    #parent_comment = models.ForeignKey('Comment',)
    parent_comment = models.ForeignKey('self',related_name='p_comment',blank=True,null=True)
    comment = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return "<%s, user:%s>" %(self.comment,self.user)

class ThumbUp(models.Model):
    '''
    点赞
    '''
    article = models.ForeignKey('Article')
    user = models.ForeignKey(UserInfo)
    date = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return "<user:%s>" %(self.user)

class Category(models.Model):
    '''
    帖子版块
    '''
    category_name = models.CharField(max_length=64,unique=True)
    category_admin = models.ManyToManyField(UserInfo,blank=True,null=True)
    def __unicode__(self):
        return self.category_name



