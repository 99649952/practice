#!/usr/bin/env python
#coding:utf-8
__author__ = 'bobo'
import time,json,logging
#time_now=(time.strftime('%Y-%m-%d %H:%M:%S'))

#with open('opt_record','w') as f_json:

def credit_log(login_record_in): #日志记录
    logging.basicConfig(filename='credit_card.log',
                    format='''%(asctime)s
                %(message)s''',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=10)
    logging.info(login_record_in)

