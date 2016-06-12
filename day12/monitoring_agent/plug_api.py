#!/usr/bin/env python
#coding:utf-8
__author__ = '123'

import cpu_check

'''调用监控插件'''

def get_cpu(): #调用cpu检测插件
    return cpu_check.cpu()