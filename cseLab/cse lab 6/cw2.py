s = input()

num_count = 1
for x in s:
    if x == ',':
        num_count += 1

print(num_count)

l = [0] * num_count

num = ''
i = 0
j = len(l) - 1
while i < len(s):
    if (s[i] >= '0' and s[i] <= '9') or s[i] == '-':
        num += s[i]
    elif num != '':
        l[j] = int(num)
        num = ''
        j -= 1
    i += 1

print(l)