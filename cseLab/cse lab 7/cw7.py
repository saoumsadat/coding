import numpy as np

def flatten(arr2d):
    elem_count = 0
    for i in range(0, len(arr2d)):
        elem_count += len(arr2d[i])

    arr1d = np.zeros(elem_count, dtype=int)

    index = 0
    for i in range(0, len(arr2d)):
        for j in range(0, len(arr2d[i])):
            arr1d[index] = arr2d[i][j]
            index += 1

    return arr1d


arr1 = np.array([[1, 2, 3], 
                 [3, 4, 5]] )
arr2 = flatten(arr1)
print(arr2)

arr3 = np.array([[1, 4], 
                 [5, 6],
                 [8, 9]])
arr4 = flatten(arr3)
print(arr4)
