def sumOfSquares(num):
    sum = 0
    for i in range(1, num+1):
        sum = sum + i**2
    return sum

def squareOfSum(num):
    sum = 0
    for i in range(1, num+1):
        sum = sum + i
    sum = sum**2
    return sum

if __name__ == '__main__':
    num = int(input("Please input a natural number: "))
    assert num >= 0, "Number less than 0"
    sumSquare = sumOfSquares(num)
    squareSum = squareOfSum(num)
    ans = sumSquare - squareSum
    print(ans)