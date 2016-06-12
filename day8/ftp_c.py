#!/usr/bin/env python
#coding:utf-8
__author__ = '123'
import socket
import os
from time import sleep

HOST='127.0.0.1'
PORT=6666
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

while True:
    login=False #标签
    user = raw_input('user:').strip()
    while True:
        passwd = raw_input('passwd:').strip()
        s.sendall(user + ' ' + passwd) #将用户名和密码发送到服务端
        servercmd=s.recv(1024) #收到的回复
        if servercmd == 'login successful': #服务端返回login successful
            print '\033[32m%s\033[m' %servercmd
            login=True #标签变为True
            break
        else: #即认证失败
            print servercmd
            break
    if login==True:
        current_dir=''
        while True: #如果命令为空继续输入
            cmd=raw_input('<FTP:%s>'%current_dir).strip()
            if cmd == '': #如果为空继续输入
                continue

            elif cmd.split()[0] == 'help':
                print '''
                get [file]          --获取服务器的文件或目录
                send [file]         --给服务器发送文件或目录
                dir                 --列出服务器当前目录的文件
                pdir                --查看服务器当前的目录
                mdir [dir]          --在服务器创建目录
                cdir [dir]          --跳转到相应的目录
                pwd                 --打印客户端当前目录
                cd [dir]            --改变自己当前的目录
                ls                  --打印自己当前目录里的内容
                help                --打印帮助信息
                quit                --退出客户端
                '''
                continue

            elif cmd.split()[0] == 'cdir': #在服务端切换目录
                if cmd == 'cdir':continue
                s.sendall(cmd)
                data=s.recv(1024)
                current_dir=data
                print data
                continue

            elif cmd == 'dir': #列出服务器上指定目录的文件
                s.sendall(cmd)
                data=s.recv(1024)
                print data
                continue

            elif cmd == 'pdir': #服务器当前的目录
                s.sendall(cmd)
                data=s.recv(1024)
                print data
                continue

            elif cmd.split()[0] == 'mdir': #用于在服务端创建目录
                if cmd == 'mdir':continue
                s.sendall(cmd)
                data=s.recv(1024)
                print data
                continue

            elif cmd.split()[0] == 'ls': #打印相应目录下的文件和文件夹，不加目录，打印当前目录
                if cmd == 'ls':
                    for i in os.listdir(os.getcwd()):print i
                    continue
                else:
                    if os.path.isdir(cmd.split()[1]):
                        for i in os.listdir(cmd.split()[1]):print(i)
                        continue

            elif cmd == 'pwd':#自己当前的目录
                print(os.getcwd())

            elif cmd.split()[0] == 'cd': #改变自己当前的目录
                try:
                    os.chdir(cmd.split()[1])
                except:
                    print '\033[31mcd failure\033[m'

            elif cmd.split()[0] == 'get': #从服务端获取文件
                if cmd == 'get':continue
                s.sendall('get ' + cmd.split()[1])
                servercmd=s.recv(1024)
                if servercmd == 'inexistence': #不存在
                    print '%s \t\033[32minexistence\033[m' %cmd.split()[1]
                elif servercmd == 'ready_file': #收到信号说明文件存在
                    with open(cmd.split()[1],'wb') as f:
                        while True: #循环接收文件
                            data=s.recv(1024)
                            if data == 'get_done':break #收到说明文件接收完毕
                            f.write(data)
                    print '%s \t\033[32mfile_done\033[m' %(cmd.split()[1])
                continue

            elif cmd.split()[0] == 'send': #往服务端发送文件
                if cmd == 'send':continue
                if os.path.isfile(cmd.split()[1]): #本地存在文件
                    s.sendall('send ' + cmd.split()[1])
                    with open(cmd.split()[1],'rb') as f:
                        s.send(f.read())
                        sleep(0.5)
                        s.sendall('file_send_done')
                        if s.recv(1024) == 'receive_end': #收到文件接收完毕信号
                            print '%s\t\033[32mput file done\033[m' %(cmd.split()[1])
                else:
                    print '%s\t\033[31munknown file\033[m' %cmd.split()[0]
                    continue
                sleep(0.5)

            elif cmd == 'quit':
                break
            else:
                print '\033[31m%s: Command not found,Please see the "help"\033[m' %cmd
        s.close()