#!/usr/bin/env python
#coding:utf-8
__author__ = '123'
from time import sleep

class story_line(object):
    def __init__(self,name,value,salary):
        self.name=name
        self.value=value
        self.salary=salary
    @staticmethod
#改变价值即对象的self.value的方法
    def __split_line():
        print('------华丽的分割线------')
        sleep(3)
    def waiter(self):
        print('%s   服务生的一天即将开始 .....')%self.name
        #将剧情内容保存在列表
        waiter_day=['早上六点，铃铃铃，朦胧中',
                    'xxx又该起床了',
                    '速度洗漱沙河挤地铁',
                    '服务员上菜，服务员擦桌子，服务员...',
                    '拖着疲惫的身体回到家',
                    '独身一人的小屋子',
                    '一年过去了',
                    '还是老样子']
        for i in waiter_day: #打印剧情进展
            print(i)
            sleep(3)
        story_line.__split_line()
        self.salary=4000
        self.value+=5 #剧情结束后value值改变
        return [self.value,self.salary] #返回一个列表保存着改变后的value和salary值。
    def programer(self):
        print('%s   程序员（代码狗）的幸福（苦逼）一天')%self.name
        program=['写写写程序，MD做梦还在写程序',
                     '寂寞的时候写程序',
                     '无聊的时候写程序',
                     '泡妹子的时候还在写程序',
                     '受到上级夸奖',
                     '一年过去了',
                     '成功晋级成高级程序员（代码狗）']
        for i in program:
            print(i)
            sleep(3)
        story_line.__split_line()
        self.salary=12000
        self.value+=30
        return [self.value,self.salary]
    def qiantai(self): #前台的英语呵呵
        print '%s   前台美女闲的不要不要的一天'%self.name
        qiantai=['漂漂亮亮来公司',
                  '老板调戏',
                  '专心玩手机',
                  '经理调戏',
                  '专心玩手机',
                  '一天就是被调戏，玩手机',
                  '一年过去了']
        for i in qiantai:
            print(i)
            sleep(3)
        story_line.__split_line()
        self.salary=3000
        self.value-=5
        return [self.value,self.salary] #没有小瞧前台的意思，总得有一个职业减点个人价值
    def english_teacher(self):
        print('%s   人民教师最美丽……') %self.name
        teacher=['小朋友们你们好',
                 '来大家一起跟我读apple',
                 '老师为什么，为什么……',
                 'OK,Class is over',
                 '一年过去了',
                 '成为高级翻译（不现实）']
        for i in teacher:
            print(i)
            sleep(3)
        story_line.__split_line()
        self.salary=7000
        self.value+=20
        return [self.value,self.salary]

def work_menu(): #选择工作
    while 1:
        work_input=raw_input('''请选择你的一份工作来提升自己：
        1：服务生
        2：程序员
        3：前台
        4：英语老师>>>''')
        if work_input in str(range(1,5)):
            return work_input
        else:
            print('您输入的选项有误请重新输入\n')
            continue

def work_op(op,name,value,salary): #进入工作返回价值
    if op == '1':
        return story_line(name,value,salary).waiter() #执行相应的工作 ，返回工作后的value值
    elif op == '2':
        return story_line(name,value,salary).programer()
    elif op == '3':
        return story_line(name,value,salary).qiantai()
    elif op == '4':
        return story_line(name,value,salary).english_teacher()