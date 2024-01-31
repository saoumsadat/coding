def sort(s):
    for x in range(0, len(s)):
        for y in range(x + 1, len(s)):
            if s[x] > s[y]:
                temp = s[x]
                s[x] = s[y]
                s[y] = temp

def arrToStr(a):
    s = ''
    for x in range(0, len(a)):
        s += a[x]
    return s

s = input()
low = []
up = []
odd = []
even = []
for x in s:
    if x >= 'a' and x <= 'z':
        low.append(x)
    elif x >= 'A' and x <= 'Z':
        up.append(x)
    elif (int(x) % 2 != 0):
        odd.append(x)
    elif (int(x) % 2 == 0):
        even.append(x)

sort(low)
sort(up)
sort(odd)
sort(even)

print(arrToStr(low) + arrToStr(up) + arrToStr(odd) + arrToStr(even))

