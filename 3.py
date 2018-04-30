import math

def findFactor(num):
    end = math.ceil(math.sqrt(num))
    boolean = False
    for i in range(2,end):
        if num % i == 0:
            largestFactor = num//i
            boolean = checkPrime(largestFactor)
            if boolean == True:
                return largestFactor
    for index in range(end+1,2,-1):
        if num % index == 0:
            boolean = checkPrime(index)
            if boolean == True:
                return index


def checkPrime(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

largestPrimeFactor = findFactor (600851475143)
print(largestPrimeFactor)