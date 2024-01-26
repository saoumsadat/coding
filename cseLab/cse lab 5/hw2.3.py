def show_palindrome(n):
    for x in range(1, n + 1):
        print(x, end="")
    for x in range(n - 1, 0, -1):
        print(x, end="")

def show_dots(n):
    print(n * ".", end="")

def show_triangle(n):
    for x in range(1, n + 1):
        show_dots(n - x)
        show_palindrome(x)
        show_dots(n - x)
        print()

show_triangle(3)