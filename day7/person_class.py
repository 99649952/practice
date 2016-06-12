#!/usr/bin/env python
#coding:utf-8
__author__ = '123'

class person(object): #创建一个人类
    def __init__(self,name,age,sex,address,job,salary,value,house=None,car=None): #初始化一些对象属性
        self.name=name
        self.age=age
        self.sex=sex
        self.address=address
        self.job=job
        self.value=value
        self.salary=salary
        self.house=house
        self.car=car
    def persional_dict(self): #创建个人信息字典方便以后调用
        person_dict={
            'name':self.name,
            'age':self.age,
            'sex':self.sex,
            'address':self.address,
            'job':self.job,
            'value':self.value,
            'salary':self.salary,
            'house':self.house,
            'car':self.car
        }
        return person_dict
    def persional_information(self): #返回个人信息
        person_info='''
        姓名：     %s
        年龄：     %s
        性别：     %s
        住址：     %s
        工作：     %s
        工资：     %s
        房子：     %s
        车子：     %s
        '''%(self.name,self.age,self.sex,self.address,self.job,self.salary,self.house,self.car)
        return person_info.strip()
    @property
    def person_value(self): #评测个人价值方法，依据或许有些牵强，但可以根据自我喜好更改
        value=50
        if 20 < self.age <30:
            value+=10
        if self.job == 'IT':
            value+=10
        if self.job == '富二代':
            value-=10
        if self.salary >= 10000:
            value+=20
        if self.house == '楼房':
            value+=20
        if self.house == '别墅':
            value+=50
        if self.car == '大众':
            value+=20
        if self.car == '跑车':
            value+=30
        if self.sex == '女':
            value+=20
        self.value=value  #对象的self.value值改变
        return value


class man(person): #继承persion类
    #初始化man类，继承父类构造函数，并新加功能。
    def __init__(self,name,age,sex,address,job,salary,value,house=None,car=None,girlfriend=None,mistress=None):
        super(man,self).__init__(name,age,sex,address,job,salary,value,house,car)
        self.girlfrind=girlfriend
        self.mistress=mistress
    @property
    def man_dict(self): #用字段形式访问任务信息列表
        return_person_dict=person.persional_dict(self)
        return_person_dict['女友'] = self.girlfrind
        return_person_dict['情妇'] = self.mistress
        return return_person_dict
    @property
    def man_information(self):
        return_person_info=person.persional_information(self) #继承父类
        man_info='''
        女友：     %s
        情妇：     %s
        ''' %(self.girlfrind,self.mistress)#增加新功能
        return '%s%s'%(return_person_info,man_info)


class woman(person): #
    def __init__(self,name,age,sex,address,job,salary,value,house=None,car=None,boyfrinend=None,girlfriend=None):
        super(woman,self).__init__(name,age,sex,address,job,salary,value,house,car)
        self.boyfriend=boyfrinend
        self.girlfrind=girlfriend
    @property
    def woman_dict(self):
        return_person_dict=person.persional_dict(self)
        return_person_dict['男友'] = self.boyfriend
        return_person_dict['闺蜜'] = self.girlfrind
        return return_person_dict
    @property
    def woman_information(self):
        return_person_info=person.persional_information(self) #继承父类
        woman_info='''
        男友：     %s
        闺蜜：     %s
        ''' %(self.boyfriend,self.girlfrind)
        return '%s%s'%(return_person_info,woman_info)