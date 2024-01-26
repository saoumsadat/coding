import numpy as np

def printPairs(arr, val):
    pair_count = 0
    for i in range(0, len(arr)):
        rem = val - arr[i]
        if rem in arr[i + 1:]:
            pair_count += 1
            print(f"{arr[i]}, {rem}")
    if not(pair_count):
        print("No Pair Found")

arr1 = np.array([7,8,10,5,3,4,2])
printPairs(arr1, 15)
print()
arr2 = np.array([2,-3,1,9,4,5])
printPairs(arr2, 6)
print()
arr3 = np.array([5, 9, 7, 6, 10])
printPairs(arr3, 18)
print()