#!/usr/bin/env python
#coding:utf-8
__author__ = '123'
import SocketServer
import os
import hmac
import json
import logging
from time import sleep

def logger():
    logging.basicConfig(level=logging.DEBUG,
    				format='%(asctime)s %(levelname)s %(message)s',
    				datefmt='%Y/%m/%d %H:%M:%S',
    				filename='myapp.log',
    				filemode='a')

def fileread(file): #读取文件内容
    try:
        with open(file,'rb') as f:
            return json.load(f)
    except Exception:
        return {}

def filewrite(file,content): #写入文件
    with open(file,'wb') as f:
        json.dump(content,f)

class MyFtpServer(SocketServer.BaseRequestHandler):#继承BaseRequestHandler基类，然后重写handle方法，在handle方法里实现与客户端的所有交互
    def handle(self):
        i = 0
        while i<3:
            user=self.request.recv(1024).strip()
            userinfo=fileread('user.json')
            if userinfo.has_key(user.split()[0]): #如果用户在字典中
                mpasswd = hmac.new(user.split()[0]) #加自定义key
                mpasswd.update(user.split()[1]) #将密码加密
                h_passwd=mpasswd.hexdigest()
                if h_passwd == userinfo[user.split()[0]][0]: #比对用户加密后的密码是否与字典中的相同
                    results='login successful'
                    self.request.sendall(results)
                    login=True
                    break
                else:
                    i = i + 1
                    results='Error:password not correct' #密码不存在
                    self.request.sendall(results)
                    continue
            else: #用户不存在
                self.request.sendall('user not exist')
        else: #当密码输错三次以上
            results = 'Error:Wrong password too many times'
            self.request.sendall(results)
            login=False
        home_path = os.getcwd() + '/' + user.split()[0] #用户的家目录
        current_path = '/' #当前目录
        logger() #日志格式
        while True:
            if login: #标签为True成功进入操作
                print 'home_path:%s=current_path:%s' %(home_path,current_path)
                cmd=self.request.recv(1024).strip() #接受数据
                logger()
                logging.info('user:%s cmd:%s path:%s%s'%(user.split()[0],cmd,home_path,current_path))
                if cmd == 'quit':
                    break

                elif cmd == 'dir': #发送当前目录下的文件和文件夹
                    list=os.listdir('%s%s' %(home_path,current_path))
                    if list: #其实可以不用区分文件和文件夹，为了把文件和文件夹的颜色区分开
                        dirlist,filelist = '',''
                        for i in list:
                            if os.path.isdir('%s%s%s' %(home_path,current_path,i)):
                                dirlist = dirlist + '\033[32m' + i + '\033[m\t'
                            else:
                                filelist = filelist + i + '\t'
                        results = dirlist + filelist
                    else:
                        results = '\033[31mnot find\033[m'
                    self.request.sendall(results)

                elif cmd == 'pdir':#发送当前目录
                    self.request.sendall(current_path)

                elif cmd.split()[0] == 'mdir': #用于创建目录
                    if cmd.split()[1].isalnum():# 如果字符串至少有一个字符并且所有字符都是字母或数字则返回True
                        tmppath='%s%s%s' %(home_path,current_path,cmd.split()[1])
                        os.makedirs(tmppath)
                        self.request.sendall('\033[32mcreating successful\033[m')
                    else:
                        self.request.sendall('\033[31mcreate failure\033[m')

                elif cmd.split()[0] == 'cdir': #跳转目录处理
                    if cmd.split()[1] == '/' : #如果请求是/或开头是/
                        tmppath='%s%s' %(home_path,cmd.split()[1])
                        if os.path.isdir(tmppath):
                            current_path = cmd.split()[1] #当前目录就等于用户输入目录
                            self.request.sendall(current_path) #返回路径数据
                        else:
                            self.request.sendall('\033[31mnot_directory\033[m')
                    elif cmd.split()[1].startswith('/'):
                        tmppath='%s%s' %(home_path,cmd.split()[1])
                        if os.path.isdir(tmppath):
                            current_path = cmd.split()[1] + '/'
                            self.request.sendall(current_path)  #返回/
                        else:
                            self.request.sendall('\033[31mnot_directory\033[m')
                    else:
                        tmppath='%s%s%s' %(home_path,current_path,cmd.split()[1])
                        if os.path.isdir(tmppath):
                            current_path = current_path + cmd.split()[1] + '/'
                            self.request.sendall(current_path)
                        else:
                            self.request.sendall('\033[31mnot_directory\033[m')

                elif cmd.split()[0]== 'get': #获取文件处理
                    if os.path.isfile('%s%s%s' %(home_path,current_path,cmd.split()[1])): #如果文件存在
                        with open('%s%s%s' %(home_path,current_path,cmd.split()[1]),'rb') as f:
                            self.request.sendall('ready_file')
                            sleep(0.5) #防止缓存区内容一起发送
                            self.request.send(f.read()) #发送文件内容
                        sleep(0.5)
                    else:
                        self.request.sendall('inexistence')
                        continue
                    self.request.sendall('get_done')#当发送这个时说明内容已经发完

                elif cmd.split()[0] == 'send': #发送文件处理
                    with open('%s%s%s' %(home_path,current_path,cmd.split()[1]),'wb') as f:
                        while True: #循环接收文件
                            data=self.request.recv(1024)
                            if data == 'file_send_done':break #如果收到跳出
                            f.write(data)
                        self.request.sendall('receive_end')
                else:
                    results = cmd.split() + ': Command not found'
                    self.request.sendall(results)

if __name__ == '__main__':
    HOST,PORT = '127.0.0.1',6666 #绑定端口和ip
    server = SocketServer.ThreadingTCPServer((HOST,PORT),MyFtpServer) #将写的类加入多线程处理
    server.serve_forever() #循环启动
