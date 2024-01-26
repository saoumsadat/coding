n = int(input())

#counting digits
dig_count = 0
temp = n    #storing to a temp variable so the original num is intact
while (temp != 0):
    temp = temp // 10
    dig_count += 1
    
# print(dig_count)

#printing till index -2 
i = 1
while i < dig_count:
    print(f"{n // 10**(dig_count - i)}, ", end="")
    n = n % 10**(dig_count - i)
    i += 1
    
print(n) #printing the last digit without comma