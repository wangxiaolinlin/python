count = 0
while count <= 9:
		row = 1
		while row <= count:
			print("%d*%d=%d"%(count,row,count*row),end="/t")
			row+=1
		print("")
		count+=1
