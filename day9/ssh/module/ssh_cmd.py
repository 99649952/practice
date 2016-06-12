#!/usr/bin/env python
#coding:utf-8
__author__ = '123'
import paramiko
import multiprocessing
import os

def conn_host(cmd): #多进程处理
	BASEDIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	result = [] #存储远程命令返回的结果
	p = multiprocessing.Pool(processes=10) #可以同时处理十个任务
	with open('%s/conf/serverlist.conf'%BASEDIR) as f:
		list = f.readlines()#主机信息列表
	for IP in list:
		print IP
		host=IP.split()[0]
		port=int(IP.split()[1])
		user=IP.split()[2]
		passwd=IP.split()[3]
		result.append(p.apply_async(ssh_cmd,(host,port,user,passwd,cmd))) #执行函数
	p.close()
	for res in result:
		res.get(timeout=35) #获取返回结果

def ssh_cmd(host,port,user,passwd,cmd): #执行系统命令
	msg = "-----------Result:%s----------" % host
	s = paramiko.SSHClient()
	s.load_system_host_keys()
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		s.connect(host,port,user,passwd,timeout=5)
		stdin,stdout,stderr = s.exec_command(cmd)
		cmd_result = stdout.read(),stderr.read()
		print msg
		for line in cmd_result:
				print line,
		s.close()
	except paramiko.AuthenticationException:
		print msg
		print 'AuthenticationException Failed'
	except paramiko.BadHostKeyException:
		print msg
		print "Bad host key"

def op_file(cmd): #文件多进程处理
	BASEDIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	result = [] #存储远程命令返回的结果
	p = multiprocessing.Pool(processes=10) #可以同时处理十个任务
	with open('%s/conf/serverlist.conf'%BASEDIR) as f:
		list = f.readlines()#主机信息列表
	for IP in list:
		print IP
		host=IP.split()[0]
		port=int(IP.split()[1])
		user=IP.split()[2]
		passwd=IP.split()[3]
		result.append(p.apply_async(ssh_file,(host,port,user,passwd,cmd))) #执行函数
	p.close()
	for res in result:
		res.get(timeout=35) #获取返回结果

def ssh_file(host,port,user,passwd,cmd): #文件传下载
	ssh=paramiko.Transport((host,port))
	ssh.connect(username=user,password=passwd)           # 连接远程主机
	sftp=paramiko.SFTPClient.from_transport(ssh)               # SFTP使用Transport通道
	if cmd.split()[0] == 'put':
		sftp.put(cmd.split()[1],cmd.split()[2])                             # 下载 两端都要指定文件名
	sftp.close()
	ssh.close()