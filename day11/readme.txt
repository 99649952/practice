login为登录入口脚本

一、用户登录
1、首先登录堡垒机
2、可选批量执行命令，也可选单独登陆操作：
	批量命令：操作记录和用户信息存入数据库。
	单台操作：登录到终端进行交互，操作记录和用户信息存入数据库。
3,查看操作记录

二、数据库表
	group :group_name
	host : id ,group_name（外键）,ip  port host_account host_passwd
	user : id ,group_name（外键）,account,passwd

三、修改paramiko的demo，interactive
	操作日志写入数据库




blog