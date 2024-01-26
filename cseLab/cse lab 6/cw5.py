l1 = [1, 3, 5, 7, 9, 10]
l2 = [2, 4, 6, 8]

new_l1 = [0] * (len(l1) - 1)
for x in range(0, len(new_l1)):
    new_l1[x] = l1[x]

print(new_l1 + l2)