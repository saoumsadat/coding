def is_even(n):
    if n % 2 == 0:
        result = True
    else:
        result = False
    return result

def is_pos(n):
    if n >= 0:
        result = True
    else:
        result = False
    return result

def sequence(n):
    if is_pos(n):
        for x in range(0, n + 1):
            if is_even(x):
                print(x, end=" ")
        print()
    else:
        for x in range(n, 0):
            if not(is_even(x)):
                print(x, end=" ")
        print()

sequence(10)
sequence(-7)
sequence(7)
sequence(-8)