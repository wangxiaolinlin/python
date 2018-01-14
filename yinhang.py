#银行取钱
kahao = 10086
mima = 10086
i = 0
while i<3:
	i+=1
	kh =int(input("请输入您的银行卡号:"))
	mm =int(input("请输入您的银行卡密码,请注意周边环境:"))
	if kh == kahao and mm == mima:
		print("输入正确,请选择以下您需要的服务")
		moshi =int(input("1存钱 2取钱 3查看余额"))
		if moshi == 1:
			money = 1000
			cunqian =int(input("请输入你要存的金额"))
			if cunqian > 0:
				print("存款金额为%d元 剩余金额为%d元"%(cunqian,cunqian+money))
		elif moshi == 2:
			money = 1000
			quqian =int(input("请输入你要取得金额"))
			if quqian < 1000:
				print("取钱为%d元 剩余%d元"%(quqian,money-quqian))
			else:
				print("自己有多少钱没点逼数吗?")
		elif moshi == 3:
			money = 100000000
			print("当前余额为%d元"%money)
			break
	else:
		print("你是傻逼吗?输入错误")
else:
	print("由于您多次输入错误,所以下辈子再来吧")
















