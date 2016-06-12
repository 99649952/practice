#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = '李晓波'
import hashlib, time


def get_token(username,token_id):
    timestamp = int(time.time())
    md5_format_str = "%s\n%s\n%s" %(username,timestamp,token_id)
    obj = hashlib.md5()
    obj.update(md5_format_str)
    return obj.hexdigest()[10:17], timestamp

if __name__ == '__main__':
    print get_token('alex', 'test')