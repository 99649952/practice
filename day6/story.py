#!/usr/bin/env python
#coding:utf-8
__author__ = '123'
import time
class story_line(object):
    @staticmethod
    def split_line():
        print('------华丽的分割线------')
        time.sleep(3)
    @property
    def waiter(self):
        print('服务生的一天即将开始 .....')
        waiter_day=['早上六点，铃铃铃，朦胧中',
                    '%s：xxx又该起床了',
                    '速度洗漱沙河挤地铁',
                    '服务员上菜，服务员擦桌子，服务员...',
                    '拖着疲惫的身体回到家',
                    '独身一人的小屋子',
                    '一年过去了',
                    '还是老样子']
        for i in waiter_day:
            print(i)
            time.sleep(3)
        story_line.split_line()
        return 5 #用于和价值相加，用于再评测
    @property
    def programer(self):
        print('程序员（代码狗）的幸福（苦逼）一天')
        program=['写写写程序，MD做梦还在写程序',
                     '寂寞的时候写程序',
                     '无聊的时候写程序',
                     '泡妹子的时候还在写程序',
                     '受到上级夸奖',
                     '一年过去了',
                     '成功晋级成高级程序员（代码狗）']
        for i in program:
            print(i)
            time.sleep(3)
        story_line.split_line()
        return 30 #用于和价值相加，用于再评测
    @property
    def qiantai(self): #前台的英语呵呵
        print '前台美女闲的不要不要的一天'
        qiantai=['漂漂亮亮来公司',
                  '老板调戏',
                  '专心玩手机',
                  '经理调戏',
                  '专心玩手机',
                  '一天就是被调戏，玩手机',
                  '一年过去了']
        for i in qiantai:
            print(i)
            time.sleep(3)
        story_line.split_line()
        return -10
    @property
    def english_teacher(self):
        print('人民教师最美丽……')
        teacher=['小朋友们你们好',
                 '来大家一起跟我读apple',
                 '老师为什么，为什么……',
                 'OK,Class is over',
                 '一年过去了',
                 '成为高级翻译（不现实）']
        for i in teacher:
            print(i)
            time.sleep(3)
        story_line.split_line()
        return 20





