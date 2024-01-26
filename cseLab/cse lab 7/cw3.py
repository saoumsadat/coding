import numpy as np

def reverseArray(arr):
    for x in range(0, (len(arr) // 2) + 1):
        temp = arr[x]
        arr[x] = arr[(len(arr) - 1) - x]
        arr[len(arr) - 1 - x] = temp
    return arr

arr1 = np.array([10, 12, 20, 5, 7])
arr1 = reverseArray(arr1)
print(arr1)

arr2 = np.array([4, 2, 6, 5])
arr2 = reverseArray(arr2)
print(arr2)

