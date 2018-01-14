import random
a = random.randint(0,100)
b =int(input("猜猜我今天捡了多少钱:"))
i = 0
while i < 10:
	i+=1
	if b > a:
		print("错了,没捡这么多")
	elif b < a:
		print("错了,没捡这么少")
	b =int(input("请重新猜"))	
		
	
	if b == a:
		print("猜对啦!!!")
		break
