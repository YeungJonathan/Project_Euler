sum = 0
for i in range(1, 1001):
	sum += i**i
for i in range(-10, 0,1):
	print(str(sum)[i], end = '')