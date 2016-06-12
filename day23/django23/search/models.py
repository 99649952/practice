# -*-coding:utf-8-*-
from __future__ import unicode_literals
from django.db import models


class Host(models.Model):
    '''
    主机
    '''
    hostname = models.CharField(max_length=25)
    ip = models.GenericIPAddressField(max_length=30)
    port = models.IntegerField(default=80)
    description = models.CharField(max_length=255, default="nothing...")

    def __unicode__(self):
        return self.hostname


class HostGroup(models.Model):
    '''
    主机组
    '''
    group_name = models.CharField(max_length=25)
    group_member = models.ManyToManyField(Host,through='HostGroupRelevance')

    def __unicode__(self):
        return self.group_name


class HostGroupRelevance(models.Model):
    '''
    主机与主机组对应表
    '''
    host = models.ForeignKey(Host)
    group = models.ForeignKey(HostGroup)

    def __unicode__(self):
        return '主机：%s 主机组：%s' % (self.host.hostname, self.group.group_name)
