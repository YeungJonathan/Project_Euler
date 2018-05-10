num = 100
factorial = 1
sum = 0
for i in range(1, num+1):
	factorial *= i
print(len(str(factorial)))
for item in str(factorial):
	sum += int(item)
print(sum)