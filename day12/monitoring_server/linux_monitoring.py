#!/usr/bin/env python
#coding:utf-8
__author__ = '123'

class cpu(object): #cpu监控指标
    def __init__(self):
        self.name = 'linux_cpu'
        self.interval = 30
        self.plugin_name = 'cpu_check'
        self.triggers = {
                'idle':{
                        'minutes': 15,
                        'warning':20,
                        'critical':5,
                        },
                'iowait':{
                        'minutes': 10,
                        'warning':40,
                        'critical':50,
                        },
                         }

class memory(object):
    def __init__(self):
        super(memory,self).__init__()
        self.name = 'linux_memory'
        self.interval = 30
        self.plugin_name = 'get_memory_info'
        self.triggers = {
                'usage':{
                        'minutes': 15,
                        'warning':80,
                        'critical':90,
                        }
                         }