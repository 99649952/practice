#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = '李晓波'

from linux import sysinfo


#调用相应收集处理函数

def LinuxSysInfo():
    #print __file__
    return  sysinfo.collect()


def WindowsSysInfo():
    from windows import sysinfo as win_sysinfo
    return win_sysinfo.collect()
