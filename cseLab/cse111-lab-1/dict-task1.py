d1 = {
    'a': 100, 
    'b': 100, 
    'c': 200, 
    'd': 300
}
d2 = {
    'a': 300,
    'b': 200,
    'd': 400,
    'e': 200
}

d = dict()

for key in d1.keys():
    if key in d2.keys():
        d[key] = d1[key] + d2[key]
    else:
        d[key] = d1[key]

for key in d2.keys():
    if key not in d1.keys():
        d[key] = d2[key]

print(d)