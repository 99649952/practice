#_*_coding:utf-8_*_
__author__ = 'Alex Li'

import main
import json,os
import hashlib
from conf import settings
import time
import SocketServer
import logging


class MyTCPHandler(SocketServer.BaseRequestHandler):
    #继承BaseRequestHandler基类，然后必须重写handle方法，并且在handle方法里实现与客户端的所有交互
    print('\033[32;1mStarting CrazyFTP server on %s:%s ......\n\033[0m' %(main.settings.BIND_HOST,main.settings.BIND_PORT))
    response_code_list = {
        '200': "Pass authentication!",
        '201': "Wrong username or password",
        '202': "Invalid username or password",
        '300': "Ready to send file to client",
        '301': "Client ready to receive file data ",
        '302': "File doesn't exist",
        '303': "Ready to put file to server",
        '304': "Ready accept rece from server"
    }

    def handle(self):   #socket交互主方法   1,
        while  True:
            data = self.request.recv(1024) #接收1024字节数据,收到的数据不一定是1024,根据客户端实际发过来的大小来定
            if not data:
                print("\033[31;1mHas lost client\033[0m", self.client_address)
                break     #如果收不到客户端数据了（代表客户端断开了），就断开
            self.instruction_allowcation(data) #客户端发过来的数据统一交给功能分发器处理    2，

    def instruction_allowcation(self,instructions):
        '''功能分发器,负责按照客户端的指令分配给相应的函数处理'''
        instructions = instructions.split("|") #分割发过来的指令
        function_str = instructions[0] # 客户端发过来的指令中,第一个参数都必须在服务器端有相应的方法处理
        if hasattr(self,function_str): #如果对象存在处理指令的方法
            self.logger()
            logging.info('%s%s'%(self.user_auth,instructions))
            func = getattr(self,function_str) #获取相应的方法
            func(instructions) #执行方法
        else:
            print("\033[31;1mReceived invalid instruction [%s] from client!\033[0m" %(instructions))

    def pdir(self,user_data):
        self.request.sendall(self.current_path)

    def dir(self,user_data): #目录内容
        list=os.listdir('%s%s' %(self.HOME_FILE,self.current_path))
        print(list)
        if list: #其实可以不用区分文件和文件夹，为了把文件和文件夹的颜色区分开
            dirlist,filelist = '',''
            for i in list:
                if os.path.isdir('%s%s%s' %(self.HOME_FILE,self.current_path,i)):
                    dirlist = dirlist + '\033[32m' + i + '\033[m\t'
                else:
                    filelist = filelist + i + '\t'
            results = dirlist + filelist
        else:
            results = '\033[31mnot find\033[m'
        self.request.sendall(results)

    def cdir(self,user_data): #切换目录
        if user_data.split()[1] == '/' : #如果请求是/
            tmppath='%s%s' %(self.HOME_FILE)
            if os.path.isdir(tmppath):
                self.current_path='/'
                current_path = self.current_path #当前目录就等于用户输入目录
                self.request.sendall(current_path) #返回路径数据
            else:
                self.request.sendall('\033[31mnot_directory\033[m')
        elif user_data.split()[1].startswith('/'):
            tmppath='%s%s' %(self.HOME_FILE,user_data.split()[1])
            if os.path.isdir(tmppath):
                self.current_path=user_data.split()[1]
                current_path = user_data.split()[1] + '/'
                self.request.sendall(current_path)  #返回/
            else:
                self.request.sendall('\033[31mnot_directory\033[m')
        else:
            tmppath='%s%s%s' %(self.HOME_FILE,self.current_path,user_data.split()[1])
            if os.path.isdir(tmppath):
                current_path = self.current_path + user_data.split()[1] + '/'
                self.request.sendall(current_path)
            else:
                self.request.sendall('\033[31mnot_directory\033[m')

    def file_put(self,user_data):
        file_name = user_data[1] #要上传的文件名
        file_abs_path = "%s/%s" %(self.HOME_FILE,file_name)
        response_str,code,file_size,file_md5 = self.request.recv(1024).split("|") #接收内容分割字符串
        if code == "303": #ready to get file #状态码是300
            self.request.send("response|304") #
            total_file_size = int(file_size) #要接收的文件大小
            received_size = 0  #接受到多少
            print(file_abs_path)
            with open(file_abs_path,"wb") as local_file_obj: #打开文件,将文件写入到var/users下
                while total_file_size != received_size: #总大小不等于接收到大小继续执行
                    data = self.request.recv(4096) #接收数据
                    received_size += len(data) #接收到内容增加
                    local_file_obj.write(data) #将接收到内容写入文件
                    print("recv size:", total_file_size,received_size)
                else:
                    print("\033[32;1m----file download finished-----\033[0m") #接收完毕

    def file_get(self,user_data):
        print("\033[32;1m---client get file----\033[0m")
        if self.login_user : #make sure user is logined first
            filename_with_path = json.loads(user_data[1]) #将传来的字符串加载进内存
            file_abs_path = "%s/%s/%s" %(settings.USER_HOME,self.login_user, filename_with_path) #在服务端的路径
            print file_abs_path
            if os.path.isfile(file_abs_path): #文件存在
                # send back to client [response_str,code,file_size,file_md5]
                file_size = os.path.getsize(file_abs_path) #获得文件大小
                response_msg = "response|300|%s|n/a" %(file_size)  # 状态码，文件大小
                self.request.send(response_msg) #发送状态码文件大小
                client_response = self.request.recv(1024).split("|")
                print '-->',client_response
                if client_response[1] == "301": #client ready recv file data
                    sent_size = 0 #发送初始值为0
                    f = open(file_abs_path,"rb")
                    #file_md5 = hashlib.md5()
                    t_start = time.time()
                    while file_size != sent_size: #发送内容不等于文件大小
                        data = f.read(4096) #
                        self.request.send(data) #发送文件
                        sent_size += len(data) #发送大小增加
                        #file_md5.update(data)
                        print("send:",file_size,sent_size)
                    else:
                        #md5_str = file_md5.hexdigest()
                        t_cost = time.time() - t_start
                        print "----file transfer time:---",t_cost
                        print("\033[32;1m----successfully sent file to client----\033[0m")
                        #print("\033[32;1m---- file md5 [%s]----\033[0m" %md5_str)
                        f.close()
            else:
                response_msg = "response|302|n/a|n/a"
                self.request.send(response_msg)

    def user_auth(self,data): #用户认证
        #try:
        auth_info = json.loads(data[1]) #将发过来的字符串转换为字典
        auth_info['username']
        auth_info['password']
        if auth_info['username'] in settings.USER_ACCOUNT:
            #如果配置文件的中的用户密码用客户端传来的一致
            if settings.USER_ACCOUNT[auth_info['username']]['password'] == auth_info['password']:
                #pass authentication
                response_code = '200' #状态码200
                self.login_user = auth_info['username'] #将用户名赋值给对象字段
                self.HOME_FILE='%s%s'%(settings.USER_HOME,self.login_user)
                self.current_path='/'
            else:
                #wrong username or password
                response_code = '201'
        else:
            response_code = '202'
            #invalid username or password
        #except
        #将状态吗，和状态吗代表的信息发送给客户端
        response_str = "response|%s|%s" %(response_code,self.response_code_list[response_code])
        self.request.send(response_str)
        return  response_code
    def logger(self):
        logging.basicConfig(level=logging.DEBUG,
        				format='%(asctime)s %(levelname)s %(message)s',
        				datefmt='%Y/%m/%d %H:%M:%S',
        				filename='myapp.log',
        				filemode='a')
