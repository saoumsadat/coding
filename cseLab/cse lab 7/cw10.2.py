import numpy as np

def transpose(m):
    t_m = np.zeros((len(m[0]), len(m)), dtype=int)
    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            t_m[j][i] = m[i][j]
    return t_m

def multiply(m1, m2):
    if len(m1[0]) != len(m2):
        return "Not multipliable"
    else:
        mp = np.zeros((len(m1), len(m2[0])), dtype=int)
        
        for i in range(0, len(m1)):
            for j in range(0, len(m2[0])):
                sum = 0
                for k in range(0, len(m2)):
                    sum += m1[i][k] * m2[k][j]
                mp[i][j] = sum
        
        return mp

A = np.array([[1,2,3,4],
              [1,4,9,16]])
t_A = transpose(A)
print(multiply(t_A, A))