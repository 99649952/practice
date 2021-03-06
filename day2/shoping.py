#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = '李晓波'
import sys
import cPickle as p
shopdict={'1':['surfacebook',18999],
        '2':['suface4',16999],
        '3':['lumia950',3999],
        '4':['iphone6s',999],
        '5':['belle',399],
        '6':['coffee',20]}
shoping_card_dict={}
shopdictfile='shopdict.data'
cost_file='storedlist.data'
def load_file(): #加载上次购物信息函数
    try:  #没有购物文件跳过错误
        f=file(shopdictfile)
        stored_dict=p.load(f)
        print '''您上次的购物信息
商品\t\t数量\t\t价格'''
        for i in stored_dict:
            print '%s\t\t%s\t\t%s' %(i.ljust(8),stored_dict[i][0],stored_dict[i][1])
    except IOError:
        pass
    try: #没有购物文件跳过错误
        f1=file(cost_file)
        stored_list=p.load(f1)
        print '您的消费总额为%s，余额为%s。'%(stored_list[0]-stored_list[1],stored_list[1])
    except IOError:
        pass
load_file()
def menu_error():
	print '未知的操作，请输入正确的操作'
'''-------------------------------菜单-----------------------------------------------------------'''
def menu():
	print'''
	+++++++++++++++++++++++++
	+   1.购物              +
	+   2.查看修改购物车    +
	+   3.结账or退出        +
	+++++++++++++++++++++++++
	'''
	op=raw_input('please select one>>>')
	return op
'''---------------------------------购物代码------------------------------------------------'''
while 1:
    try:
        salary=int(raw_input('请输入你的工资：'))
        balance=salary
        if salary > 999:
            break
        else:
            print '穷鬼赶紧挣钱去'
    except ValueError:
            print '您输入的有误请输入整数！！！'
def goods_list(): #打印购物列表
    print '\n开启您的购物之旅\n'
    print '编号\t\t产品\t\t价格'
    for shop_line in shopdict:
        print '%s\t\t\t\t%s\t\t\t\t%s'%(shop_line,shopdict[shop_line][0].ljust(12),shopdict[shop_line][1])
def yes_or_no(): #购物状态选择
    while 1:
            input_yes_no=raw_input('请输入y或n选择是否继续购物：(y/n)')
            if input_yes_no == 'y' or input_yes_no == 'n':
                return input_yes_no
            else:
                continue
def shoping(): #购物主程序
    while 1:
        global salary  #设置salary为全局变量
        goods_list()
        shoping_id=raw_input('请输入要加入购物车的产品编号：')
        if shoping_id in shopdict:
            while 1:  #判断输入的产品个数
                try:
                    goods_numbers=int(raw_input('请输入购买的个数：'))
                    break
                except ValueError:
                    print '您输入的有误请输入整数！！！'
            if salary >= shopdict[shoping_id][1]*goods_numbers:  #如果工资大于购买额
                balance = salary-shopdict[shoping_id][1]*goods_numbers
                print '%d个%s已加入购物车，您现在的余额是%s' %(goods_numbers,shopdict[shoping_id][0],
                                                    balance)
                salary-=shopdict[shoping_id][1]*goods_numbers  #工资减去消费额
                if shopdict[shoping_id][0] in shoping_card_dict:   #如果已购买此产品
                    goods_numbers_agin=shoping_card_dict[shopdict[shoping_id][0]][0] + goods_numbers #产品个数相加
                    shoping_card_dict[shopdict[shoping_id][0]]=[goods_numbers_agin,shopdict[shoping_id][1]*goods_numbers_agin] #产品总额更改
                else:
                    shoping_card_dict[shopdict[shoping_id][0]]=[goods_numbers,shopdict[shoping_id][1]*goods_numbers]#产品不在购物字典中则添加
                shoping_card()
                yes_no_return=yes_or_no()
                if yes_no_return == 'y':
                    continue
                else:
                    break
                    return 'shoping_exit'
            else:
                print '穷鬼找你老婆要钱去！！！'
        else:
            print '请输入正确的产品id！！！'

'''------------------------------------查看并修改购物车-------------------------------------------'''
def shoping_card():
    global cost
    cost=0
    global cost_list
    print '商品\t\t数量\t\t价格'
    for i in shoping_card_dict:
        print '%s\t\t%d\t\t%d' %(i,shoping_card_dict[i][0],shoping_card_dict[i][1])
        cost=cost+shoping_card_dict[i][1]  #购物车产品额递加
    print '购物总额为%d余额为%d' %(cost,balance-cost)
def alter_goods(): #修改产品数量代码
    shoping_card()
    input_goods=raw_input('请输入您要更改数量的商品')
    if input_goods in shoping_card_dict:
        price=shoping_card_dict[input_goods][1]/shoping_card_dict[input_goods][0] #些改后单个商品总额
        while 1:
            try:
                input_numbers=int(raw_input('输入更改后的数量'))
                shoping_card_dict[input_goods]=[input_numbers,price*input_numbers] #将购买修改数量和单个商品总额加入购物车字典
                break
            except ValueError:
                print '您正确输入商品个数！！！'
    else:
        print '请输入已加入购物车的商品！！！'
def remove_goods():  #删除商品字典代码
    shoping_card()
    input_goods=raw_input('请输入您要删除的商品')
    if input_goods in shoping_card_dict:
        del shoping_card_dict[input_goods] #在购物字典中删除商品
        print '%s已移除购物车'%input_goods
    else:
        print '你输入的商品不存在'
def exit_shop_card():
    main()
shop_card_chose_dict={'1':remove_goods,
                        '2':alter_goods,
                        '3':shoping,
                        '4':exit_shop_card}
def shop_card_input():
    print '''1、删除购物车内的商品
2、修改已购买商品的个数
3、继续购物
4、退出购物车'''
    shopcard_op=raw_input('请输入操作：')
    return shopcard_op
def shop_card_main():
    while True:
        op = shop_card_input()
        shop_card_chose_dict.get(op,menu_error)()

'''-------------------------------结账或退出------------------------------------------------------------'''
def save_shop():  #购物信息保存函数
    f=file(shopdictfile,'w')
    p.dump(shoping_card_dict,f)
    f.close()
    f1=file(cost_file,'w')
    p.dump([balance,balance-cost],f1)
    f1.close()
def exit_shoping():
    shoping_card()
    while 1:
        a=raw_input('亲输入1：结账  2：退出')
        if a=='1':
            print '您一共消费%s,欢迎下次光临' %(cost)
            save_shop() #将购物信息保存
            shoping_card_dict.clear() #结账完需清除购物车
            break
        elif a=='2':
            sys.exit()
        else:
            print '请输入正确选项'
'''------------------------------------主程序-----------------------------------------------------------'''
ops={'1':shoping,
	'2':shop_card_main,
	'3':exit_shoping}
def main():
    while True:
        op = menu()
        ops.get(op,menu_error)()
main()
