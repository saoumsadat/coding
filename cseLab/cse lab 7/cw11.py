import numpy as np

def task11(m):
    row = len(m)
    col = len(m[0])
    mres = np.zeros((row, col), dtype=float)

    abs_val = row - col
    if abs_val < 0:
        abs_val = -abs_val
    
    rem = abs_val % row

    sum = 0
    for i in range(0, len(m[0])):
        sum += m[rem][i]
    avg = round(sum / len(m[0]), 2)
    
    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            mres[i][j] = m[i][j] * avg

    return mres

A = np.array([[4,1,2],
              [9,3,7]])

print(task11(A))

B = np.array([[6,3], 
              [1,5]])

print(task11(B))