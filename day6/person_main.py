#!/usr/bin/env python
#coding:utf-8
__author__ = '123'

from person_class import person
from person_class import man
from person_class import woman
from story import story_line

def role_op(op): #角色选择
    if op == '1':
        ruru=woman('Ruru',23,'女','河南','人事经理',12000,None,'大众',None,'Liao')
        print('角色初始信息……')
        print ruru.woman_information()
        return ruru
    elif op == '2':
        liao=woman('Liao',22,'女','山西','tour guide',4000,None,None,'Jack','Ruru')
        print('角色初始信息……')
        print liao.woman_information()
        return liao
    elif op == '3':
        jack=man('Jack',23,'男','河北','网管',4000,None,None,'Liao',None)
        print('角色初始信息……')
        print jack.man_information()
        return jack
    elif op == '4':
        tom=man('Tom',24,'男','北京','富二代',0,'别墅','跑车',None,'Rose')
        print('角色初始信息……')
        print tom.man_information()
        return tom

def work_op(op):
    if op == '1':
        waiter_value=story_line().waiter
        return waiter_value
    elif op == '2':
        programer_value=story_line().programer
        return programer_value
    elif op == '3':
        qiantai=story_line().qiantai
        return qiantai
    elif op == '4':
        teacher_value=story_line().english_teacher
        return teacher_value

def name_menu():
    while 1:
        name_input=raw_input('''请选择一个角色：
        1：Ruru
        2：Liao
        3：Jack
        4：Tom
        >>>''')
        if name_input in str(range(1,5)):
            return name_input
        else:
            print('您输入的选项有误请重新输入\n')
            continue

def work_menu():
    while 1:
        work_input=raw_input('''请选择你的下一份工作：
        1：服务生
        2：程序员
        3：前台
        4：英语老师>>>''')
        if work_input in str(range(1,5)):
            return work_input
        else:
            print('您输入的选项有误请重新输入\n')
            continue

def main():
    op_role=name_menu()
    role=role_op(op_role)
    value=0
    initial_value=role.person_value() #初始价值
    value+=initial_value
    op_work=work_menu()
    work=work_op(op_work)
    value+=work
    print(value)

if __name__ == '__main__':
    main()