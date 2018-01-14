zhanghao = 123
mima = 123
zh =int(input("请输入账号"))
mm =int(input("请输入密码"))
if zh == zhanghao and mm == mima:
	a =input("欢迎来到个人信息系统")
	print(a.center(20,"*"))
	list = []
while True:
		b =int(input("请选择功能1:新增 2:查询 3:修改 4:删除 5:退出"))

		if b == 1:
			name =input("请输入你的名字:")
			age =int(input("请输入你的年龄"))
			xingbie =input("请输入你的性别")
			gongzuo =input("请输入你的工作")
			list.append(name)
			list.append(age)
			list.append(xingbie)
			list.append(gongzuo)
		elif b == 2:
			position =int(input("请输入索引"))
			print(list[position])
		elif b == 3:
			oldname =input("请输入名字")
			newname =input("请输入新名字")
			list[0] = newname
			print(list)
		elif b == 4:
			delname =input("请输入你要删除的名字")
			list.remove(delname)
			print(list)
		elif b == 5:
			break
