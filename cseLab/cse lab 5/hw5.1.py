def sequence_iterative(n):
    if n == 0:
        return n
    if n % 2 != 0:
        return n + sequence_iterative(n - 1)
    else:
        return -n + sequence_iterative(n - 1)
    
n = int(input())
y = sequence_iterative(n)
print(y)

