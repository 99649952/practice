#_*_coding:utf-8_*_
__author__ = 'Alex Li'

from conf import settings
from modules import threading_socket_server


class  ArgvHandler(object):
    def __init__(self,args):
        self.args = args #启动模块传入的参数start、stop
        print self.args
        self.argv_parser()

    def argv_parser(self):
        if len(self.args) < 2: #参数小于两个
            self.help_msg()
        else:
            first_argv = self.args[1]
            if hasattr(self,first_argv): #在对象有这个成员
                func = getattr(self,first_argv) #获取这个成员
                func() #执行成员
            else:
                self.help_msg()

    def help_msg(self): #启动主函数时
        msg = '''
        start   :start ftp server
        stop    :stop ftp server

                '''
        print(msg)

    def start(self):
        try:
            #实例化对象，传入conf文件中的ip和端口，传入处理请求的类
            server = threading_socket_server.SocketServer.ThreadingTCPServer((settings.BIND_HOST, settings.BIND_PORT), threading_socket_server.MyTCPHandler)
            server.serve_forever() #永久启动服务
        except KeyboardInterrupt: #捕捉Ctrl+c
            print("----going to shutdown ftp server-----")
            server.shutdown()  #关闭socket服务