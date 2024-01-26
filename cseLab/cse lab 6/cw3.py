s = input()
l = []
num = ''
count = 0
for x in range(0, len(s)):
    if s[x] >= '0' and s[x] <= '9':
        num += s[x]
    if s[x] == "," or x == len(s) - 1:
        l.append(int(num))
        num = ""

new_l = []
if len(l) >= 4:
    for x in range(0, len(l)):
        if x > 1 and x < (len(l) - 2):
            new_l.append(l[x])
    print(new_l)
else:
    print("Not possible")