"""
a = 1

while a <=7:
	print("*"*a)
	a+=1
"""

#乘法口诀
for a in range(1,10):
	for b in range(1,1+a):
		print("%d*%d=%d"%(b,a,a*b),end="\t")
	print("")
