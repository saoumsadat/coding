s = input()
c = input()
temp = ""

for i in range(0, len(s)):
    if s[i] == c:
        print(temp)
        temp = ""
    else:
        temp += s[i]

print(temp)