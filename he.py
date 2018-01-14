"""
def _q():
	sum1 = 0#奇数和
	sum2 = 0#偶数和
	sum3 = 0#总和
	for i in range(1,101):
		if i%2 == 0:
			sum2 = sum2+i
		if i%2 != 0:
			sum1 = sum1+i
		sum3 = sum3+i
	print(sum3)
	print(sum2)
	print(sum1)
_q()
"""
#乘法口诀

def _a():
	for i in range(1,10):
		for j in range(1,i+1):
			print("%d*%d=%d"%(i,j,i*j),end= "\t")
		print("")
_a()
_a()























