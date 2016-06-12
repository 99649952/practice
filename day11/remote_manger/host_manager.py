#!/usr/bin/env python
#coding:utf-8
__author__ = '123'

from mysql_op import Mysql_Manger


class Host_Manager(object):

    def __init__(self,group):
        self.group=group

    def Fetch_member_information(self): #从数据库提取文件
        reCount = "select ip,port,host_account,host_passwd from host where hostgroup = '%s'"%self.group
        self.data_return=Mysql_Manger().Fetch_sql(reCount) #主机成员信息序列

    def add_ip_to_list(self):
        self.ip_list=[]  #存取ip地址
        for i in self.data_return:
            self.ip_list.append(i['ip'])

    def __show_ip(self):
        print('group_memeber:')
        for i in self.ip_list:
            print(i)

    def menu(self): #操作模式选择菜单
        self.__show_ip()
        print('''
        1:batch_manager
        2:single_op
        ''')
        op=raw_input('please select one:')
        return op

    def single(self): #但用户操作登录信息提取
        for i in self.ip_list:
            print(i)
        op=raw_input('Please select a IP to manager>>>')
        recount="select ip,port,host_account,host_passwd,hostgroup from host where ip = '%s'and hostgroup='%s'"%(op,self.group)
        fetch_result=Mysql_Manger().Fetch_sql(recount)
        return fetch_result[0]
