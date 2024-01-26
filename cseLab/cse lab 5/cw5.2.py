def reverse_printing(st, n):
    if st > n:
        return
    print(n, end=" ")
    reverse_printing(st, n - 1)

reverse_printing(1, 5)