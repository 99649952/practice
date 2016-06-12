#!/usr/bin/env python
import sys
province=['hebei','henan','shanxi']
city={'hebei':['shijiazhuang','baoding','handan'],'henan':['zhengzhou','kaifeng','luoyang'],'shanxi':['taiyuan','linfen','yangquan']}
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
while 1:
	province_input=raw_input('please input province select in %s:' %province)
	if province_input in province:
		while 1:
			city_input=raw_input('please input city select in %s:' %city[province_input])
			if city_input in city[province_input]:
				print country[city_input]
				back_input=raw_input('What would you like to do next select in %s:' %select_next)
				if back_input == 'exit':
					sys.exit()
				elif back_input == 'back_province':
					break
				elif back_input == 'back_city':
					continue
				else:
					print 'Please enter the correct option'
			else:
				print 'Please choose city again'
				continue
	else:
		print 'Please choose province again'
