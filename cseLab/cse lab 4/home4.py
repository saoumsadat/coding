s = input()
new_s = ''
flag = 1
for x in s:
    if flag:
        if x >= 'a' and x <= 'z':
            new_s += chr(ord(x) - (ord('a') - ord('A')))
            flag = 0
        elif x >= 'A' and x <= 'Z':
            new_s += x
            flag = 0
        else:
            new_s += x
    else:
        if x >= 'A' and x <= 'Z':
            new_s += chr(ord(x) + (ord('a') - ord('A')))
            flag = 1
        elif x >= 'a' and x <= 'z':
            new_s += x
            flag = 1
        else:
            new_s += x

print(new_s)