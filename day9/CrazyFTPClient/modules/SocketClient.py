#_*_coding:utf-8_*_
__author__ = 'Alex Li'

import os,sys
import socket
import json
import hashlib
import time

BASE_DIR = '%s/var/users/'%os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Client(object):

    def __init__(self,sys_argv):
        self.args = sys_argv  #执行启动模块传入的参数  1,
        self.argv_parser() #传入参数判断参数    2,
        self.response_code = {
            '200': "pass user authentication",
            '201': "wrong username or password",
            '202': "invalid username or password",
            '300': "Ready to get file from server",
            '301': "Ready to send to  server",
            '302': "File doesn't exist on ftp server",
            '303': "Ready to put file to server",
            '304': "Ready accept rece from server"
        } #服务端返回状态码字典
        self.handle()  #连接服务端   3,
    def help_msg(self): #帮助提示
        msg = '''
        -s ftp_server_addr    :ftp server ip address, mandatory
        -p ftp_server_port    :ftp server port , mandatory
        '''
        print(msg)

    def instruction_msg(self):
        msg = '''
        get ftp_file        : download file from ftp server
        put local  remote   : upload local file to remote
        ls                  : list files on ftp server
        cd  path            : change dir on ftp server
        '''
    def argv_parser(self):#传入参数判断参数为端口和ip赋值
        if len(self.args) < 5: #参数小于五个
            self.help_msg()
            sys.exit()
        else:
            mandatory_fields = ["-p","-s"] # 参数内容存入列表
            for i  in mandatory_fields:
                if i not in self.args:#参数在列表中
                    sys.exit("\033[31;1mLack of argument [%s]\033[0m" % i)
            try:
                self.ftp_host = self.args[self.args.index("-s") + 1] #地址
                self.ftp_port = int(self.args[self.args.index("-p") + 1]) #端口
            except (IndexError,ValueError): #值错误索引错误
                self.help_msg()
                sys.exit()

    def connect(self,host,port):
        try:
            self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #实例化socket
            self.sock.connect((host,port)) #连接socket服务器
        except socket.error as e:
            sys.exit("\033[31;1m%s\033[0m" %e)

    def auth(self):
        retry_count = 0
        while retry_count < 3: #循环3次
            username = raw_input("\033[32;1mUsername:\033[0m").strip() #用户名
            if len(username) == 0 : continue
            password = raw_input("\033[32;1mPassword:\033[0m").strip() #密码
            if len(password) == 0 : continue
            raw_json = json.dumps({
                'username': username,
                'password': password
            }) #将用户名在内存中存为字符串
            auth_str = "user_auth|%s" %(raw_json) #指令加用户登录信息的字符串
            self.sock.send(auth_str) #发送字符串
            server_response = self.sock.recv(1024) #接收服务端消息消息
            response_code = self.get_response_code(server_response) #获取状态码
            print(self.response_code[response_code])  #打印状态码的内容
            if response_code == '200': #如果内容为200
                self.login_user = username #增加对象字段
                self.current_dir = "/" #用户登录自动在自己家目录即/
                return  True #登录成功返回True
            else:
                retry_count +=1 #失败次数加1
        else:
            sys.exit("\033[31;1mToo many attempts!\033[0m") #三次失败退出登录

    def get_response_code(self,response): #获取状态码
        response_code = response.split("|")
        code =response_code[1]
        return code

    def parse_instruction(self,user_input): #处理指令
        user_input_to_list = user_input.split()
        func_str = user_input_to_list[0] #取动作
        if hasattr(self,'instruction__'+ func_str): #存在方法
            return True,user_input_to_list
        else:
            return False,user_input_to_list

    def conn_help(self):
        print '''
        get [file]          --获取服务器的文件或目录
        send [file]         --给服务器发送文件或目录
        dir                 --列出服务器目录下的文件
        pdir                --查看服务器当前的目录
        mdir [dir]          --在服务器创建目录
        cdir [dir]          --跳转到相应的目录
        pwd                 --打印客户端当前目录
        cd [dir]            --改变自己当前的目录
        ls                  --打印自己当前目录里的内容
        help                --打印帮助信息
        quit                --退出客户端
        '''

    def interactive(self):
        self.logout_flag = False
        while  self.logout_flag is not True: #为False
            #用户交互并打印当前用户和所在目录
            user_input = raw_input("[%s@%s]" %(self.login_user,self.current_dir)).strip()
            if len(user_input) == 0:continue #输入长度为0继续输入
            status,user_input_instructions = self.parse_instruction(user_input) #返回处理的状态和指令列表   6,
            if status is True: #状态为True
                func = getattr(self,"instruction__" + user_input_instructions[0]) #获取方法
                func(user_input_instructions) #执行方法     7,
            else:
                self.conn_help()

    def instruction__dir(self,instructions):  # 查询服务器目录下的文件
        cmd=instructions[0]
        raw_str='dir|%s'%(cmd)
        self.sock.send(raw_str)
        data=self.sock.recv(1024)
        print data

    def instruction_pdir(self,instruction): #查看在服务器端的当前目录
        cmd=instruction[0]
        self.sock.sendall(cmd)
        data=self.sock.recv(1024)
        print data

    def instruction__cdir(self,instructions): #在服务端切换目录
        if len(instructions) == 2:
            cmd=instructions[1]
            raw_str='cdir|%s'%(cmd)
            self.sock.send(raw_str)
            data=self.sock.recv(1024)
            self.current_dir=data
            print data

    def instruction__put(self,instructions):
        if len(instructions) == 1:
            return
        local_file='%s%s'%(BASE_DIR,instructions[1]) #上传的文件名
        file_name=instructions[1]
        raw_str="file_put|%s" %(file_name)
        if os.path.isfile(local_file):
            self.sock.send(raw_str) #发送上传文件指令，和文件名
            file_size = os.path.getsize(local_file) #获得文件大小
            response_msg = "response|303|%s|n/a" %(file_size)  # 状态码，文件大小
            self.sock.send(response_msg) #发送状态码文件大小
            server_response = self.sock.recv(1024).split("|")
            print '-->',server_response
            if server_response[1]=='304': #'301': "Ready to send to  server",
                sent_size = 0 #发送初始值为0
                with open(local_file,"rb") as f:
                    #file_md5 = hashlib.md5()
                    t_start = time.time()
                    while file_size != sent_size: #发送内容不等于文件大小
                        data = f.read(4096)
                        self.sock.send(data) #发送文件
                        sent_size += len(data) #发送大小增加
                        #file_md5.update(data)
                        print("send:",file_size,sent_size)
                    else:
                        #md5_str = file_md5.hexdigest()
                        t_cost = time.time() - t_start
                        print "----file transfer time:---",t_cost
                        print("\033[32;1m----successfully sent file to client----\033[0m")
                        #print("\033[32;1m---- file md5 [%s]----\033[0m" %md5_str)
        else: #file doesn't exist
            print(self.response_code['302']) #打印状态码相应的内容

    def instruction__get(self,instructions):
        if len(instructions) == 1:
            return
        else:
            file_name = instructions[1] #要获取的文件名
            raw_str = "file_get|%s"% (json.dumps(file_name)) #文件的指令，和文件名
            self.sock.send(raw_str) #发送内容
            response_str,code,file_size,file_md5 = self.sock.recv(1024).split("|") #接收内容分割字符串
            if code == "300": #ready to get file #状态码是300
                self.sock.send("response|301") #
                total_file_size = int(file_size) #要接收的文件大小
                received_size = 0  #接受到多少
                local_file_obj = open(BASE_DIR+file_name,"wb") #打开文件,将文件写入到var/users下
                while total_file_size != received_size: #总大小不等于接收到大小继续执行
                    data = self.sock.recv(4096) #接收数据
                    received_size += len(data) #接收到内容增加
                    local_file_obj.write(data) #将接收到内容写入文件
                    print("recv size:", total_file_size,received_size)
                else:
                    print("\033[32;1m----file download finished-----\033[0m") #接收完毕
                    local_file_obj.close()
            elif code == '302' : #file doesn't exist
                print(self.response_code[code]) #打印状态码相应的内容

    def handle(self): #链接服务端
        self.connect(self.ftp_host,self.ftp_port)
        if self.auth(): #用户认证   4,
            self.interactive() #ftp操作做入口方法  5,
