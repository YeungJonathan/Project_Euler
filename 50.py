#not done

def checkPrime(num):
	for n in range(2, int(num**(1/2)+1)):
		if num % n == 0:
			return False
	return True
	

def eratosthenesSieve(n):
	primesDictionary = {i:True for i in range(2, n+1)}
	rootN = n**(1/2)
	for i in range(2, int(rootN) + 1):
		if primesDictionary[i]:
			j = i**2
			while j <= n:
				primesDictionary[j] = False
				j += i
			
	return [i for i in primesDictionary if primesDictionary[i]]

maxPrime = 0
tmp = 0
prime = eratosthenesSieve(1000000)
for i in range(len(prime)):
	tmp += prime[i]
	isPrime = checkPrime(tmp)
	if isPrime:
		maxPrime = tmp
print(maxPrime)