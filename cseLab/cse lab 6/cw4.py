l1 = [1, 4, 3, 2, 5]
l2 = [8, 7, 6, 9]

flag = False

for x in l1:
    if x in l2:
        flag = True

print(flag)