#密码重设程序
#passwor = 'a123456'
#让用户输入密码
#最多输入3此
#如果正确就印出'登录成功'
#如果错误就印出'密码错误，你好友__次机会'

n = 3
while True:
	password = input('请输入密码')
	if password != 'a123456':
		n = n - 1
		print('密码错误，你还有',n,'次机会')
		if n < 1:
			print('机会用完')
			break
	else:
		print('登录成功')
		break

