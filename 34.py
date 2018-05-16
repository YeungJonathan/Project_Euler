import math
dic = {}
count = []
for i in range(2,1000000):
	tmpsum = 0
	tmp = str(i)
	for item in tmp:
		try:
			tmpsum += dic[int(item)]
		except:
			fac = math.factorial(int(item))
			dic[int(item)] = fac
			tmpsum += fac
	if tmpsum == i:
		count.append(i)
print(sum(count))
			