n = int(input())
if (n % 2 == 0 or n % 5 == 0):
    if (n % 2 == 0 and n % 5 == 0):
        print("Multiple of 2 and 5 both")
    else:
        print(n)
else:
    print("Not a multiple we want")