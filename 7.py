def findPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

count = 1
num = 3
while count < 10001:
    boolean = findPrime(num)
    if boolean == True:
        count += 1
    num += 1
    
    
    
print(num -1)
