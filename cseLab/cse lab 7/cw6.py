import numpy as np

def create_array(n):
    arr = np.zeros(n, dtype=int)
    for x in range(0, n):
        elem = int(input())
        arr[x] = elem
    return arr

def selection_sort_array(arr):
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

n = int(input())
arr = create_array(n)
selection_sort_array(arr)
print(arr)