s = input()
new_s = ""
for i in s:
    if i == 'z':
        new_s += 'a'
    else:
        new_s += chr(ord(i) + 1)

print(new_s)