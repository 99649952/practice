#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import json
import shutil
import cPickle as p
import datetime
import functools
import re
#s = '{"backend": "www.oldboy.org","record":{"server": "100.1.7.20","weight": 20,"maxconn": 3000}}'
history_list=[] #历史命令记录列表
d1 = datetime.datetime.now() #时间

def menu(): #打印菜单返回操作选项
	print'''
	++++++++++++++++++++++++
	+   1.find_record      +
	+   2.add_record       +
	+   3.delete_record    +
	+   4.recover_record   +
	+   5.history_record   +
	+   6.exit_program     +
	++++++++++++++++++++++++
	'''
	op=raw_input('please select on>>>')
	return op

def passwd_auth(): #自己第一天写的登录，写的比较low就不打注释了
	information={'lxb':'123','alex':'234','liao':'345','wusir':'456'}
	while True:
		count=0
		user_input=raw_input('user:').strip()
		if user_input in information.keys():
			f=open('fail_account.txt')
			user_lock=f.read().strip()
			f.close()
			if user_input in user_lock:
				print 'account already lock'
				main()
			while(count<3):
				passwd_input=raw_input('password:') #pycham不支持getpass模块
				if passwd_input == information[user_input]:
					print 'login successfully'
					return 'success'
				else:
					count +=1
					if count == 3:
						f=file('fail_account.txt','a')
						f.write(user_input)
						f.write('\n')
						f.close()
						print 'You have to lose the wrong password three times account has been locked'
		else:
			print 'user not exist'

def fetch(backend): #查找记录返回列表
	fetch_list = []  #创建空列表用于存储查找到的记录
	with open('ha') as obj:  #打开配置文件，把指定标题下的记录写入列表
		flag = False  #起始标签为faild
		for line in obj:  #循环读取文件的每行
			if line.strip() == "backend %s" % backend: #如果行里的内容等于指定标题
				flag = True #标签变为true
				continue #跳出本次循环
			if flag and line.strip().startswith('backend'):# 判断，如果当前标签为true并且是backend开头
				break #跳出循环体
			if flag and line.strip(): #如果标签为true并且有line
				fetch_list.append(line.strip()) #将指定标题下的行追加到列表
	return fetch_list #返回记录列表

def find_input(): #调用fetch函数打印记录
	input_find=raw_input('please input find record:').strip() #记录用户输入内容
	if re.search('(\w*\.)(\w*)',input_find): #用于匹配一个点网站
		pass
	elif re.search('(\w*\.){2}(\w*)',input_find): #用于匹配两个点网站
		pass
	else: #格式不对
		print('please enter a title right')
		return
	history_list.append(d1)
	history_list.append('findinput:%s'%input_find) #将操作追加到history_list
	history_dump() #将新生成的列表写入文件
	if len(fetch(input_find)) == 0: #如果记录列表长度为0那么不存在记录
		print('You find the title does not exist')
	else:
		print '='*70
		print 'backend %s'%input_find
		for i in  fetch(input_find): #记录列表存在则循环打印列表
			print('\t\t%s'%i)
		print '='*70

def add_www(dict_info): #添加指定标题的记录，并留取备份文件
	try:  #当输入数字json不能过滤出错误所以get回会报错
		backend_title = dict_info.get('backend') #获取backend的title
	except AttributeError:
		print('input error please input correct record')
		return
	current_title = "backend %s" % backend_title  #获取标题
	record=dict_info['record'] #获取记录字典
	#获取插入记录
	current_record = "server %s %s weight %s maxconn %s" % (record['server'],record['server'],record['weight'],record['maxconn'])
	fetch_list = fetch(backend_title) # 获取制定backend下的所有记录
	if fetch_list:# backend是否存在
		# 存在backend，则只需再添加记录
		if current_record in fetch_list: # 要插入的记录存在
			print '='*70
			print 'record already in file'
			print '='*70
			return 'add exist'
		else: # 要插入的记录不存在则追加到记录列表
			fetch_list.append(current_record)
		with open('ha') as read_obj, open('ha.new', 'w') as write_obj:# 同时打开原配置文件做读操作，新打开文件做写操作
			flag = False
			has_write = False
			for line in read_obj: #循环读取原配置文件
				if line.strip() == current_title: #如果行内容等于标题，写入新文件标签变为true，且跳出本次循环
					write_obj.write(line)
					flag = True
					continue
				if flag and line.strip().startswith('backend'): #如果标签是true，且开头时backend，标签变为false
					flag = False
				if flag: #如果标签为true
					# 中，把列表所有数据写入
					if not has_write: #如果标签不是false，说白了就是true
						for new_line  in fetch_list:  #循环读取记录列表写入新文件
							temp = "%s %s \n" %(" "*8, new_line)
							write_obj.write(temp)
						has_write = True #标签变为true，下次再执行上次的if not has_write，此时为false
				else:
					# 上，下
					write_obj.write(line)
		print '='*70
		print 'insert success!!!'
		print '='*70
	else:# 不存在backend，添加记录和backend
		with open('ha') as read_obj, open('ha.new', 'w') as write_obj: #打开原文件读，新文件写入
			for line in read_obj:
				write_obj.write(line)
			write_obj.write('\n')
			write_obj.write(current_title+'\n')
			temp = "%s %s \n" %('\t\t', current_record)
			write_obj.write(temp)
		print '='*70
		print 'insert success!!!'
		print '='*70

	if os.path.exists('ha.bak'): #如果备份文件存在则删除
		os.remove('ha.bak')
	else:
		pass
	os.rename("ha", 'ha.bak') #原配置文件变为备份文件
	os.rename("ha.new", 'ha')  #新配置文件，改为原文件

