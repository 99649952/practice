#!/usr/bin/env python
import getpass
information={'lxb':'123','alex':'234','liao':'345','wusir':'456'}
while True:
	count=0
	user_input=raw_input('user:')
	if user_input in information.keys():
		f=open('fail_account.txt')
		a=f.read()
		user_lock=a.split()
		f.close()
		if user_input in user_lock:
				print 'account already lock'
				continue
		while(count<3):
			passwd_input=getpass.getpass('password:')
			if passwd_input == information[user_input]:
				print 'congratulation longin successfully!!!'
				break
			elif passwd_input == '':
				print 'The password you entered is empty, please enter again.'
			else:
				count +=1
				print 'you are fail %s' %count
				if count == 3:
					f=file('fail_account.txt','a')
					f.write(user_input)
					f.write('\n')
					f.close()
	else:
		print 'user not exist'
