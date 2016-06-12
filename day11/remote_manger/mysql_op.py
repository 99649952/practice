#!/usr/bin/env python
#coding:utf-8
__author__ = '123'

import MySQLdb

class Mysql_Manger(object): #mysql交互

    def __init__(self,host='192.168.10.143',user='lxb',password='0l.0l.',db='bastion_host',): #初始化链接基础信息
        self.host=host
        self.user=user
        self.password=password
        self.db=db
        self.__connect()

    def __connect(self):#连接数据库
        self.conn=MySQLdb.connect(self.host,self.user,self.password,self.db)
        self.cur = self.conn.cursor(MySQLdb.cursors.DictCursor)#

    def __close(self): #关闭连接
        self.cur.close()
        self.conn.close()

    def Fetch_sql(self,recount): #提取数据
        self.cur.execute(recount)
        data=self.cur.fetchall()
        self.__close()
        return data

    def Isert_sql(self,recount):
        pass

    def Delete_sql(self,recount):
        pass

    def Update_sql(self,recount):
        pass
