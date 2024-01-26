import numpy as np

def insert(m, start, end, s_m, index, sign):
    if sign == 'r':
        for i in range(start, end + 1):
            s_m[index] = m[start][i]
            index += 1
    elif sign == 'd':
        for i in range(start + 1, end + 1):
            s_m[index] = m[i][end]
            index += 1
    elif sign == 'l':
        for i in range(end - 1, start - 1, -1):
            s_m[index] = m[end][i]
            index += 1
    elif sign == 'u':
        for i in range(end - 1, start, -1):
            s_m[index] = m[i][start]
            index += 1
   
    return [s_m, index]

def spiral(m, s_m):
    start = 0
    end = len(m[0]) - 1
    up = [s_m, 0]
    while start <= end:
        right = insert(m, start, end, up[0], up[1], 'r')
        down = insert(m, start, end, right[0], right[1], 'd')
        left = insert(m, start, end, down[0], down[1], 'l')
        up = insert(m, start, end, left[0], left[1], 'u')
        start += 1
        end -= 1
    return s_m


A = np.array([[1, 2, 3],
              [8, 9, 4],
              [7, 6, 5]])

s_A = np.zeros(len(A) * len(A[0]), dtype=int)

print(spiral(A, s_A))