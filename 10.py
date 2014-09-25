num = [1]
for i in range (0,30):
	count = []
	for i in range(len(num)-1,-1,-1):
		x = num[i]
		if len(count) >= 2 and count[1]==x:
			count[0]+=1
		elif len(count) >= 2:
			count = [1,x] + count
		else:
			count = [1,x]
	num =count
print len(num)
