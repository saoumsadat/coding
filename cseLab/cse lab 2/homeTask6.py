num1 = 10
num2 = -3
num3 = -1
sum = num1 + num2 + num3
if (num3 < 0):
    print(num3 * -2) #2
else:
    print(sum)
if (num1 < 5):
    print(num1 + 10)
elif (num2 == -3):
    num2 = num1  #num2 = 10
    print(num2)  #10
else:
    print(num1 + num2 + num3)
if (num1 > 15):
    print(num1)
elif (num2 == 0):
    print(num2 + num3)
else:
    print(num3)  #-1
if (sum != 0):
    print(100)  #100
else:
    print(sum + 100)
if (num1 > 0 and num2 < 0):
    print(num1 == num2)
else:
    print("False")   #False

