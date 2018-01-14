shitou = 1
jiandao = 2
bu =3

import random
diannao = random.randint(1,3)
my = int(input("请输入1,2,3:"))

if (my == 1 and diannao == 2) or (my == 2 and diannao == 3) or (my == 3 and diannao == 1):
	print("你赢啦")
elif (my == 1 and diannao ==3) or (my == 3 and diannao == 2) or (my ==2 and dainnao == 1):
	print("你输了")
else:
	print("平局")
