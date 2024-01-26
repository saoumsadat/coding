q = int(input())

n = int(input())
min = max = sum = n

i = 0
while (i < q - 1):
    n = int(input())
    if (n < min):
        min = n
    elif (n > max):
        max = n
    sum += n
    
    i += 1

avg = sum / q

print("Maximum", max)
print("Minimum", min)
print("Average is", avg)
        
    