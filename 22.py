import string

dictionary = dict(zip(string.ascii_uppercase,range(1,27)))
tmpList = []
for f in open('names.txt'):
	tmpList = f.split(',')
for i in range(len(tmpList)):
	tmpList[i] = tmpList[i][1:len(tmpList[i])-1]

tmpList = sorted(tmpList)

finalsum = 0
for index, names in enumerate(tmpList, start = 0):
	tmpsum = 0
	for char in names:
		tmpsum += dictionary[char]
	finalsum += tmpsum * index
print(finalsum)