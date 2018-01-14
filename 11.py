"""
def sum(sum1,sum2):
	for i in range(sum1,sum2):
		for j in range(1,i+1):
			print("%dx%d=%d"%(i,j,i*j),end="\t")
		print("")
sum(1,10)
"""
def money(count):
	mymoney =count+99
	return mymoney
c = money(1)
print(c)
