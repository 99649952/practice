#!/usr/bin/env python
#coding:utf-8
__author__ = '123'
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #找到项目根目录
print BASE_DIR
sys.path.append(BASE_DIR) #将根目录加到Python变量中
from module import main

if __name__ == '__main__':
    Entrypoint = main.ArgvHandler(sys.argv) #调用检测输入的类
