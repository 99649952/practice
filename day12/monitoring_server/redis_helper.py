#!/usr/bin/env python
#coding:utf-8
__author__ = '123'

import redis

class RedisHelper:

    def __init__(self):
        self.__conn = redis.Redis(host='192.168.10.22')
        self.chan_sub = 'fm87.7'
        self.chan_pub = 'fm87.7'

    def get(self,key):
        return self.__conn.get(key)

    def set(self,key,value):
        self.__conn.set(key, value)

    def public(self,msg):
        self.__conn.publish(self.chan_pub, msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub

