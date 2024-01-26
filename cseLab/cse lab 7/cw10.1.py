import numpy as np 

def transpose(m):
    t_m = np.zeros((len(m[0]), len(m)), dtype=int)
    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            t_m[j][i] = m[i][j]
    return t_m

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print(transpose(A))