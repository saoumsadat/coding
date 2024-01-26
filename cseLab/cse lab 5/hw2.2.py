def show_palindrome(n):

    for x in range(1, n + 1):
        print(x, end="")
    
    for x in range(n - 1, 0, -1):
        print(x, end="")

show_palindrome(3)