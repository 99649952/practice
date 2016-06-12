#!/usr/bin/env python
#coding:utf-8
__author__ = '123'

import subprocess

def cpu(): #执行Linux系统命令返回一个包含结果的字典
    shell_command = 'sar 1 3| tail -1'
    try:
        result = subprocess.check_output(shell_command,shell=True)
        user,nice,system,iowait,steal,idle = result.split()[2:]
        value_dic= {
            'user': user,
            'nice': nice,
            'system': system,
            'iowait': iowait,
            'steal': steal,
            'idle': idle,
        }
    except Exception,e:
        value_dic = {'status':e}
    return value_dic

