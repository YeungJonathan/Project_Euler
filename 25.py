lst = [1,1]
hasFound = False
while not hasFound:
	tmp = lst[-1]+lst[-2]
	lst.append(tmp)
	if len(str(tmp)) == 1000:
		hasFound = True

print(len(lst))
