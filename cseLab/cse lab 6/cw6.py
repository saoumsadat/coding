list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [10, 11, 12, -13, -14, -15,-16]

list = []

for x in list1:
    if x % 2 == 0:
        list.append(x)

for x in list2:
    if x % 2 == 0:
        list.append(x)

print(list)