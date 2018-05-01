def primeDictionary(num):
    primeSet={}
    for i in range(2,num+1):
        boolean = False
        boolean = findPrime(i)
        if boolean == True:
            primeSet[i] = 0
    return primeSet

def findPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def updateDictionary(primeSet, num):
    for i in range(2,num+1):
        for j in range(2,i+1):
            if i % j == 0:
                primeSet[j] = primeSet[j]+1

    return primeSet


primeSet = primeDictionary(20)
primeSet = updateDictionary(primeSet, 20)
print(primeSet)