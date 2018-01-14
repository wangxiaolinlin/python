list = []
def a():
	while True:
		zidian = {}
		gn = int(input("欢迎来到名片管理系统,请选择1:新增名片 2:查询 3:修改: 4:删除 5:退出"))
		if gn == 1:
			name = input("请输入要添加的名字:")
			age = input("请输入要添加的年龄:")
			sex = input("请输入性别:")
			zidian["name"]=name
			zidian["age"] =age
			zidian["sex"]=sex
			list.append(zidian)
			for i in list:
				for k,v in i.items():
					print("%s:%s"%(k,v))
	
					
		if gn == 2:						
			chaxun =input("请输入要查询的名字:")
			for zidian in list:
				if chaxun == zidian["name"]:
					print("名字:%s 年龄:%s 性别:%s"%(zidian["name"],zidian["age"],zidian["sex"]))
							
		if gn == 3:
			name =input("请输入要修改的名字:")
			for zidian in list:
					if zidian["name"] == name:
							name2 = input("请输入要修改的新名字:")
							zidian["name"] = name2
							gn = int(input("修改成功,请通过2:查询来查看是否修改成功"))
		if gn == 4:
			name = input("请输入要删除的名字:")
			d = 0
			for zidian in list:
				if zidian["name"] == name:
					del list[d]
				else:
					d+=1
				gn = int(input("删除成功,请选择2:查询来查看是否删除成功"))
				print("您输入的名字不存在")
		if gn == 5:
			print("退出")
					
			break
xitong = "欢迎进入个人名片管理系统"
print(xitong.center(65,"*"))
zhanghao = 1105
mima = 1105
zh = int(input("请输入账号:"))
mm = int(input("请输入密码:"))
if zh == zhanghao and mm == mima:
	print("登录成功")
	a()
else:
	print("账号或密码错误")






