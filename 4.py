def palindrome(product):
    product= str(product)
    n=len(product)//2
    for i in range(n):
        if product[i]!=product[-i-1]:
            return False
    return True


for i in range(999, 900,-1):
    for j in range(999, 900, -1):
        product=i*j
        ans = palindrome(product)
        if ans==True:
            print(product)