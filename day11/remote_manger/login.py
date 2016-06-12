#!/usr/bin/env python
#coding:utf-8
__author__ = '123'

from mysql_op import Mysql_Manger
from host_manager import Host_Manager
from ssh_connect import conn_host
from demo import single_shell


def logon_host(op,object):
    if op=='1':
        while True:
            cmd=raw_input('cmd:')
            if len(cmd)==0:continue
            conn_host(cmd,object.data_return) #host信息传入用于批量处理命令
    elif op == '2':
        single_result=object.single()
        single_shell(single_result['ip'],single_result['port'],single_result['host_account'],single_result['host_passwd'],single_result['hostgroup'])

def Fetch_host_infomation(group):
    host_object=Host_Manager(group) #实例化类传入用户的属组
    host_object.Fetch_member_information()
    host_object.add_ip_to_list()
    op=host_object.menu()
    logon_host(op,host_object)

def logon_manager():
    count=0
    while count<3:
        mysql_op=Mysql_Manger()
        user=raw_input('please input your account >>>').strip()
        passwd=raw_input('please input your password >>>').strip()
        reCount = "select account,passwd,hostgroup from user where account = '%s'"%user
        data_return=mysql_op.Fetch_sql(reCount) #返回序列
        if len(data_return) > 0: #序列大于0
            result_dict=data_return[0]
            if  result_dict['passwd']== passwd:
                print('logon successfully')
                Fetch_host_infomation(result_dict['hostgroup'])
                #host_object.menu()
                break
            else:
                count+=1
                print('logon faild!!!')
        else:
            print('logon faild!!!')

if __name__ == '__main__':
    logon_manager()

