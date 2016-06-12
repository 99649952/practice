#!/usr/bin/env python
#coding:utf-8

import socket
import sys
import paramiko
import interactive

def single_shell(ip,port,username,passwd,group): #开启交互终端用于用户操作
    if len(ip) == 0:
        print '*** Hostname required.'
        sys.exit(1)
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, int(port)))
    except Exception, e:
        print '*** Connect failed: ' + str(e)
        sys.exit(1)
    #登陆服务器
    try:
        t = paramiko.Transport(sock)
        try:
            t.start_client()
        except paramiko.SSHException:
            print '*** SSH negotiation failed.'
            sys.exit(1)
        t.auth_password(username, passwd)
        if not t.is_authenticated():
            print '*** Authentication failed. :('
            t.close()
            sys.exit(1)
        chan = t.open_session()# 打开一个通道
        chan.get_pty()#获取一个终端
        chan.invoke_shell()#激活器
        print '*** Here we go!'
        print
        interactive.interactive_shell(chan,ip,username,group)
        chan.close()
        t.close()
    except Exception, e:
        print '*** Caught exception: ' + str(e.__class__) + ': ' + str(e)
        try:
            t.close()
        except:
            pass
        sys.exit(1)


