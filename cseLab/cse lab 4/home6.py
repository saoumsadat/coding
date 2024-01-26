test = ""
i = 5
j = 0
k = 15
while i< 10:
    k-=1
    j = k
    while 5 < j - 5:
        if (j % 2) == 0:
            test = "<--"
            test = str(test) + str(i) + str(2) + "-->" + str(int(j / 2))  
        else:
            test = "-->"
            test = "-->" + str(int(i / 2)) + str(test) + str(j)
        print(test)
        j = j-1
    i+=1

print(i, j, k)