def add_input(): #调用add_www用于添加记录并打印相应的内容
	input_add=raw_input('please input add record:').strip()
	history_list.append(d1)
	history_list.append('input_add:%s'%input_add)
	history_dump()
	try: #如果输入的内容能转换成字典类型，则跳出循环体，不能话跳过错误继续输入
		data_dict = json.loads(input_add)
	except ValueError:
		print('input error please input correct record')
		return
	add_www(data_dict)

def remove_www(dict_info):
	try:
		backend_title = dict_info.get('backend')
	except AttributeError:
		print('input error please input correct record')
		return
	current_title = "backend %s" % backend_title
	record=dict_info['record']
	current_record = "server %s %s weight %s maxconn %s" % (record['server'],record['server'],record['weight'],record['maxconn'])
	# 获取制定backend下的记录列表
	fetch_list = fetch(backend_title)
	# backend是否存在
	if fetch_list:
		if current_record in fetch_list: #如果记录在文件中不做操作
			with open('ha') as read_obj, open('ha.new', 'w') as write_obj:
				flag = False
				has_write = False
				for line in read_obj:
					if len(fetch_list) == 1 and line.strip() == current_title: #如果查到的列表长度为1，那么不将backend写入新文件
						flag = True
						continue
					elif line.strip() == current_title:  #如果内容为backend标题，将backend标题插入文件
						flag = True
						write_obj.write(line)
						continue
					if flag and line.strip().startswith('backend'):
						flag = False
					if flag:
						# 中，把列表所有数据写入
						if not has_write:
							for new_line  in fetch_list:
								if new_line == current_record:  #如果删除内容在列表中则跳过本次循环即不插入新文件
									continue
								else:
									temp = "%s %s \n" %(" "*8, new_line)
									write_obj.write(temp)
							has_write = True
					else:
						# 上，下
						write_obj.write(line)
			print '='*70
			print 'remove success'
			print '='*70
		else:
			print '='*70
			print 'Delete the content does not exist'
			print '='*70
			return 'remove faild'
		# fetch_list,处理完的新列表

	else:
		print '='*70
		print 'Delete the content does not exist'
		print '='*70
	if os.path.exists('ha.bak'):
		os.remove('ha.bak')
	else:
		pass
	os.rename("ha", 'ha.bak')
	os.rename("ha.new", 'ha')

def remove_input(): #调用remove_www用于删除记录，并打印相应内容
	input_remove=raw_input('please input remove record:').strip()
	history_list.append(d1)
	history_list.append('input_remove:%s'%input_remove)
	history_dump()
	try:
		data_dict = json.loads(input_remove)
	except ValueError:
		print('input error please input correct record')
		return
	remove_www(data_dict)

def menu_error():#菜单选项不正确调用的函数
	print 'Unkonw options,Please try again!'

def recover_input(): #还原配置文件
	history_list.append('recover')
	history_dump()
	if os.path.exists('ha.bak'): #如果存在备份文件就还原配置文件
		os.remove('ha')
		shutil.copy('ha.bak','ha')
		print '='*70
		print 'record success'
		print '='*70
	else: #不存在配置文件
		print '='*70
		print('ha.bak not exist')
		print '='*70

def history_dump(): #执行格式化存储文件
	f=open('history_txt','w')
	p.dump(history_list,f) #将历史操作记录列表保存到文件
	f.close()

def history_load(): #用于存储历史操作记录的函数
	if os.path.exists('history_txt'): #如果存在历史记录文件则加载
		global history_list
		f=open('history_txt')
		history_list=p.load(f)

	else:  #否则不做操作即历史操作记录为空
		pass

def history_opt(): #历史操作记录操作
	global history_list
	while 1:
		history_input=raw_input('1:see_history|2:delete_history:')
		if history_input == '1': #输入为1 打印历史操作记录
			print '='*70
			print 'history opt list:'
			for i in history_list:
				print '\t\t',i
			print '='*70
			break
		elif history_input == '2':  #输入为2 保存空列表到文件
			history_list=[]
			history_dump()
			break
		else:
			print('input error')

def exit_program(): #退出程序
	os._exit(0)

#调用函数的字典
ops={'1':find_input,
	'2':add_input,
	'3':remove_input,
	 '4':recover_input,
	 '5':history_opt,
	 '6':exit_program}

#程序主函数
def pass_wrapper(func): #装饰器实现在查找前需要认证才能查找
	@functools.wraps(func)
	def wrapper(): #被装饰后的函数
		passwd_auth()
		func()
	return wrapper
@pass_wrapper #原函数等于装饰后的函数，达到执行原函数即执行封装后的函数
def main():
	history_load()
	while True:
		op = menu()
		ops.get(op,menu_error)() #获取相应选项的函数结果，选项不存在执行默认操作即menu_error函数

if __name__ == '__main__': #模块名是main则执行主函数
	main()
