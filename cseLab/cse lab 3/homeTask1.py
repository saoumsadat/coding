N = int(input())
sum = 0

i = 7
while i <= N:
    if (i % 7 == 0 and i % 9 != 0) or (i % 7 != 0 and i % 9 == 0):
        sum += i
    i += 1
    
    
print(sum)