#!/usr/bin/env python
#coding:utf-8
__author__ = '123'
from person_class import man
from person_class import woman
from time import sleep

def role_op(op): #角色选择，返回角色对象
    if op == '1':
        ruru=woman('Ruru',23,'女','河南','人事经理',12000,None,None,'大众',None,'Liao') #创建对象
        print('角色初始信息……')
        return ruru
    elif op == '2':
        liao=woman('Liao',22,'女','山西','tour guide',4000,None,None,None,'Jack','Ruru')
        print('角色初始信息……')
        return liao
    elif op == '3':
        jack=man('Jack',23,'男','河北','网管',4000,None,None,None,'Liao',None)
        print('角色初始信息……')
        return jack
    elif op == '4':
        tom=man('Tom',24,'男','北京','富二代',800000,None,'别墅','跑车',None,'Rose')
        print('角色初始信息……')
        return tom

def name_menu(): #选择角色
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

class man_act(man):
    def __init__(self,name,salary,girlfriend,value,car):
        self.name=name
        self.salary=salary
        self.girlfrind=girlfriend
        self.value=value
        self.car=car

    @staticmethod
    def __split_line():
        print('\t\t------华丽的分割线------')
        sleep(3)

    @staticmethod
    def __for_print(content): #用于循环打印列表的内容
        for i in content:
            print('\t\t%s'%i)
            sleep(3)

    def kiss(self):
        print('''
        ----------剧情主线----------
        %s:今天有点想女朋友了，想……'''%(self.name))
        sleep(3)
        if self.girlfrind == None:
            print('''
            擦又做梦呢，我哪有女朋友吗！！！
            MD明年双十一不想过光棍节了，赶紧找女票去……''')
            return
        print('''
女朋友家里：
        %s：我想亲亲
        不嘛人家想要包包
        '''%(self.name))
        if self.salary <=6000:
            content=['%s：媳妇啊，那个工资交房租了'%self.name,
            '没钱了下次吧',
            '%s：又是下次'%self.girlfrind,
            '你是不是不爱我了',
            '我们分手吧！！！',
            '呵呵要不是我没有钱，我就信了。']
            man_act.__for_print(content) #循环打印story内容
            man_act.__split_line()#分割线方法
            print('\t\t我要提升自己')
            return 'salary'
        elif self.salary >6000:
            print('''
            买买买！！！
            就知道你最好
            ''')
            man_act.__split_line()

    def party(self):
        print('''
        %s：今天又要同学聚会，除了装逼就是吹
某某饭店中'''%self.name)
        if self.value <= 80:
            conntent=['自己一个人默默地吃饭',
                      '听着老同学间各种吹嘘',
                      '为啥我这么我混的这么苦逼',
                      '不能再这样我得努力']
            man_act.__for_print(conntent)
            man_act.__split_line()
        elif  80< self.value <100:
            print '''
            跟着同学一起聊天
            这几年在外边干的不错'''
        elif self.value >= 100:
            conntent=['当年的大波妹贴过来，主动搭讪',
                      '各种递烟敬酒',
                      '都听着呢各种装x',
                      '逼格爆表',
                      '聚会结束都找你要联系方式']
            man_act.__for_print(conntent)
            man_act.__split_line()

    def yedian(self):
        print('夜店小生活')
        if self.car == '跑车':
            print('''
            妹子开车带你兜风
            车外：车在有规律的晃动
            ''')
        else:
            print('''
            自己喝闷酒
            我要奋斗''')

class woman_act(woman): #女的情节自己随意加了，毕竟咱不是女的剧情就少了
    def __init__(self,name,salary,boyfriend,value,girlfriend):
        self.name=name
        self.salary=salary
        self.boyfriend=boyfriend
        self.value=value
        self.girlfrind=girlfriend

    @staticmethod
    def __split_line():
        print('\t\t------华丽的分割线------')
        sleep(3)

    @staticmethod
    def __for_print(content):
        for i in content:
            print('\t\t%s'%i)
            sleep(3)

    def eat(self):
        print('-'*10+'剧情主线'+'-'*10)
        print('\t\t想吃西餐了')
        sleep(3)
        if self.value<=80:
            print('\t\t下次再吃吧，钱都买衣服和化妆品了')
            sleep(3)
        elif 80 <self.salary<100:
            print('\t\t叫上%s一块去'%self.boyfriend)
            sleep(3)
        elif self.salary > 100:
            print('\t\t今天请%s吃西餐'%self.girlfrind)
            sleep(3)

    def shop(self):
        print('''
        %s：今天要买衣服，买吃的，买化妆品，
        总之就是买买买……'''%self.name)
        sleep(3)
        if self.salary <=4000:
            print('''
            又得花%s的钱
            每次都得花男朋友的钱'''%self.boyfriend)
            sleep(3)
        elif 4000 <self.salary < 8000:
            print('''
            得对男朋友好点就用他提东西就好
            不动他钱包了，下次花他的''')
            sleep(3)
        elif self > 8000:
            print('没有男人老娘照样可以过')
            sleep(3)

