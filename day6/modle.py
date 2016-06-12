#!/usr/bin/env python
#-*-coding:utf-8-*-
__author__ = '123'

#之前的函数式编程，是面向过程
# python类、对象、方法、属性，python中一切皆为对象
#对象的特征也称为属性（attribute）。它所具有的行为也称为方法（method）
#结论：对象=属性+方法
#在python中，把具有相同属性和方法的对象归为一个类（class）
#类是对象的抽象化，对象是类的实例化。类不代表具体的事物，而对象表示具体的事物。
#多态：多态意味着可以对不同的对象使用同样的操作，但它们可能会以多种形态呈现出结果。
#继承：面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过 继承机制。
#1、多个方法共用同样的变量，2、动态创建具有相同属性的对象。
#类的成员：
# 字段1、静态字段，动态字段
# 方法：动态方法，静态方法，类方法
# 属性：方法的另种形式，访问时以字段形式
class person(object): #类的格式
    beipiao = '北漂一族' #静态字段：属于类的变量叫做静态字段属于类。
    #__init__函数为构造函数，用于初始化动态字段即初始化对象变量
    def __init__(self, name,age,addr): #其中self为对象本身，后面的参数为类在实例化传入的参数
        #动态字段：属于对象的变量叫做动态字段属于对象
        self.name = name #动态字段
        self.age = age
        self.addr = addr
        self.__papapa = True #私有字段 ，不能被外部直接访问
        print '(%s: %s)' % (person.beipiao,self.name)
    def __del__(self): #析构函数：当对象不再被使用时， __del__ 方法运行
        print('最后的话')
    def sayHi(self): #类中函数称为动态方法
        print 'Hi, my name is %s.' % self.name
    @staticmethod #将动态方法转换为静态方法,不用实例化类，直接用类调用静态方法
    def chinese(): #不用加self参数，可加其他参数
        print('我们都是中国人')
    @classmethod
    def class_met(cls): #类方法：用类调用，参数只能是cls
        print('class    method')

    def info(self):
        print('name:%s  age:%s  address:%s'%(self.name,self.age,self.addr))
    @property #属性：通过装饰器把方法转换成属性：常用作返回值，直接用对象调用方法不用加（）
    def car(self):
        print ('买不起车')
    def __me(self): #私有方法
        print('没钱没房没车')
    @property #只读
    def papapa(self):
        return self.__papapa
    @papapa.setter #可写
    def papapa(self,value):
        self.__papapa=value
    @papapa.deleter
    def papapa(self,value): #删除值
        self.__papapa=value

#lxb = person('小波',23,'河北') #创建对象，就是类的实例化，同时声明变量。
#print(lxb.beipiao)# 对象能访问静态字段#print(person.name)#类不能访问动态字段
#person.chinese() #类的静态方法
#print(lxb.papapa()) #私有字段通过内部公有方法方法展示
#print lxb.car #用字段形式访问特性
#lxb._person__me() #直接访问私有方法不建议使用
#person.chinese() #用类调用静态方法
#person.class_met() #用类调用类方法
#print lxb.papapa #修改私有字段前结果
#lxb.papapa=False #修改私有字段
#print(lxb.papapa) #修改私有字段之前的结果

#类的继承
class poor(person):
    def __init__(self,name,age,addr,buy): #子类增加类变量buy
        super(poor,self).__init__(name,age,addr)#调用父类的构造函数,经典类调用方法
#        person.__init__(self, name,age,addr)#调用父类的构造函数
        self.buy=buy
    def sayHi(self):
        print('%s is a poor')%self.name
#经典类深度优先继承，#新式类为广度优先
class a(): #不继承任何类为经典类，继承object为新式类。
    def f1(self):
        print('a.f1')
class b(a):
    def f2(self):
        print('b.f1')
class c(a):
    def f1(self):
        print('c.f1')
class d(b,c):
    def f2(self):
        print('d.f1')
#d().f1() #经典类结果为a.f1 #当a类继承object，结果为c.f1

#lxb=poor('小波',23,'河北','cannot')
#lxb.car #子类中不存在的方法直接调用，将继承父类的方法
#lxb.sayHi() #子类中重新定义的方法，将使用自己的方法



