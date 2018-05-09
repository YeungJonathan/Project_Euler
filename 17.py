dic = {}
dic[1] = len('one')  #one
dic[2] = len('two')  #two
dic[3] = len('three')  #three
dic[4] = len('four')  #four
dic[5] = len('five')  #five
dic[6] = len('six')  #six
dic[7] = len('seven')  #seven
dic[8] = len('eight')  #eight
dic[9] = len('nine')  #nine
dic[10] = len('ten') #ten
dic[11] = len('eleven') #eleven
dic[12] = len('twelve') #twelve
dic[13] = len('thirteen')
dic[14] = len('fourteen')
dic[15] = len('fifteen')
dic[16] = len('sixteen')
dic[17] = len('seventeen')
dic[18] = len('eighteen')
dic[19] = len('nineteen')
dic[20] = len('twenty')
dic[30] = len('thirty')
dic[40] = len('forty')
dic[50] = len('fifty')
dic[60] = len('sixty')
dic[70] = len('seventy')
dic[80] = len('eighty')
dic[90] = len('ninety')
dic[100] = len('hundred')
dic[1000] = len('thousand')

sum = 0
for num in range(1,1001):
    if len(str(num)) == 1 or (len(str(num))== 2 and list(str(num))[0] == '1') and num == 20:
        sum += dic[num]

    elif len(str(num)) == 2:
        sum = sum + dic[int(list(str(num))[0])*10]
        if int(list(str(num))[1])!= 0 :
            sum = sum + dic[int(list(str(num))[1])]

    elif len(str(num)) == 3:
        if list(str(num))[1] == '0' and list(str(num))[2] == '0':
            sum = sum + dic[int(list(str(num))[0])] + dic[100]
        elif list(str(num))[1] == '0' and list(str(num))[2] != '0':
            sum = sum + dic[int(list(str(num))[0])] + dic[100] + len('and') + dic[int(list(str(num))[2])]
        elif list(str(num))[1] != '0' and list(str(num))[2] == '0':
            sum = sum + dic[int(list(str(num))[0])] + dic[100] + len('and') + dic[int(list(str(num))[1])*10]
        elif list(str(num))[1] != '0' and list(str(num))[2] != '0':
            sum = sum + dic[int(list(str(num))[0])] + dic[100] + len('and') + dic[int(list(str(num))[1])*10] + dic[int(list(str(num))[2])]

    elif num == 1000:
        sum += dic[1] + dic[1000]
print(sum)