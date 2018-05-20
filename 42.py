dic = {}
for n in range(250):
	dic[int(1/2*(n)*(n+1))] = 1

alphabet = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,
	'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,
	'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

count = 0
f = open('words.txt')
text = f.read().split(',')
for word in text:
	word = word[1:-1].lower()
	value = 0
	for letter in word:
		value += alphabet[letter]
	try:
		a = dic[value]
		count+= 1
	except:
		continue
print(count)