def power(b, e):
    if e == 0:
        return 1
    else:
        return b * power(b, e - 1)

print(power(2, 4))