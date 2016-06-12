#!/usr/bin/env python
#coding:utf-8
__author__ = '123'

import paramiko
import multiprocessing

def conn_host(cmd,host_information): #多进程处理
	result = [] #存储远程命令返回的结果
	p = multiprocessing.Pool(processes=4) #可以同时处理十个任务
	for host in host_information:
		ip=host['ip']
		port=int(host['port'])
		user=host['host_account']
		passwd=host['host_passwd']
		result.append(p.apply_async(ssh_cmd,(ip,port,user,passwd,cmd))) #执行函数
	p.close()
	for res in result:
		res.get(timeout=35) #获取返回结果

def ssh_cmd(ip,port,user,passwd,cmd): #执行系统命令
	msg = "-----------Result:%s----------" % ip
	s = paramiko.SSHClient()
	s.load_system_host_keys()
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		s.connect(ip,port,user,passwd,timeout=5)
		stdin,stdout,stderr = s.exec_command(cmd)
		cmd_result = stdout.read(),stderr.read()
		print msg
		for line in cmd_result:
				print line,
		s.close()
	except paramiko.AuthenticationException:
		print msg
		print 'AuthenticationException Failed'