def sequence_iterative(n):
    flag = 0
    sum = 0
    for x in range(1, n + 1):
        if not(flag):
            sum += x
        else:
            sum += -x
        flag = not(flag)
    return sum

N = int(input())
y = sequence_iterative(N)
print(y)