#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = '李晓波'
import os
BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

Params = {
    "server": "192.168.10.131",
    "port":'',
    'request_timeout':30,
    "urls":{
          "asset_report_with_no_id":"/asset/report/asset_with_no_asset_id/",    #没有资产id发送的链接
          "asset_report":"/asset/report/",  #正常汇报
        },
    'asset_id': '%s/var/.asset_id' % BaseDir,   #资产id存放路径
    'log_file': '%s/logs/run_log' % BaseDir,    #日志存放路径

    'auth':{
        'user':'lxb994@163.com',
        'token': 'abc'
        },
}