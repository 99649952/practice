#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'bobo'
import json
def login(): #用户认证
	with open('account') as f_json:
		information=json.load(f_json)
	while True:
		count=0
		id_input=raw_input('credit card_id:')
		if id_input in information.keys(): #如果用户id存在
			with open('account') as f_json:
				acccount_lock=information[id_input][6]
			if acccount_lock == 'lock': #如果用户锁定
					print 'account already lock'
					continue
			while(count<3): #用户输错三次密码锁定用户
				passwd_input=raw_input('password:') #ide不支持getpass所以没用
				if passwd_input == information[id_input][5]:
					return id_input
				else:
					count +=1
					print 'you are fail %s' %count
					if count == 3:
						with open('account') as f_json:
							account=json.load(f_json)
							account[id_input][6]='lock'
						with open('account','w') as f_json:
							json.dump(account,f_json)
						print 'account already lock'
		else:
			print 'credit card_id not exist'