#!/usr/bin/env python
import os
province=['hebei','henan','shanxi']
city={'hebei':['shijiazhuang','baoding','handan'],'henan':['zhengzhou','kaifeng'
,'luoyang'],'shanxi':['taiyuan','linfen','yangquan']}
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
	+++++++++++++++++++++++
	+   1.province select +
	+   2.city select     +
	+   3.eixt program    +
	+++++++++++++++++++++++	
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
	if globals().has_key('province_input'):
		while 1:
			city_input=raw_input('please input city select in %s:' %city[province_input])
			if city_input in country:
				print '''=======================================

%s

======================================='''%country[city_input]
				break
			else:
				print 'Please choose city again'
				continue
	else:
		print 'Please select a province first'
def province_all():
	print 
ops={'1':province_select,
	'2':city_select,
	'3':menu_exit}
def main():
	while True:
		op = menu()
		ops.get(op,menu_error)()
main()
