#not done

found = False
num = 2
while not found:
	dic = {}
	string = list(str(num))
	for item in string:
		try:
			dic[item] = dic[item]+1
		except:
			dic[item] = 1

	lst = [2*num, 3*num, 4*num, 5*num, 6*num]
	for item in lst:
		for char in str(item):
			