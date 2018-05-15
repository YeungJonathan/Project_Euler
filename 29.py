dict = {}
for a in range(2, 101):
	for b in range(2, 101):
		num = a**b
		dict[num] = 1
print(len((dict)))