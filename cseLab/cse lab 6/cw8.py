l = []

for i in range(0, 5):
    s = input()
    elem = ''
    in_l = []
    for x in s:
        if (x >= "A" and x <= "Z") or (x >= "a" and x <= "z") or (x >= "0" and x <= "9") or (x == '.'):
            elem += x
        elif (x == ","):
            in_l.append(elem)
            elem = ''
        elif (x == "]"):
            in_l.append(float(elem))
    l.append(in_l)
    print(l)

