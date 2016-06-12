#!/usr/bin/env python
import os
province=['hebei','henan','shanxi']
city={'hebei':['shijiazhuang','baoding','handan'],'henan':['zhengzhou','kaifeng'
,'luoyang'],'shanxi':['taiyuan','linfen','yangquan']}
city_list_all=city['hebei']+city['henan']+city['shanxi']
country={'shijiazhuang':['jingxingxian','zhengding','luquan'],
'baoding':['yixian','xushui','yongdingxian'],
'handan':['chenganxian','lizhangxian','shexian'],
'zhengzhou':['gongyi','shangjie','gaoxin'],
'kaifeng':['qixian','tongxuxian','weishixian'],
'luoyang':['xinan','luoningxian','yiningxian'],
'taiyuan':['qingxuxian','yangquxian','loufanxian'],
'linfen':['hongtongxian','zhaocheng','jialing'],
'yangquan':['mengxian','pingdingxian','cheng']}
select_next=['exit','back_province','back_city']
def menu():
	print'''
	++++++++++++++++++++++++
	+   1.province select  +
	+   2.city select      +
	+   3.show_city_all    +
	+   4.show_country_all +
	+   5.eixt program     +
	++++++++++++++++++++++++	
	'''
	op=raw_input('please select on>>>')
	return op
def menu_exit():
	os._exit(0)
def menu_error():
	print 'Unkonw options,Please try again!'
def province_select():
	global province_input
	while 1:
		province_input=raw_input('please input province select in %s:' %province)
		if province_input in city:
			print '''=======================================
					
%s
					
=======================================''' %city[province_input]
			while 1:
				city_input=raw_input('please input city select in %s:' %city[province_input])
				if city_input in country: 
					print '''=======================================

%s

======================================='''%country[city_input]
					main()
				else:
					print 'Please choose city again'
					continue
		else:
			print 'Please choose province again'
			continue
def city_select():
		while 1:
			city_input=raw_input('please input city select in %s:' %city_list_all)
			if city_input in country:
				print '''=======================================

%s

======================================='''%country[city_input]
				break
			else:
				print 'Please choose city again'
				continue
def city_all():
	a=[]
	count=0
	for i in city.values():
		a.extend(i)
	print '============================='
	for city_single in  city_list_all:
		count+=1
		print '%s.%s' %(count,city_single)
	print '============================='
def country_all():
	a=[]
	count=0
	for i in country.values():
		a.extend(i)
	print '============================='
	for country_single in a:
		count+=1
		print '%s.%s' %(count,country_single)
	print '============================='
ops={'1':province_select,
	'2':city_select,
	'3':city_all,
	'4':country_all,
	'5':menu_exit}
def main():
	while True:
		op = menu()
		ops.get(op,menu_error)()
main()
