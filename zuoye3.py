zhanghao = 123
mima = 123
i = 0
while i<3:
	zh = int(input("请输入你的账号:"))
	mm = int(input("请输入你的密码:"))	
	if zh == zhanghao and mm == mima:
		print("	登录成功,大吉大利今晚吃鸡")
		break
	else:
		print("账号或密码错误,登录失败")
	i+=1
else:
	print("因为您多次输入失败,请稍后再试")
