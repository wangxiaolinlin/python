"""
name = "wanglin"
for a in name:
	print("身体各个部分%S"%a)
"""
"""
for i in range (0,101,1):
	print(i)
"""
osum = 0
jsum = 0
zsum = 0




for i in range (0,101):
if i % 2 == 0:
		osum = i + osum
	if i % 2 != 0:
		jsum = i + jsum
		zsum = i + zsum
print(osum)
print(jsum)
print(zsum)
