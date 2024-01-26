import numpy as np

vec1 = np.array([1,2,3])
vec2 = np.array([4,5,6])


dot = 0
for x in range(0, len(vec1)):
    dot += (vec1[x] * vec2[x])    

print(f"Dot Product: {dot}")

if dot % 2 == 0:
    for x in range(0, len(vec1)):
        if x % 2 == 0:
            temp = vec1[x]
            vec1[x] = vec2[x]
            vec2[x] = temp
else:
    for x in range(0, len(vec1)):
        if x % 2 != 0:
            temp = vec1[x]
            vec1[x] = vec2[x]
            vec2[x] = temp

print(f'''After Swapping:
{vec1}
{vec2}''')
