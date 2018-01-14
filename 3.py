zhanghao =int(input("欢迎来到王者荣耀,请输入账号:"))
mima =int(input("请输入密码:"))
zh = 123
mm = 123
i = 1
k = 0
if zhanghao == zh and mima == mm:
	print("登录成功")
	yx = input("请选择英雄范围1.adc 2.坦克 3.fashi")
	if yx == "1":
			print("鲁班")
	if yx == "2":
			print("程咬金")
	if yx == "3":
			print("王昭君")
if zhanghao != zh or mima != mm:
	while i<3:
		i+=1
		print("账号或密码错误")
		zhanghao =int(input("欢迎来到王者荣耀,请输入账号:"))
		mima =int(input("请重新输入密码"))

