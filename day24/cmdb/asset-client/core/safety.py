#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = '李晓波'
import time
import hashlib


def encrypt_client(name, password):
    name = name
    now_time = time.time()
    data = [name, now_time]
    password = password
    encrypt = hashlib.md5('%s%s' % (password, now_time))
    encrypt_data = encrypt.hexdigest()
    data.append(encrypt_data)
    return data
