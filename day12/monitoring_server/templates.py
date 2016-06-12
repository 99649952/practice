#!/usr/bin/env python
#coding:utf-8
__author__ = '123'

import linux_monitoring

'''模板'''

class linux_template(object):

    def __init__(self):
        self.hosts=[]
        self.name = 'LinuxTemplate'
        self.services= [
                        linux_monitoring.cpu, #监控指标类
                        ]

class linux_base_check(object):

    def __init__(self):
        self.hosts=[]
        self.name = 'LinuxTemplate'
        self.services= [
                        linux_monitoring.cpu,
                        linux_monitoring.memory,
                        ]

