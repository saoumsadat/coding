s = input()
new_s = ''
for i in range(1, len(s), 2):
    if s[i] >= "A" and s[i] <= "Z":
        new_s += s[i]
    else:
        new_s += chr(ord(s[i]) - 32)

print(new_s)