def reverse_digits(n):
    if not(n):
        return
    print(n % 10)
    reverse_digits(n // 10)

reverse_digits(1000)