#!/usr/bin/env python
#coding:utf-8
__author__ = 'bobo'
from credit_card import credit_card
from logon import login
from shop import main
import sys
login_return=login()


def credit_menu():
    print'''
	    +++++++++++++++++++++++++
	    +   1.购物商城          +
	    +   2.提现              +
	    +   3.还款              +
	    +   4.交易记录          +
	    +   5.账单              +
	    +   6.转账              +
	    +   7.账户信息          +
	    +   8.退出登录          +
	    +++++++++++++++++++++++++
	    '''
    credit_op=raw_input('please select one>>>')
    return credit_op

def exit_credit_card():
	sys.exit()

ops={'1':main,
	'2':credit_card(login_return).withdraw,
	'3':credit_card(login_return).refund,
	 '4':credit_card(login_return).record_opt(),
	 '5':credit_card(login_return).bill,
	 '6':credit_card(login_return).trsfer_accounts,
	 '7':credit_card(login_return).account_info,
	 '8':exit_credit_card}
def menu_error():
	print '未知的操作，请输入正确的操作'

def credit_main():
    while True:
        credit_op = credit_menu()
        ops.get(credit_op	,menu_error)()
if __name__=='__main__':
	credit_main()
