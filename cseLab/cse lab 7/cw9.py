import numpy as np

def diag_diff(matrix):
    prim_sum = 0
    sec_sum = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if i == j:
                prim_sum += matrix[i][j]
            elif i + j == len(matrix) - 1:
                sec_sum += matrix[i][j]

    total = prim_sum - sec_sum
    if total < 0:
        return -total
    else:
        return total

A = np.array([[1,  5,  12,  1],
              [2,  -4,  6,  7],
              [3,  8,  5,  9],
              [3,  5,  23,  -6]])

print(diag_diff(A))