zhanghao = 123
mima = 123
zh =int(input("请输入你的账号:"))
mm =int(input("请输入你的密码,请注意周边环境:"))
if zh == zhanghao and mm == mima:
	print("登录成功,请选择你需要的服务:")
	moshi =int(input("1:取钱 2:存钱 3:查看余额"))
	if moshi == 1:
		money = 100
		quqian =int(input("请输入你要取的钱数:"))
		if quqian<100:
			print("您以取走%d元 账户余额剩余%d元"%(quqian,money-quqian))
	elif moshi == 2:
		money = 100
		cunqian =int(input("请输入您要存的钱数:"))
		if cunqian>100:
			print("您以存入%d元 账户余额剩余%d元%"(cunqian,money+cunqian))
	elif moshi == 3:
		money == 50000000
