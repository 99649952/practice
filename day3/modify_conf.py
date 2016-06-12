#!/usr/bin/env python
#coding:utf-8
__author__ = '123'
import re,json,shutil,sys
def menu():
	print'''
	+++++++++++++++++++++++++
	+   1.查看内容           +
	+   2.修改内容           +
	+   3.删除内容           +
	+   4.退出程序           +
	+++++++++++++++++++++++++
	'''
	op=raw_input('please select one>>>')
	return op
def p_www(): #打印标题内容函数
    #input_find=raw_input('please input find content:').strip()
    input_find='www.oldboy.org'
    f=open('conf')
    for i in f:
        if re.search('^(backend)\s(%s)$'%input_find,i):
            print 'backend %s'%input_find
            for i in f:
                if re.search('^\s(.*)',i):
                    print i,
                else:
                    break
        else:
            pass
    f.close()
def in_www():#给指定标题插入内容
    input_dict=raw_input('Please enter a new record:')
    #a='{"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}'
    try:
        load_dic=json.loads(input_dict)
    except ValueError:
        print '您输入的格式有误'
        return
    backend_title = load_dic['backend']
    record=load_dic['record']
    #如果文件存在插入标题则pass，不存在则创建
    f=open('conf','rb+')
    for line in f:
        if 'backend %s'%backend_title in line:
            back=1
            break
        else:
            back=2
    if back==1:
        pass
    elif back==2:
        f.write('\n')
        f.write('backend %s'%backend_title)
    f.seek(0)
    f_len=len(f.readlines())
    f.seek(0)
    count=0
    #当循环达到文件最大行或找到插入标题退出循环.
    try:
        while count <f_len:
            count+=1
            if re.search('^(backend)\s(%s)$'%backend_title,f.readline()):
                f_write='\t\tserver %s %s weight %s maxconn %s'%(record['server'],record['server'],record['weight'],record['maxconn'])
                f.write('\n')
                f.write(f_write)
                print '-'*60
                print '%s already insert'%f_write
                f.close()
                break
            else:
                pass
    except IOError:
        print '您已插入相应应的条目'
def rm_www():  #删除内容，功能没实现
    input_dict=raw_input('Please enter remove a record:')
    #a='{"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}'
    try:
        load_dic=json.loads(input_dict)
    except ValueError:
        print '您输入的格式有误'
        return 1
    backend_title = load_dic['backend']
    record=load_dic['record']
    with open('conf') as f,open('conf_bak','w') as f_bak:
        for i in f.readlines():
            if re.search('(backend)\s(%s)'%backend_title,i):
                f_bak.write(i)
            elif  re.search('^\s*(server\s%s\s%s\sweight\s%s\smaxconn\s%s)'%(record['server'],record['server'],record['weight'],record['maxconn']),i):
                pass
            else:
                f_bak.write(i)
    shutil.move('conf_bak', 'conf')  #将修改后的文件覆盖源文件
    print '指定内容已被删除'
def exit_program():
    sys.exit()
def menu_error():
	print '未知的操作，请输入正确的操作'
ops={'1':p_www,    #选择对应函数
	'2':in_www,
	'3':rm_www,
     '4':exit_program}
def main():  #主程序
    while True:
        op = menu()
        ops.get(op,menu_error)()
main()
