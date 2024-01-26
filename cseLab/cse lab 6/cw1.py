# #with append
l = []
for x in range(0, 5):
    n = int(input())
    l.append(n)
    print(l)

#without append
l = []
for x in range(0, 5):
    newl = [0] * (len(l) + 1)
    for i in range(0, len(l)):
        newl[i] = l[i]
    newl[x] = int(input())
    l = newl
    print(l)
