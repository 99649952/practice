#!/usr/bin/env python
#coding:utf-8
__author__ = '123'
import ssh_cmd
import os

class  ArgvHandler(object):
    def __init__(self,args):
        self.args = args #启动模块传入的参数start、stop
        self.argv_parser() #传入参数处理

    def argv_parser(self):
        if len(self.args) < 2: #参数小于两个
            self.help_msg()
        else:
            first_argv = self.args[1]
            if hasattr(self,first_argv): #在对象有这个成员
                func = getattr(self,first_argv) #获取这个成员
                func() #执行成员
            else:
                self.help_msg()

    def help_msg(self): #启动主函数时
        msg = '''
        start   :start ssh server
        stop    :stop ssh server                '''
        print(msg)

    def file_help(self):
        msg='''
        get [target_file] [local_file]    :get target file
        put [local_file] [target_file]    :put local file
        '''
        print msg

    def start(self): #交互逻辑
        while True:
            cmd=raw_input('cmd:')
            if len(cmd)==0:continue
            if cmd.split()[0]=='put':
                if len(cmd.split()) == 3:
                    ssh_cmd.op_file(cmd) #调用文件操作函数
                    continue
                else:
                    self.file_help()
                    continue
            ssh_cmd.conn_host(cmd) #调用并发执行系统命令函数

