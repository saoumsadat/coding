import numpy as np

n = int(input())
ori_arr = np.zeros(n, dtype=int)

for x in range(0, n):
    val = int(input())
    ori_arr[x] = val

print(f"Original Array: {ori_arr}")

for x in range(0, n):
    if ori_arr[x] > 0:
        ori_arr[x] = 1
    else:
        ori_arr[x] = 0

print(f"After modifying: {ori_arr}")