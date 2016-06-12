#!/usr/bin/env python
#coding:utf-8
__author__ = '123'

import pickle
from redis_helper import RedisHelper
from plug_api import get_cpu

class MonitorClient(object):
    def __init__(self):
        self.configs = {}
        self.redis = RedisHelper()

    def handle(self):
        self.redis.public('xxxxxxxxxxxxxxxxxxxxxx')



b=MonitorClient()
b.handle()