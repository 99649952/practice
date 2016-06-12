#!/usr/bin/env python
#coding:utf-8
__author__ = '123'
import json
import sys
import hmac
import os

def fileread(file): #读取文件内容
    try:
        with open(file,'rb') as f:
            return json.load(f)
    except Exception:
        return {}

def filewrite(file,content): #写入文件
    with open(file,'wb') as f:
        json.dump(content,f)

def user_op_menu(): #操作菜单
    print '''
        1.add user
        2.del user
        3.query user
        0.exit
        '''
    i = raw_input('>>>').strip()
    if i in str(range(5)):
        return i
    else:
        print('op error')
        return user_op_menu()

def op_result():
    op=user_op_menu()
    userinfo=fileread('user.json')
    if op == '1': #添加用户
        user=raw_input('user name:').strip()
        passwd=raw_input('passwd:').strip()
        passwd1=raw_input('Confirm password:').strip()
        if passwd == passwd1:
            mpasswd = hmac.new(user) #加自定义key
            mpasswd.update(passwd) #将密码加密
            h_passwd=mpasswd.hexdigest()
            userinfo[user] = [h_passwd]
            if not os.path.isdir(user):
                os.mkdir(user)
            print '%s creating successful ' %user

    elif op == '2': #删除用户
        user=raw_input('user name:').strip()
        if userinfo.has_key(user):
            del userinfo[user]
            os.removedirs(user)
            print 'Delete users successfully'
        else:
            print 'user not exist'

    elif op == '3': #打印用户
        for i in userinfo.keys():
            print(i)

    elif op == '0':
        sys.exit()

    filewrite('user.json',userinfo) #将修改写入文件

while 1:
    op_result()



