s = input()
rev_s = ''

for i in range(len(s) - 1, -1, -1):
    rev_s += s[i]

print(rev_s)
    