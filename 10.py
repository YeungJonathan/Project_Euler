# def checkPrime(num):
#    for i in range(2,(num//2)+1):
#        remainder = num%i
#        if remainder == 0:
#            return False
#    return True
#
# sum = 0
# for index in range(3,2000000,2):
#    boolean = checkPrime(index)
#    print(index)
#    if boolean == True:
#        sum += index
# print(sum)


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

print(sum(eratosthenesSieve(2*(10**6))))