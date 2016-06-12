#_*_coding:utf-8_*_
__author__ = 'Alex Li'


import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #找到项目根目录
print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
sys.path.append(BASE_DIR) #将根目录加到Python变量中
from modules import main

if __name__ == '__main__':
    Entrypoint = main.ArgvHandler(sys.argv) #执行文件时实例化对象传入参数
