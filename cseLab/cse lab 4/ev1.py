string = input()
binary = True

for i in range(0, len(string)):
    if (string[i] != "1" and string[i] != "0"):
        binary = False
        break

if binary:
    print("Binary Number")
else:
    print("Not a Binary Number")
