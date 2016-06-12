#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = '李晓波'

from plugins import plugin_api
import json,platform,sys


class InfoCollection(object):
    def __init__(self):
        pass


    def get_platform(self):

        os_platform = platform.system()

        return os_platform


    def collect(self):
        os_platform = self.get_platform()   #获取系统类型
        try:
            func = getattr(self,os_platform)    #执行相应的系统处理方法
            info_data = func()
            formatted_data = self.build_report_data(info_data)
            return formatted_data
        except AttributeError,e:
            sys.exit("Error:MadKing doens't support os [%s]! " % os_platform)
    def Linux(self):
        sys_info = plugin_api.LinuxSysInfo()    #调用接口处理文件

        return sys_info

    def Windows(self):
        sys_info = plugin_api.WindowsSysInfo()#调用接口处理文件
        print sys_info
        #f = file('data_tmp.txt','wb')
        #f.write(json.dumps(sys_info))
        #f.close()
        return sys_info
    def build_report_data(self,data):

        #add token info in here before send

        return data
