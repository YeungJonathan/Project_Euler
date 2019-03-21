sumNum=0
first=1
second=1
nextNum=first+second
while second<4000000:
    nextNum=first+second
    if nextNum<4000000 and nextNum%2==0:
        sumNum+=nextNum
    first=second
    second=nextNum
print(sumNum)
