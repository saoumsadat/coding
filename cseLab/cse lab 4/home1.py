s = input()
flag = ""
new_s = ""

for i in s:
    if flag != i:
        new_s += i
        flag = i
print(new_s)