#!/usr/bin/env python
#coding:utf-8
__author__ = '123'
from object_oprate import name_menu
from object_oprate import role_op
from change_value import work_menu
from change_value import work_op
from object_oprate import man_act
from object_oprate import woman_act

def value_change(role):
    while 1:
        y_no=raw_input('选择y/n是否要提升个人价值：')
        if y_no == 'y':
            op_work=work_menu() #执行工作选择
            work_return=work_op(op_work,role.name,role.value,role.salary) #将进入工作剧情,并且改变对象的value值
            role.value=work_return[0] #对象的value属性改变
            role.salary=work_return[1] #对象的salary属性改变
            return 'y'
        elif y_no == 'n':
            return 'n'
        else:
            print('您的输入有误请重新输入！！！')
            continue

def main_story(role): #剧情主线
        if role.sex=='男':
            man_act_ob=man_act(role.name,role.salary,role.girlfrind,role.value,role.car) #剧情类实例化
            man_act_ob.kiss() #进入场景1
            man_act_ob.party() #进入场景2
            man_act_ob.yedian() #进入场景3
        else:
            woman_act_op=woman_act(role.name,role.salary,role.boyfriend,role.value,role.girlfrind)
            woman_act_op.eat()
            woman_act_op.shop()

def main(): #定制故事情节
        op_role=name_menu() #角色选择菜单
        role=role_op(op_role)  #返回一个实例化后的对象
        role.person_value #对象value值计算
        while 1:
            print(role.persional_information())
            main_story(role) #执行剧情
            if value_change(role) == 'y':#如果选择y将改变value和salary并继续进入主线了，主要是不想写判断了，显得太繁琐`
                pass
            else:#如果选n将继续角色选择
                op_role=name_menu()
                role=role_op(op_role)
                role.person_value

if __name__ == '__main__':
    main()