import numpy as np

def identity_check(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if i == j and matrix[i][j] != 1:
                return False
            elif i != j and matrix[i][j] != 0:
                return False
    return True

A = np.array([[1,  0,  0],
              [0,  1,  0],
              [0,  0,  1]])

if(identity_check(A)):
    print("Identity Matrix")
else:
    print("Not an Identity Matrix")