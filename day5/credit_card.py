#!/usr/bin/env python
#coding:utf-8
__author__ = 'bobo'
import json,time,opt_log
#time_now=(time.strftime('%Y-%m-%d %H:%M:%S'))
#account={'000000001':['lxb',21,'m',15000,15000],
#         '000000002':['liao',22,'w',20000,20000]}

class credit_card(object): #信用卡类

    def __init__(self,account_id):#初始化一些信用卡信息
        with open('account') as f_json:
            account=json.load(f_json)
        self.id=account_id
        self.name=account[account_id][0]
        self.age=account[account_id][1]
        self.gender=account[account_id][2]
        self.limit=account[account_id][3]
        self.balance=account[account_id][4]

    def account_info(self): #打印个人信息方法
        print'''Personal information form
\t\tid:\t\t\t%s
\t\tname:\t\t%s
\t\tage:\t\t%s
\t\tgender:\t\t%s
\t\tlimit:\t\t%s
\t\tbalance:\t%s'''%(self.id,self.name,self.age,self.gender,self.limit,self.balance)

    def withdraw(self): #提现
        draw=int(raw_input('请输入要取出的现金：'))
        b=draw*0.05
        self.balance=self.balance-draw-b
        if self.balance<=self.limit*0.5:
            print 'You can not go on cash top-up, please!'
        else:
            with open('account') as f_json:
                account=json.load(f_json)
                account[self.id][4]=self.balance
            with open('account','w') as f_json:
                json.dump(account,f_json)
            time_now=(time.strftime('%Y-%m-%d %H:%M:%S'))
            act='withdraw:%s balance:%s'%(draw,self.balance)
            opt_record='%s %s 取出现金%s\n'%(self.id,time_now,act)
            with open('credit_card.log','a') as f:
                f.write(opt_record)
            print('withdraw %s successfully balance %s'%(draw,self.balance))

    def refund(self):#还款
        refund_in=int(raw_input('请输入存入金额：'))
        self.balance=self.balance+refund_in
        with open('account') as f_json:
            account=json.load(f_json)
            account[self.id][4]=self.balance
        with open('account','w') as f_json:
            json.dump(account,f_json)
        opt_record='存入%s'%refund_in
        time_now=(time.strftime('%Y-%m-%d %H:%M:%S'))
        act='refund:%s balance:%s'%(refund_in,self.balance)
        opt_record='%s %s 还款金额%s\n'%(self.id,time_now,act)
        with open('credit_card.log','a') as f:
            f.write(opt_record)
        print('refund %s successfully balance %s'%(refund_in,self.balance))

    def record_opt(self): #还款
        with open('credit_card.log') as f:
            for i in f:
                if i.startswith(self.id):
                    print(i)
                else:
                    pass

    def bill(self):#账单
        with open('credit_card.log') as f:
            for i in f:
                if i.startswith(self.id):
                    print(i)
                else:
                    pass

    def trsfer_accounts(self):#转账
        account_id=raw_input('请输入对方的账户：')
        money=int(raw_input('输入转账金额：'))
        self.balance=self.balance-money
        if self.balance<=self.limit*0.5:
            print 'You can not continue to transfer!'
            return 0
        else:
            with open('account') as f_json:
                account=json.load(f_json)
                account[self.id][4]=self.balance
            with open('account','w') as f_json:
                json.dump(account,f_json)
        with open('account') as f_json:
            account=json.load(f_json)
            account[account_id][4]=account[account_id][4]+money
        with open('account','w') as f_json:
            json.dump(account,f_json)
        time_now=(time.strftime('%Y-%m-%d %H:%M:%S'))
        act='trafer_account:%s balance:%s'%(money,self.balance)
        opt_record='%s 对方id:%s %s 转账金额%s\n'%(account_id,self.id,time_now,act)
        with open('credit_card.log','a') as f:
            f.write(opt_record)
        print('trasfer_account %s successfully') %money