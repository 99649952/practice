#!/usr/bin/env python
#coding:utf-8
__author__ = '123'

import logging
def logger(ip,username,group,cmd):
    logging.basicConfig(level=logging.DEBUG,
    				format='%(asctime)s %(levelname)s %(message)s',
    				datefmt='%Y/%m/%d %H:%M:%S',
    				filename='myapp.log',
    				filemode='a')
    logging.info('%s %s %s %s'%(ip,username,group,cmd))