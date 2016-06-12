#!/usr/bin/env python
#coding:utf-8
__author__ = '123'

import templates

'''主机实例化模板'''

group1 = templates.linux_base_check()
group1.hosts = ['192.168.10.22','192.168.10.80']  #主机绑定模板

group2 = templates.linux_template()
group2.hosts = ['192.168.10.22','192.168.10.80',]

group3 = templates.linux_template()
group3.hosts = ['192.168.10.80','192.168.10.81','192.168.10.82']

groups=[group3,group2,group1,]