def collatz(num):
	if num % 2 == 1:
		num = 3 * num + 1
	else:
		num = num // 2
	return num
	
check = {1:1}
maxValue = 1
maxNum = 1
for num in range(2,1000001):
	item = num
	count = 1
	final = 0
	while item != 1:
		if item in check.keys():
			count = count + check[item]
			break
		else:
			item = collatz(item)
			count = count + 1
	if count > maxValue:
		maxNum = num
		maxValue = count
	check[num] = count
				
print(maxNum)

				